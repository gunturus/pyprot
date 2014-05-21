# sr 01/10/2014

# Takes a single- or multi-molecule MOL2 file and checks if
# 2 functional groups are within a specified distance (in Angstrom).
# Writes all molecules that match the functional group distance
# criteria to a new MOL2 file.

import sys
import os
import pyprot.mol2

def create_atom_list(func_groups, charge_ranges):
    """ Creates a list mapping charge ranges to functional groups.
        E.g., [['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]

    """
    atom_list = []
    i = 0
    for atom in func_groups:
        try:
            curr_range = charge_ranges[i].split(',')
            atom_list.append([atom, float(curr_range[0]), float(curr_range[1])])
        except IndexError:
            atom_list.append([atom])
        i += 1
    return atom_list

try:
    assert len(sys.argv) == 6

    in_mol2file = sys.argv[1]
    func_groups = sys.argv[2].split(',')
    charge_ranges = sys.argv[3].split(';')
    distance = float(sys.argv[4])
    assert len(func_groups) == 2, "Please provide 2 functional groups"
    assert len(charge_ranges) <= 2, "Please provide no more than 2 charge ranges"
    out_mol2file = sys.argv[5]


    atom_list = create_atom_dict(func_groups, charge_ranges)

    single_mol2s_in = pyprot.mol2.mol2_io.split_multimol2(in_mol2file)
    single_mol2s_out = []

    for mol2 in single_mol2s_in:
        mol2_lines = mol2[1].split('\n')
        if pyprot.mol2.mol2_filter.distance_match(mol2_lines, atom_dict, distance):
            single_mol2s_out.append(mol2)

    with open(out_mol2file, 'w') as out_file:
        for mol2 in single_mol2s_out:
            out_file.write(mol2[1])

except:
    print("""
Takes a single- or multi-molecule MOL2 file and checks if
2 functional groups are within a specified distance.
Writes molecules that match the criteria to a new MOL2 file.
""")
    print("ERROR\nUSAGE: python intramol_funcgroup_dist.py mol2-file.mol2 functional-groups charge-ranges distance out.mol2")
    print("\nEXAMPLE:\npython intramol_funcgroup_dist.py mymol2.mol2 'O.2,O.3' '-0.8,-0.5;-0.5,-0.9' '1.0' filtered.mol2\n")
