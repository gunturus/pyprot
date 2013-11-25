import pyprot

new_pdb = pyprot.PdbObj("./test/test_data/3EIY.pdb")

def test_center_of_mass():
    assert new_pdb.center_of_mass() == [8.979, 41.661, 12.495]

