# sr 11/25/2013

import pyprot

new_pdb = pyprot.PdbObj("./test/test_data/bfact.pdb")

def test_get_bfactor():
    b_atoms = [54.68, 55.07, 54.60, 57.59, 61.87, 63.51, 63.20, 55.71]
    b_hets = [24.45, 26.73, 30.89, 32.68, 32.62, 33.46, 30.47, 33.48]
    assert new_pdb.get_bfactors() == b_atoms
    assert new_pdb.get_bfactors(False, True) == b_hets
    assert new_pdb.get_bfactors(True, True) == b_atoms + b_hets

def test_median_bfactor():
    assert new_pdb.median_bfactor() == 56.650000000000006
    assert new_pdb.median_bfactor(False, True) == 31.755
    assert new_pdb.median_bfactor(True, True) == 44.04

def test_mean_bfactor():
    assert new_pdb.mean_bfactor() == 58.278749999999995
    assert new_pdb.mean_bfactor(False, True) == 30.5975
    assert new_pdb.mean_bfactor(True, True) == 44.438125
