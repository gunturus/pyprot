# sr 01/10/2014

# Takes a single- or multi-molecule MOL2 file (query) and a reference molecule (target) and
# checks if 2 functional groups (one in the query molecule(s) and one in the target molecule
# are within a specified distance (in Angstrom).
# Writes all molecules that match the functional group distance
# criteria to a new MOL2 file.

import sys
import pyprot.mol2io
import pyprot.mol2filter

def create_atom_dict(func_groups, charge_ranges):
    """ Creates a list mapping charge ranges to functional groups.
    E.g., [['O.2', -1.12, -0.792], ['O.2', -0.595, -0.315]]

    """
    atom_dict = dict()
    i = 0
    for atom in func_groups:
        try:
            curr_range = charge_ranges[i].split(',')
            atom_dict[atom] = float(curr_range[0]), float(curr_range[1])
        except IndexError:
            atom_dict[atom] = []
        i += 1
    return atom_dict

try:
    assert len(sys.argv) == 7

    in_mol2file1 = sys.argv[1]
    in_mol2file2 = sys.argv[1]
    func_groups = sys.argv[3].split(',')
    charge_ranges = sys.argv[4].split(';')
    distance = float(sys.argv[5])
    assert len(func_groups) == 2, "Please provide 2 functional groups"
    assert len(charge_ranges) <= 2, "Please provide no more than 2 charge ranges"
    out_mol2file = sys.argv[6]


    atom_dict = create_atom_dict(func_groups, charge_ranges)
    chargetype_list = [[k]+list(atom_dict[k]) for k in atom_dict]

    single_mol2s_in1 = pyprot.mol2io.split_multimol2(in_mol2file1)
    single_mol2s_in2 = pyprot.mol2io.split_multimol2(in_mol2file2)
    single_mol2s_out = []

    for query in single_mol2s_in1:
        for target in single_mol2s_in2:
            if pyprot.mol2filter.distance_match(query[1], chargetype_list, distance, target[1]):
                single_mol2s_out.append(query[1])

    with open(out_mol2file, 'w') as out_file:
        for mol2 in single_mol2s_out:
            out_file.write(mol2[1])

except:
    print("ERROR\nUSAGE: python intermol_funcgroup_dist.py query.mol2 target.mol2 functional-groups charge-ranges distance out.mol2")
    print("\nEXAMPLE: python intermol_funcgroup_dist.py my.mol2 myother.mol2 'O.2,O.3' '-0.8,-0.5;-0.5,-0.9' '1.0' filtered.mol2\n")
