"""
Sebastian Raschka 2014

Unit tests for split_multimol2 function in mol2io.py

"""

from pyprot.mol2io import split_multimol2

mol2file = "./tests/data/mol2s/confs.mol2"

def test_split_multimol2():
    res = list(split_multimol2(mol2file))
    assert(len(res) == 200)
    assert(res[2][0] == "ZINC00000016_3")
    assert(res[4][1].startswith("@<TRIPOS>MOLECULE") == True)
