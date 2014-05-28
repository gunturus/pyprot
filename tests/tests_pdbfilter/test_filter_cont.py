"""
Sebastian Raschka 2014

Unit tests for pdb filtering function _filter_column_matchs
in pdbfilter.py

"""

import pyprot
from pyprot.pdbfilter import _filter_column_match

def test_filter_column_match():

    test_data = []

    with open("./tests/data/pdbs/3EIY.pdb") as data:
        for line in data:
            test_data.append(line.strip())

    filtered_a = _filter_column_match\
            (test_data, ["ATOM", "END"])
    filtered_b = _filter_column_match\
            (test_data, ["atom", "end"])
    filtered_c = _filter_column_match\
            (test_data, ["END"])
    filtered_d = _filter_column_match\
            (test_data, ["END", "MASTER"])
    filtered_e = _filter_column_match\
            (test_data, ["end", "atom"], case_sensitive = False)
    filtered_f = _filter_column_match\
            (test_data, ["POP"], col_start_pos = 17)

    assert(len(filtered_a) > 0)
    assert(len(filtered_a) < len(test_data))
    assert(len(filtered_b) == 0)
    assert(len(filtered_c) == 1)
    assert(len(filtered_d) == 2)
    assert(len(filtered_e) == len(filtered_a))
    assert(len(filtered_f) == 9)


def test_filter_col_match_exclude():
    pdb = pyprot.Pdb("./tests/data/pdbs/small_3EIY_noH.pdb")
    data1 = _filter_column_match(
            pdb.cont, ["ATOM"], exclude = True)
    assert(len(data1) == 18)
    data2 = _filter_column_match(
            pdb.cont, ["ATOM","HETATM","TER","NA","MASTER"], exclude = True)
    assert(len(data2) == 13)
