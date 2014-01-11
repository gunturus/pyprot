import pyprot.pdb as ppdb

pdb1 = ppdb.PdbObj("./test/test_data/3EIY.pdb")


def test_constructor():
    assert len(pdb1.cont) == 2147
    assert len(pdb1.atom) == 1330
    assert len(pdb1.hetatm) == 151
    assert len(pdb1.conect) == 54


