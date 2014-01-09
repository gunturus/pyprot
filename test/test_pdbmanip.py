import os
import pyprot.pdb as ppdb

pdb1 = ppdb.PdbObj("./test/test_data/small_3EIY.pdb")

def test_pdb_save():
    dest = "./test/test_data/out/test_pdb_save.pdb"
    os.remove(dest)
    pdb1.save_pdb(dest)
    assert os.path.isfile(dest) == True
