import pyprot

lig1 = pyprot.PdbObj("./test/test_data/lig_conf_1.pdb")
lig2 = pyprot.PdbObj("./test/test_data/lig_conf_2.pdb")
pdb1 = pyprot.PdbObj("./test/test_data/3EIY.pdb")
pdb2 = pyprot.PdbObj("./test/test_data/3EIY.pdb")

def test_rmsd():
    assert round(lig1.rmsd(lig2, ligand = True),4) == 1.9959
    assert pdb1.rmsd(pdb2) == 0.0

if __name__ == "__main__":
    test_rmsd()
