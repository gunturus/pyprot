"""
Sebastian Raschka 2014

Unit tests for select_residues method in PdbManip class
from pyprot.pdbmanip.
PdbManip is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/short_RIV_1.pdb")

def test_select_atoms():
    protein_9_12 = [
    'ATOM      9  N   ILE L   2      13.612   8.513  29.609  1.00 34.82           N',
    'ATOM     10  CA  ILE L   2      13.590   8.155  31.016  1.00 29.86           C',
    'ATOM     11  C   ILE L   2      14.203   9.319  31.777  1.00 30.58           C',
    'ATOM     12  O   ILE L   2      15.263   9.822  31.415  1.00 32.54           O',
    ]
    
    
    lig_3357_3361 = [
    'HETATM 3357  C16 OBE H 201      20.533  -2.037  27.441  1.00 16.26           C',
    'HETATM 3358  N1  OBE H 201      21.820  -2.333  26.716  1.00 21.52           N',
    'HETATM 3359  O1  OBE H 201      25.350  -3.062  24.488  1.00 23.55           O',
    'HETATM 3360  O2  OBE H 201      26.881  -1.489  24.963  1.00 21.32           O',
    'HETATM 3361  O3  OBE H 201      25.782  -3.225  27.941  1.00 19.70           O',
    ]

    assert(pdb1.select_atoms(pos=[9, 12], protein=True, ligand=False) == protein_9_12)
    assert(pdb1.select_atoms(pos=[3357, 3361], protein=False, ligand=True) == lig_3357_3361)
