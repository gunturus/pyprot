import pyprot.mol2 as mol2

mol2file = "./test/test_data/mol2/confs.mol2"

def test_split_multimol2():
    res = list(mol2.mol2_io.split_multimol2(mol2file))        
    assert len(res) == 200
    assert res[2][0] == "ZINC00000016_3"
    assert res[4][1].startswith("@<TRIPOS>MOLECULE") == True
