"""
Sebastian Raschka 2014

Unit tests for extract_chains method in PdbManip class
from pyprot.pdbmanip.
PdbManip is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/short_RIV_1.pdb")

def test_extract_chains():
    h_l = [
    'ATOM      1  N   ASP L   1      11.431   9.546  26.980  1.00 42.84           N',
    'ATOM      2  CA  ASP L   1      12.768   9.604  27.627  1.00 41.86           C',
    'ATOM      3  C   ASP L   1      12.634   9.246  29.088  1.00 41.46           C',
    'ATOM      4  O   ASP L   1      11.654   9.628  29.733  1.00 39.57           O',
    'ATOM      5  CB  ASP L   1      13.348  11.010  27.535  1.00 38.99           C',
    'ATOM      6  CG  ASP L   1      13.792  11.368  26.140  1.00 43.09           C',
    'ATOM      7  OD1 ASP L   1      13.329  10.708  25.180  1.00 41.52           O',
    'ATOM      8  OD2 ASP L   1      14.594  12.322  26.014  1.00 41.66           O',
    'ATOM      9  N   ILE L   2      13.612   8.513  29.609  1.00 34.82           N',
    'ATOM     10  CA  ILE L   2      13.590   8.155  31.016  1.00 29.86           C',
    'ATOM     11  C   ILE L   2      14.203   9.319  31.777  1.00 30.58           C',
    'ATOM     12  O   ILE L   2      15.263   9.822  31.415  1.00 32.54           O',
    'ATOM     13  CB  ILE L   2      14.380   6.874  31.272  1.00 23.91           C',
    'ATOM     14  CG1 ILE L   2      13.694   5.711  30.546  1.00 25.64           C',
    'ATOM     15  CG2 ILE L   2      14.456   6.609  32.773  1.00 20.81           C',
    'ATOM     16  CD1 ILE L   2      14.524   4.451  30.447  1.00 26.02           C',
    'ATOM     17  N   VAL L   3      13.515   9.759  32.818  1.00 28.51           N',
    'ATOM     18  CA  VAL L   3      13.974  10.886  33.618  1.00 25.67           C',
    'ATOM     19  C   VAL L   3      14.696  10.393  34.851  1.00 30.01           C',
    'ATOM     20  O   VAL L   3      14.147   9.608  35.635  1.00 24.91           O',
    'ATOM     21  CB  VAL L   3      12.783  11.750  34.073  1.00 30.33           C',
    'ATOM     22  CG1 VAL L   3      13.268  12.911  34.915  1.00 22.12           C',
    'ATOM     23  CG2 VAL L   3      12.013  12.237  32.864  1.00 24.01           C',
    'ATOM     24  N   MET L   4      15.933  10.849  35.017  1.00 30.22           N',
    'ATOM     25  CA  MET L   4      16.738  10.451  36.159  1.00 27.34           C',
    'ATOM   3335  CB  LYS H 228      55.744  47.316  42.227  1.00 55.82           C',
    'ATOM   3336  CG  LYS H 228      54.735  46.929  43.279  1.00 59.26           C',
    'ATOM   3337  CD  LYS H 228      53.322  47.322  42.862  1.00 62.38           C',
    'ATOM   3338  CE  LYS H 228      52.879  46.619  41.585  1.00 64.90           C',
    'ATOM   3339  NZ  LYS H 228      51.517  47.052  41.158  1.00 60.26           N',
    'ATOM   3340  OXT LYS H 228      57.902  49.285  43.398  1.00 70.44           O',
    'TER    3341      LYS H 228',
    'HETATM 3356  C15 OBE H 201      24.725  -3.136  27.406  1.00 27.56           C',
    'HETATM 3357  C16 OBE H 201      20.533  -2.037  27.441  1.00 16.26           C',
    'HETATM 3358  N1  OBE H 201      21.820  -2.333  26.716  1.00 21.52           N',
    'HETATM 3359  O1  OBE H 201      25.350  -3.062  24.488  1.00 23.55           O',
    'HETATM 3360  O2  OBE H 201      26.881  -1.489  24.963  1.00 21.32           O',
    'HETATM 3361  O3  OBE H 201      25.782  -3.225  27.941  1.00 19.70           O',
    'HETATM 3362  O4  OBE H 201      23.810  -4.086  27.519  1.00 23.18           O',
    'HETATM 3363  O5  OBE H 201      31.267  -3.891  23.783  1.00 37.43           O',
    'HETATM 3440  O   HOH L 290      39.794  19.138  55.192  1.00 45.73           O',
    'HETATM 3441  O   HOH L 291      30.165  39.040  46.112  1.00 31.60           O',
    'HETATM 3442  O   HOH L 292      11.904  -4.213  38.248  1.00 47.47           O',
    'HETATM 3443  O   HOH H 229      25.710   1.134  24.699  1.00 23.08           O',
    'HETATM 3444  O   HOH H 230      26.500  -1.587  30.027  1.00 24.76           O',
    'HETATM 3445  O   HOH H 231      39.649  16.017  31.547  1.00 57.79           O'
    ]

    h = [
    'ATOM   3335  CB  LYS H 228      55.744  47.316  42.227  1.00 55.82           C',
    'ATOM   3336  CG  LYS H 228      54.735  46.929  43.279  1.00 59.26           C',
    'ATOM   3337  CD  LYS H 228      53.322  47.322  42.862  1.00 62.38           C',
    'ATOM   3338  CE  LYS H 228      52.879  46.619  41.585  1.00 64.90           C',
    'ATOM   3339  NZ  LYS H 228      51.517  47.052  41.158  1.00 60.26           N',
    'ATOM   3340  OXT LYS H 228      57.902  49.285  43.398  1.00 70.44           O',
    'TER    3341      LYS H 228',
    'HETATM 3356  C15 OBE H 201      24.725  -3.136  27.406  1.00 27.56           C',
    'HETATM 3357  C16 OBE H 201      20.533  -2.037  27.441  1.00 16.26           C',
    'HETATM 3358  N1  OBE H 201      21.820  -2.333  26.716  1.00 21.52           N',
    'HETATM 3359  O1  OBE H 201      25.350  -3.062  24.488  1.00 23.55           O',
    'HETATM 3360  O2  OBE H 201      26.881  -1.489  24.963  1.00 21.32           O',
    'HETATM 3361  O3  OBE H 201      25.782  -3.225  27.941  1.00 19.70           O',
    'HETATM 3362  O4  OBE H 201      23.810  -4.086  27.519  1.00 23.18           O',
    'HETATM 3363  O5  OBE H 201      31.267  -3.891  23.783  1.00 37.43           O',
    'HETATM 3443  O   HOH H 229      25.710   1.134  24.699  1.00 23.08           O',
    'HETATM 3444  O   HOH H 230      26.500  -1.587  30.027  1.00 24.76           O',
    'HETATM 3445  O   HOH H 231      39.649  16.017  31.547  1.00 57.79           O'
    ]

    assert(pdb1.extract_chains(['L', 'H']) == h_l)
    assert(pdb1.extract_chains(['H']) == h)
