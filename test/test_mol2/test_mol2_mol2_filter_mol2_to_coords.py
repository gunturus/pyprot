import pyprot.mol2 as mol2

def test_mol2_to_coords():
    line = "25 O1         -3.9941    5.6485   15.3588 O.3       1 <0>        -0.7380"
    res = mol2.mol2_to_coords(line)        
    assert res == [-3.9941, 5.6485, 15.3588]
