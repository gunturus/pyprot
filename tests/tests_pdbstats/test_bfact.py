"""
Sebastian Raschka 2014

Unit tests for b-factor methods in PdbStats class
from pyprot.pdbstats.bfact

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/small_3EIY_h.pdb")


def test_get_bfactor():

    atom_bf = pdb1.get_bfactors(protein=True, ligand=False, atoms='all')
    assert(len(atom_bf) == 58), 'Missing or too many ATOM b-factor(s)'
    assert(atom_bf[0] == 52.73), 'Got wrong first ATOM b-factor'
    assert(atom_bf[-1] == 35.70), 'Got wrong last ATOM b-factor'

    hetatm_bf = pdb1.get_bfactors(protein=False, ligand=True, atoms='all')
    assert(len(hetatm_bf) == 3), 'Missing or to many HETATM b-factor(s)'
    assert(hetatm_bf[0] == 24.45), 'Got wrong first HETATM b-factor'
    assert(hetatm_bf[-1] == 30.89), 'Got wrong last HETATM b-factor'

    both_bf = pdb1.get_bfactors(protein=True, ligand=True, atoms='all')
    assert(both_bf == atom_bf + hetatm_bf), 'Missing or too many b-factor(s)'


def test_bfactor_mean():
    mean_atom_bf = pdb1.bfactor_mean(protein=True, ligand=False, atoms='all')
    assert(round(mean_atom_bf, 5) == 46.56017)

    mean_hetatm_bf = pdb1.bfactor_mean(protein=False, ligand=True, atoms='all')
    assert(round(mean_hetatm_bf, 5) == 27.35667)

    mean_both_bf = pdb1.bfactor_mean(protein=True, ligand=True, atoms='all')
    assert(round(mean_both_bf, 5) == 45.61574)


def test_bfactor_median():
    median_atom_bf = pdb1.bfactor_median(protein=True, ligand=False, atoms='all')
    assert(median_atom_bf == 47.35), print(median_atom_bf)

    median_hetatm_bf = pdb1.bfactor_median(protein=False, ligand=True, atoms='all')
    assert(median_hetatm_bf == 26.73)

    median_both_bf = pdb1.bfactor_median(protein=True, ligand=True, atoms='all')
    assert(median_both_bf== 47.0)

    
def test_bfactor_std_dev():
    std_dev_atom_bf = pdb1.bfactor_std_dev(protein=True, ligand=False, atoms='all')
    assert(round(std_dev_atom_bf,3) == 4.579), print(std_dev_atom_bf)

    std_dev_hetatm_bf = pdb1.bfactor_std_dev(protein=False, ligand=True, atoms='all')
    assert(round(std_dev_hetatm_bf,3) == 2.666), print(std_dev_hetatm_bf)

    std_dev_both_bf = pdb1.bfactor_std_dev(protein=True, ligand=True, atoms='all')
    assert(round(std_dev_both_bf,3) == 6.126), print(std_dev_both_bf)


def test_bfactor_std_err():
    std_err_atom_bf = pdb1.bfactor_std_err(protein=True, ligand=False, atoms='all')
    assert(round(std_err_atom_bf,3) == 0.607), print(std_err_atom_bf)

    std_err_hetatm_bf = pdb1.bfactor_std_err(protein=False, ligand=True, atoms='all')
    assert(round(std_err_hetatm_bf,3) == 1.885), print(std_err_hetatm_bf)

    std_err_both_bf = pdb1.bfactor_std_err(protein=True, ligand=True, atoms='all')
    assert(round(std_err_both_bf,3) == 0.791), print(std_err_both_bf)
    

def test_bfactor_stats():
    stats_atom_bf = pdb1.bfactor_stats(protein=True, ligand=False, atoms='all')
    assert([round(i,3) for i in stats_atom_bf] == [47.350, 46.560, 4.579, 0.607]), print(stats_atom_bf)
