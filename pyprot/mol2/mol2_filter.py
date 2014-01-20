import os

def _filter_atoms(mol2_cont, atom_dict):
    '''Searches for atom types in a mol2 file.
       Returns the mol2 lines that contains matches as a list.
    Args:
        mol2_cont (list): mol2 file content as where each list item represents
                     a line 
        atom_dict (dict): Dictionary that consists of atom types as keys 
                and their allowed charge range as 2 integers in a list
                (inclusive lower and inclusive upper boundary). If
                charge list is empty, charge comparison is ignored.
                e.g., {'O.3':[-0.42, -0.12], 'O.2':[]}
    Returns list: 
        Returns the mol2 lines that contains matches as a list.

    '''
    matched_lines = []
    for line in mol2_cont:
        fields = line.split()
        for atom in atom_dict.keys():
            if atom in fields:
                if atom_dict[atom]: # optional: requires user defined charge range
                    try:
                        charge = float(fields[-1])
                    except ValueError:
                        print("Error: cannot get charge")
                        continue
                    if charge >= atom_dict[atom][0] \
                            and charge <= atom_dict[atom][1]:
                        matched_lines.append(line)
                else:
                    matched_lines.append(line)
        if '@<TRIPOS>BOND' in fields:
            break
    return matched_lines


def contains_atom(mol2_cont, atom_dict):
    '''Searches for atom types in a mol2 file. Returns True if
       mol2 file contains atom types in the specified charge range
    Args:
       mol2_cont (list): mol2 file content as where each list item represents
                     a line 
        atom_dict (dict): Dictionary that consists of atom types as keys 
                and their allowed charge range as 2 integers in a list
                (inclusive lower and inclusive upper boundary). If
                charge list is empty, charge comparison is ignored.
                e.g., {'O.3':[-0.42, -0.12], 'O.2':[]}
    Returns bool: 
        True if one of the atoms in atom_dict was found in the 
        mol2 string and its charge is in the specified range.

    '''
    return len(_filter_atoms(mol2_cont, atom_dict)) >= len(atom_dict.keys()) 


def distance_match(mol2_cont, atom_dict, distance):
    '''Searches for atom types in a mol2 file. Returns True if
       2 atoms of the defined types are within a certain distance range.
    Args:
       mol2_cont (list): mol2 file content as where each list item represents
                     a line 
        atom_dict (dict): Dictionary that consists of atom types as keys 
                and their allowed charge range as 2 integers in a list
                (inclusive lower and inclusive upper boundary). If
                charge list is empty, charge comparison is ignored.
                e.g., {'O.3':[-0.42, -0.12], 'O.2':[]}
                Max number of keys in the dictionary is 2!
    Returns bool: 
        True if 2 atoms (each of one specified type) are within a 
        specified distance. 

    '''
    assert len(atom_dict.keys()) == 2   # can only compare 2 atoms
    atom_lines = _filter_atoms(mol2_cont, atom_dict)
    coords_1 = []
    coords_2 = []
    for line in atom_lines:
        line = line.strip().split()
        
        # expected format of a 'line':
        # ['11', 'O1', '0.0847', '-6.3706', '-0.6593', 'O.2', '1', '<0>', '-0.0409']
        
        coords = [float(i) for i in line[2:5]]
        if line[5] == list(atom_dict.keys())[0]:
            coords_1.append(coords)
        else:
            coords_2.append(coords)
    dist_match = False
    for xyz_1 in coords_1:
        for xyz_2 in coords_2:
            if sum([(j-i)**2 for i,j in zip(xyz_1,xyz_2)])**0.5 <= distance:
                dist_match = True
                break

    return dist_match      
