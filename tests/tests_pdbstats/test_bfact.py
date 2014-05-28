"""
Sebastian Raschka 2014

Unit tests for b-factor methods in PdbStats class
from pyprot.pdbstats.bfact

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/small_3EIY_h.pdb")


def test_get_bfactor():

    atom_bf = pdb1.get_bfactors(protein=True, ligand=False, main_chain="")
    assert(len(atom_bf) == 58), 'Missing or too many ATOM b-factor(s)'
    assert(atom_bf[0] == 52.73), 'Got wrong first ATOM b-factor'
    assert(atom_bf[-1] == 35.70), 'Got wrong last ATOM b-factor'

    hetatm_bf = pdb1.get_bfactors(protein=False, ligand=True, main_chain="")
    assert(len(hetatm_bf) == 3), 'Missing or to many HETATM b-factor(s)'
    assert(hetatm_bf[0] == 24.45), 'Got wrong first HETATM b-factor'
    assert(hetatm_bf[-1] == 30.89), 'Got wrong last HETATM b-factor'

    both_bf = pdb1.get_bfactors(protein=True, ligand=True, main_chain="")
    assert(both_bf == atom_bf + hetatm_bf), 'Missing or too many b-factor(s)'


def test_mean_bfactor():
    mean_atom_bf = pdb1.mean_bfactor(protein=True, ligand=False, main_chain="")
    assert(round(mean_atom_bf, 5) == 46.56017)

    mean_hetatm_bf = pdb1.mean_bfactor(protein=False, ligand=True, main_chain="")
    assert(round(mean_hetatm_bf, 5) == 27.35667)

    mean_both_bf = pdb1.mean_bfactor(protein=True, ligand=True, main_chain="")
    assert(round(mean_both_bf, 5) == 45.61574)


def test_median_bfactor():
    median_atom_bf = pdb1.median_bfactor(protein=True, ligand=False, main_chain="")
    assert(median_atom_bf == 47.35), print(median_atom_bf)

    median_hetatm_bf = pdb1.median_bfactor(protein=False, ligand=True, main_chain="")
    assert(median_hetatm_bf == 26.73)

    median_both_bf = pdb1.median_bfactor(protein=True, ligand=True, main_chain="")
    assert(median_both_bf== 47.0)
