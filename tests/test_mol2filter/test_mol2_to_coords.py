"""
Sebastian Raschka 2014

Unit tests for mol2_to_coords function in mol2filter.py

"""

from pyprot.mol2filter import mol2_to_coords

def test_mol2_to_coords():
    line = "25 O1         -3.9941    5.6485   15.3588 O.3       1 <0>        -0.7380"
    res = mol2_to_coords(line)
    assert(res == [-3.9941, 5.6485, 15.3588])
