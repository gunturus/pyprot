# sr 11/25/2013

import pyprot

def test_get_bfactor():
    new_pdb = pyprot.PdbObj("./test/test_data/bfact.pdb")
    new_pdb.get_bfactors() 
