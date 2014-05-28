"""
Sebastian Raschka 2014

Unit tests for center_of_mass methods in PdbStats class
from pyprot.pdbstats.center_of_mass

"""

import pyprot

pdb1 = pyprot.Pdb('./tests/data/pdbs/3EIY.pdb')

def test_center_of_mass():
    assert pdb1.center_of_mass(protein=True, ligand=False) == [8.979, 41.661, 12.495]
