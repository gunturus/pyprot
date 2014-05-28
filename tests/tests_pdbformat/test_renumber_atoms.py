"""
Sebastian Raschka 2014

Unit tests for renumber_atoms method in PdbFormat class
from pyprot.pdbformat.
PdbFormat is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb('./tests/data/pdbs/short_1vr1_colfix.pdb')

def test_renumber_atoms():
    renumbered = pdb1.renumber_atoms(start=4)
    expect = 'ATOM     91  CA  LYS L  10      -3.668  17.825  17.723  1.00 34.32           C'
    assert(renumbered[100] == expect), '\nexpect:\n%s\ngot:\n%s' %(expect, renumbered[100])
