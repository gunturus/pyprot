"""
Sebastian Raschka 2014

Unit tests for save_pdb method in PdbManip class
from pyprot.pdbmanip.
PdbManip is a parent class of the Pdb class.

"""

import os
import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/small_3EIY_noH.pdb")

def test_save_pdb():
    dest = "./tests/data/output_pdbs/test_pdb_save.pdb"
    if os.path.isfile(dest):
        os.remove(dest)
    pdb1.save_pdb(dest)
    assert(os.path.isfile(dest) == True)
