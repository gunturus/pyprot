import pyprot.mol2 as mol2

def test_multi_mol2list():
    assert len(mol2.multi_mol2list('./test/test_data/multimol2_small1.mol2')) == 3
