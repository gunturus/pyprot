import pyprot

def test_constructor():
    pdb = pyprot.PdbObj()
    pdb = pyprot.PdbObj("./test/test_data/3EIY.pdb")
    assert len(pdb.cont) == 2147
    assert len(pdb.atom) == 1330
    assert len(pdb.hetatm) == 151
    assert len(pdb.conect) == 54

def test_print():
    pdb = pyprot.PdbObj()
    print(pdb)
    del pdb


