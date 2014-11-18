"""
Sebastian Raschka 2014

Unit tests for  create_chargetype_list function in mol2filter.py

"""

from pyprot.mol2filter import create_chargetype_list

def test_create_chargetype_list():
    l1 = create_chargetype_list(group_charge_pairs='O.2,-1.2,2;O.3,-20.0,100.0' ,atom_list=None)
    assert l1 == [['O.2', -1.2, 2.0], ['O.3', -20.0, 100.0]]

