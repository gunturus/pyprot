import pyprot.pdb as ppdb

lig1 = pyprot.PdbObj("./test/test_data/lig_conf_1.pdb")
lig2 = pyprot.PdbObj("./test/test_data/lig_conf_2.pdb")
pdb1 = pyprot.PdbObj("./test/test_data/3EIY.pdb")
pdb2 = pyprot.PdbObj("./test/test_data/3EIY.pdb")
pdb3 = pyprot.PdbObj("./test/test_data/1T48_995.pdb")
pdb4 = pyprot.PdbObj("./test/test_data/1T49_995.pdb")

def test_rmsd():
    assert lig1.rmsd(lig2, ligand = True) == 1.9959
    assert lig1.rmsd(lig2, ligand = True, atoms = "all") == 2.6444
    assert pdb1.rmsd(pdb2) == 0.0
    assert pdb3.rmsd(pdb4) == 0.7377
    assert pdb3.rmsd(pdb4, atoms = "ca") == 0.4785
if __name__ == "__main__":
    test_rmsd()
