"""
Sebastian Raschka 2014

Unit tests for to_fasta method in PdbManip class
from pyprot.pdbmanip.
PdbManip is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/short_RIV_1.pdb")
pdb2 = pyprot.Pdb("./tests/data/pdbs/3B7V.pdb")

def test_to_fasta():
    expect = {'H': ['K'], 'L': ['D', 'I', 'V', 'M']}
    assert(pdb1.to_fasta() == expect)


def test_to_fasta():
    """ 
    Test for unusual amino acids in HETATMs, 
    here X in chain C from HETATM LNT. 
    
    """
    expect = {'C': ['N', 'L', 'X', 'Q', 'I'
                    ], 
              'B': ['P', 'Q', 'I', 'T', 'L', 'W', 'K', 'R', 'P', 'L', 'V', 'T', 'I', 'K', 'I', 'G', 
                    'G', 'Q', 'L', 'K', 'E', 'A', 'L', 'L', 'D', 'T', 'G', 'A', 'D', 'D', 'T', 'V', 'I', 'E', 'E', 'M', 'S', 'L', 
                    'P', 'G', 'R', 'W', 'K', 'P', 'K', 'M', 'I', 'G', 'G', 'I', 'G', 'G', 'F', 'I', 'K', 'V', 'R', 'Q', 'Y', 'D', 
                    'Q', 'I', 'I', 'I', 'E', 'I', 'A', 'G', 'H', 'K', 'A', 'I', 'G', 'T', 'V', 'L', 'V', 'G', 'P', 'T', 'P', 'V', 
                    'N', 'I', 'I', 'G', 'R', 'N', 'L', 'L', 'T', 'Q', 'I', 'G', 'A', 'T', 'L', 'N', 'F'
                    ], 
              'A': ['P', 'Q', 'I', 'T', 'L', 'W', 'K', 'R', 'P', 'L', 'V', 'T', 'I', 'K', 'I', 'G', 'G', 'Q', 'L', 'K', 'E', 'A', 
                    'L', 'L', 'D', 'T', 'G', 'A', 'D', 'D', 'T', 'V', 'I', 'E', 'E', 'M', 'S', 'L', 'P', 'G', 'R', 'W', 'K', 'P', 
                    'K', 'M', 'I', 'G', 'G', 'I', 'G', 'G', 'F', 'I', 'K', 'V', 'R', 'Q', 'Y', 'D', 'Q', 'I', 'I', 'I', 'E', 'I', 
                    'A', 'G', 'H', 'K', 'A', 'I', 'G', 'T', 'V', 'L', 'V', 'G', 'P', 'T', 'P', 'V', 'N', 'I', 'I', 'G', 'R', 'N', 
                    'L', 'L', 'T', 'Q', 'I', 'G', 'A', 'T', 'L', 'N', 'F'
                    ]
             }
    assert(pdb2.to_fasta(hetatm=True) == expect)
