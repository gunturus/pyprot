"""
Sebastian Raschka 2014

Unit tests for get_chains method in PdbManip class
from pyprot.pdbmanip.
PdbManip is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/short_RIV_3_mod.pdb")

def test_get_atom_chains():
    out = {
        'L': ['ATOM      1  N   ASP L   1      11.431   9.546  26.980  1.00 42.84           N',
              'ATOM      2  N   ASP L   1      11.431   9.546  26.980  1.00 42.84           N',
              'TER       3      ASP L   1',
              'HETATM 3440  O   HOH L 290      39.794  19.138  55.192  1.00 45.73           O',
              'HETATM 3441  O   HOH L 291      30.165  39.040  46.112  1.00 31.60           O',
              'HETATM 3442  O   HOH L 292      11.904  -4.213  38.248  1.00 47.47           O'
             ],
        'H': ['ATOM   3335  CB  LYS H 228      55.744  47.316  42.227  1.00 55.82           C',
              'ATOM   3336  CG  LYS H 228      54.735  46.929  43.279  1.00 59.26           C',
              'ATOM   3337  CD  LYS H 228      53.322  47.322  42.862  1.00 62.38           C',
              'ATOM   3338  CE  LYS H 228      52.879  46.619  41.585  1.00 64.90           C',
              'ATOM   3339  NZ  LYS H 228      51.517  47.052  41.158  1.00 60.26           N',
              'ATOM   3340  OXT LYS H 228      57.902  49.285  43.398  1.00 70.44           O',
              'TER    3341      LYS H 228',
              'HETATM 3356  C15 OBE H 201      24.725  -3.136  27.406  1.00 27.56           C',
              'HETATM 3363  O5  OBE H 201      31.267  -3.891  23.783  1.00 37.43           O'
             ]
          }


    chain_dict = pdb1._get_chains() 

    assert(len(chain_dict['L']) == 6)    
    assert(len(chain_dict['H']) == 9)
    assert(chain_dict == out)
