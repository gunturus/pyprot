"""
Sebastian Raschka 2014

Unit tests for strip_water method in PdbManip class
from pyprot.pdbmanip.
PdbManip is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/short_RIV_2.pdb")

def test_strip_water():
    out = [
        'ORIGX2      0.000000  1.000000  0.000000        0.00000',
        'ORIGX3      0.000000  0.000000  1.000000        0.00000',
        'SCALE1      0.013187  0.007613  0.000000        0.00000',
        'SCALE2      0.000000  0.015227  0.000000        0.00000',
        'SCALE3      0.000000  0.000000  0.006515        0.00000',
        'ATOM      1  N   ASP L   1      11.431   9.546  26.980  1.00 42.84           N',
        'ATOM   3335  CB  LYS H 228      55.744  47.316  42.227  1.00 55.82           C',
        'ATOM   3336  CG  LYS H 228      54.735  46.929  43.279  1.00 59.26           C',
        'ATOM   3337  CD  LYS H 228      53.322  47.322  42.862  1.00 62.38           C',
        'ATOM   3338  CE  LYS H 228      52.879  46.619  41.585  1.00 64.90           C',
        'ATOM   3339  NZ  LYS H 228      51.517  47.052  41.158  1.00 60.26           N',
        'ATOM   3340  OXT LYS H 228      57.902  49.285  43.398  1.00 70.44           O',
        'TER    3341      LYS H 228',
        'HETATM 3356  C15 OBE H 201      24.725  -3.136  27.406  1.00 27.56           C',
        'HETATM 3363  O5  OBE H 201      31.267  -3.891  23.783  1.00 37.43           O',
        'CONECT  157  711',
        'CONECT  711  157',
        'CONECT 1051 1533',
        'CONECT 2787 3204',
        'CONECT 2788 3205',
        'CONECT 3362 3356',
        'CONECT 3363 3352',
        'MASTER      286    0    1   10   47    0    4    6 3543    2   34   35',
        'END'
    ]
    assert(out == pdb1.strip_water())
