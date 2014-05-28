"""
Sebastian Raschka 2014

Unit tests for renumber_residues method in PdbFormat class
from pyprot.pdbformat.
PdbFormat is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb('./tests/data/pdbs/short_1vr1_colfix.pdb')

def test_renumber_residues():
    renumbered = pdb1.renumber_residues(start=2)
    expect1 =  'ATOM     14  N   CYS L   4      10.930  16.366  19.574  1.00 28.95           N'
    expect2 =  'ATOM    127  N   LYS L  18      -5.816   5.075  21.742  1.00 28.96           N'
    assert(renumbered[26] == expect1),  '\nexpect:\n%s\ngot:\n%s' %(expect1, renumbered[26])
    assert(renumbered[139] == expect2), '\nexpect:\n%s\ngot:\n%s' %(expect2, renumbered[139])
