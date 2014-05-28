"""
Sebastian Raschka 2014

Unit tests for __init__  method in Pdb child class
from pyprot.pdbmain.

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/3EIY.pdb")

def test_init():
    assert(len(pdb1.cont) == 2147)
    assert(len(pdb1.atom) == 1330)
    assert(len(pdb1.atom_ter) == 1331)
    assert(len(pdb1.hetatm) == 151)
    assert(len(pdb1.conect) == 54)
