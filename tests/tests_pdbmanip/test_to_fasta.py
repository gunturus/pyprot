"""
Sebastian Raschka 2014

Unit tests for to_fasta method in PdbManip class
from pyprot.pdbmanip.
PdbManip is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/short_RIV_1.pdb")

def test_to_fasta():
    print(pdb1.to_fasta())

    assert pdb1.to_fasta() == {'H': ['K'], 'L': ['D', 'I', 'V', 'M']}
