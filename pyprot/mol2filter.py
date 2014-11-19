"""
Sub-package for filtering MOL2 files by different criteria.
"""

import os

def mol2_to_coords(line):
    """ 
    Extracts XYZ coordinates from MOL2 atom entry line. 
    
    Parameters
    ----------
    line : `string`.
      One MOL2-file line with coordinate content.
        
    Returns
    ----------
    C : `list` = `[float_x, float_y, float_z]`.
      List of the x, y, and z coordinates of the atom.
    
    """
    line = line.strip().split()
    return [float(i) for i in line[2:5]]


def create_atom_dict(group_charge_pairs, atom_dict=None):
    """ 
    Creates a dictionary mapping charge ranges to functional groups.
    
    Parameters
    ----------    
    
    group_charge_pairs : `list` = `[pair_1, pair2, ...]`.
      Pair of names of functional groups and charge ranges.
      E.g., `['O.2,-1.12,-0.792', 'O.3,-0.595,-0.315']`
        
    atom_dict : `dict`
        Existing atom dictionary to update or `None` to create a new atom dictionary.
    
    Returns
    ----------     
    
    atom_dict : dict = `{atom:[min_charge, maxcharge], ...}`.
        A dictionary mapping of `group_charge_pairs` input.
        E.g., {'O.2':[-1.12, -0.792], 'O.3':[-0.595, -0.315]}

    """
    if not atom_dict:
        atom_dict = dict()
    for pair in group_charge_pairs:
        a, c1, c2 = pair.strip().split(',')
        c1,c2 = float(c1), float(c2)
        atom_dict[a] = [c1,c2]
    return atom_dict


def create_chargetype_list(group_charge_pairs, atom_list=None):
    """ 
    Creates a list mapping charge ranges to functional groups.
    
    Parameters
    ----------      
    
    group_charge_pairs : `string`.
      Semi-colon separated `string` of names of functional groups and charge ranges.
      E.g., `'O.2,-1.12,-0.792;O.3,-0.595,-0.315'`
    
    atom_list : `list`.
      Existing atom list to update or `None` to create a new atom `list`.

    Returns
    ----------  
    
    atom_list : `list`.
      A list mapping of the input.
      E.g., `[['O.2', -1.2, 2.0], ['O.3', -20.0, 100.0]]`.

    """
    if not atom_list:
        atom_list = []
    s = group_charge_pairs.split(';')
    for pair in s:
        a, c1, c2 = pair.strip().split(',')
        c1, c2 = float(c1), float(c2)
        atom_list.append([a, c1, c2])
    return atom_list


def _filter_atoms(mol2_cont, chargetype_list):
    """
    Searches for atom types in a mol2 file.
    Returns the mol2 lines that contains matches as a list.

    Parameters
    ----------    

    mol2_cont : `list`.
      MOL2 file content as where each `list` item represents a line.
      
    chargetype_list : `list`. 
      `list` of sub`list`s that consists of atom types as first sublist item, 
      and the allowed charge range is given as 2nd and 3rd sublist items.
      E.g., `[['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]`


    Returns
    ---------- 

    matched_lines : `list`.
      The mol2 lines that contains matches as a `list`.

    """
    matched_lines = []
    for line in mol2_cont:
        fields = line.split()
        for atom in chargetype_list:
            if atom[0] in fields:
                if len(atom) == 3: # optional: requires user defined charge range
                    try:
                        charge = float(fields[-1])
                    except ValueError:
                        print("Error: cannot get charge")
                        continue
                    if charge >= atom[1] \
                            and charge <= atom[2]:
                        matched_lines.append(line)
                else:
                    matched_lines.append(line)
        if '@<TRIPOS>BOND' in fields:
            break
    return matched_lines


def count_matches(mol2_cont, chargetype_list):
    """
    Checks of MOL2 structure contains atom types in a charge range.

    Parameters
    ----------   

    mol2_cont : `list`.
      MOL2 file content as where each `list` item represents a line.
      
    chargetype_list : `list`. 
      `list` of sub`list`s that consists of atom types as first sublist item, 
      and the allowed charge range is given as 2nd and 3rd sublist items.
      E.g., `[['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]`

    Returns
    ---------- 

    cnt : `int`.
      Number of how many atoms the MOL2 structure contains that match the
      atom-charge pairs in the `chargetype_list`.

    """
    cnt = len(_filter_atoms(mol2_cont, chargetype_list))
    return cnt


def match_all(mol2_cont, chargetype_list):
    """
    Checks if molecule matches all criteria (all atoms or atoms and charge ranges
            in the `chargetype_list`).

    Parameters
    ----------   

    mol2_cont : `list`.
      MOL2 file content as where each `list` item represents a line.
      
    chargetype_list : `list`.
      `list` of sub`list`s that consists of atom types as first sublist item, 
      and the allowed charge range is given as 2nd and 3rd sublist items.
      E.g., `[['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]`

    Returns
    ----------
    
    matched : `bool`.
      True if all atoms are matched.

    """
    prefilter = _filter_atoms(mol2_cont, chargetype_list)
    check_dict = {idx:0 for idx in range(len(chargetype_list))}
    matched = False
    
    for line in prefilter:
        fields = line.split()
        for idx,atom in enumerate(chargetype_list):
            if atom[0] in fields:
                if len(atom) == 3: # optional: requires user defined charge range
                    try:
                        charge = float(fields[-1])
                    except ValueError:
                        print("Error: cannot get charge")
                        continue
                    if charge >= atom[1] and charge <= atom[2]:
                        check_dict[idx] += 1
                else:
                    check_dict[idx] += 1
        if '@<TRIPOS>BOND' in fields:
            break
    for i in check_dict.values():
        if i < 1:
            return matched
    
    matched = True
    return matched


def intermol_distance_match(mol2_ref, mol2_query, chargetype_list, distance):
    """
    Searches for atom types in MOL2 file(s). Returns True if
    2 atoms of the defined types are within a certain distance range.

    Parameters
    ----------   
    
    mol2_ref (list) : `list`.
        MOL2 file content of the reference molecule where each list item represents
        a single line in the mol2 file.
        mol2_query (list): mol2 file content of a query molecule where each list item represents
                     a single line in the mol2 file.
    chargetype_list : `list`.
      `list` of sub`list`s that consists of atom types as first sublist item, 
      and the allowed charge range is given as 2nd and 3rd sublist items.
      E.g., `[['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]`
      
    distance : `list`. 
      List of 2 numbers that specify the allowed distance
      between the 2 atoms in Angstrom. E.g., `[4, 12.5]`

    Returns
    ----------

    match_dict : `dict`.
      A dictionary with the count of chargetypes matched.
      E.g., `{ 0: [['O.2', -1.0, 0.0], 3],         # 3 matches
              1: [['N.am', -0.8181, -0.2181], 1]  # 1 match
            }`

    """
    match_dict = {i:[chargetype_list[i], 0] for i in range(len(chargetype_list))}
    
    for idx,lst in enumerate(chargetype_list):
        atom1_matches = _filter_atoms(mol2_ref, [lst])
        atom2_matches = _filter_atoms(mol2_query, [lst])
        coords_1 = []
        coords_2 = []
        for line in atom1_matches:
            line = line.strip().split()
            coords_1.append([float(i) for i in line[2:5]])
            # expected format of a 'line':
            # ['11', 'O1', '0.0847', '-6.3706', '-0.6593', 'O.2', '1', '<0>', '-0.0409']
        for line in atom2_matches:
            line = line.strip().split()
            coords_2.append([float(i) for i in line[2:5]])
        
        for xyz_1 in coords_1:
            for xyz_2 in coords_2:
                dist = sum([(j-i)**2 for i,j in zip(xyz_1,xyz_2)])**0.5
                if dist >= distance[0] and dist <= distance[1]:
                    match_dict[idx][1] += 1
                    break

    return match_dict
