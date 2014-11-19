import os

def mol2_to_coords(line):
    """ Extracts XYZ coordinates from mol2 atom entry line. """
    line = line.strip().split()
    return [float(i) for i in line[2:5]]


def create_atom_dict(group_charge_pairs, atom_dict=None):
    """ 
    Creates a dictionary mapping charge ranges to functional groups.
    Keyword arguments:
        group_charge_pairs: List of names of functional groups and charge ranges.
                E.g., ['O.2,-1.12,-0.792', 'O.3,-0.595,-0.315']
        atom_dict: Existing atom dictionary to update or None to
                create a new atom dictionary.
    
    Returns a dictionary mapping of the input:
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
    Keyword arguments:
        group_charge_pairs: Semicolon-separated string 
                of names of functional groups and charge ranges.
                E.g., 'O.2,-1.12,-0.792;O.3,-0.595,-0.315'
        atom_list: Existing atom list to update or None to
                create a new atom list.
    
    Returns a dictionary mapping of the input:
        E.g., [['O.2', -1.2, 2.0], ['O.3', -20.0, 100.0]]

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

    Keyword arguments:
        mol2_cont (list): mol2 file content as where each list item represents
                     a line
        chargetype_list (list): List of sublists that consists of atom types as
                first sublist item, and the allowed charge range is given
                as 2nd and 3rd sublist items.
                Example: [['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]

    Returns:
         The mol2 lines that contains matches as a list.

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
    Returns number of atom type and charge matches.

    Keyword arguments:
        mol2_cont (list): mol2 file content as where each list item represents
                     a line
        chargetype_list (list): List of sublists that consists of atom types as
                first sublist item, and the allowed charge range is given
                as 2nd and 3rd sublist items.
                Example: [['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]

    Returns number of matches as integer.

    """
    return len(_filter_atoms(mol2_cont, chargetype_list))


def match_all(mol2_cont, chargetype_list):
    """
    Checks if molecule matches all criteria (all atoms or atoms and charge ranges
            in the chargetype_list).

    Keyword arguments:
       mol2_cont (list): mol2 file content as where each list item represents
                     a line
        chargetype_list (list): List of sublists that consists of atom types as
                first sublist item, and the allowed charge range is given
                as 2nd and 3rd sublist items.
                Example: [['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]

    Returns True if all atoms are matched.

    """
    prefilter = _filter_atoms(mol2_cont, chargetype_list)
    
    check_dict = {idx:0 for idx in range(len(chargetype_list))}
    
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
            return False
    return True


def intermol_distance_match(mol2_ref, mol2_query, chargetype_list, distance):
    """
    Searches for atom types in mol2 file(s). Returns True if
    2 atoms of the defined types are within a certain distance range.

    Keyword arguments:
        mol2_ref (list): mol2 file content of the reference molecule where each list item represents
                     a single line in the mol2 file.
        mol2_query (list): mol2 file content of a query molecule where each list item represents
                     a single line in the mol2 file.
        chargetype_list (list): List of sublists that consists of atom types as
                first sublist item, and the allowed charge range is given
                as 2nd and 3rd sublist items.
                Example: [['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]
                Max number of sublists is 2!
        distance (list): List of 2 numbers that specify the allowed distance
                between the 2 atoms in Angstrom. E.g., [4, 12.5]

    Returns a dictionary with the count of chargetypes matched.
        E.g., { 0: [['O.2', -1.0, 0.0], 3],         # 3 matches
                1: [['N.am', -0.8181, -0.2181], 1]  # 1 match
              }

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
