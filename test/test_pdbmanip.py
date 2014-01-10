import os
import pyprot.pdb as ppdb

pdb1 = ppdb.PdbObj("./test/test_data/small_3EIY.pdb")
pdb2 = ppdb.PdbObj("./test/test_data/3EIY.pdb")

def test_pdb_save():
    dest = "./test/test_data/out/test_pdb_save.pdb"
    os.remove(dest)
    pdb1.save_pdb(dest)
    assert os.path.isfile(dest) == True

def test_grab_radius():
    res = pdb2.grab_radius(5.2, [4.698, 36.387, 11.996])
    out = [ 'ATOM    426  CE1 TYR A  56       5.834  40.653  13.201  1.00 24.86           C',
            'ATOM    428  CZ  TYR A  56       4.585  40.513  12.637  1.00 26.22           C',
            'ATOM    429  OH  TYR A  56       4.338  39.402  11.853  1.00 26.67           O',
            'ATOM    532  CB  ASP A  71       7.284  39.034   9.838  1.00 26.37           C',
            'ATOM    533  CG  ASP A  71       5.942  38.790   9.227  1.00 28.24           C',
            'ATOM    534  OD1 ASP A  71       5.331  39.745   8.677  1.00 30.97           O',
            'ATOM    535  OD2 ASP A  71       5.496  37.624   9.306  1.00 28.38           O',
            'ATOM    719  CE  MET A  96       7.289  33.359  14.839  1.00 33.43           C',
            'ATOM    765  CB  ASP A 103       5.182  31.541  10.962  1.00 39.54           C',
            'ATOM    766  CG  ASP A 103       4.926  33.029  11.126  1.00 40.16           C',
            'ATOM    767  OD1 ASP A 103       5.544  33.843  10.396  1.00 42.27           O',
            'ATOM    768  OD2 ASP A 103       4.081  33.379  11.977  1.00 38.14           O',
            'ATOM    772  O   ALA A 104       9.037  34.959   9.857  1.00 30.17           O',
            'ATOM    778  CB  LYS A 105       9.142  36.750  13.090  1.00 27.30           C',
            'ATOM    779  CG  LYS A 105       7.712  36.235  12.749  1.00 27.03           C',
            'ATOM    780  CD  LYS A 105       6.645  37.016  13.447  1.00 26.83           C',
            'ATOM    781  CE  LYS A 105       5.287  36.300  13.367  1.00 24.94           C',
            'ATOM    782  NZ  LYS A 105       4.698  36.387  11.996  1.00 23.03           N',
            'ATOM   1046  CE1 PHE A 139       4.796  37.021  16.763  1.00 26.81           C',
            'HETATM 1333 NA    NA A 177       1.633  34.181  11.897  1.00 26.73          NA',
            'HETATM 1334 NA    NA A 178       6.489  35.143   8.444  1.00 30.89          NA',
            'HETATM 1335  P1  POP A 179       1.233  37.542  11.212  1.00 32.68           P',
            'HETATM 1336  O1  POP A 179       1.910  38.831  11.612  1.00 32.62           O',
            'HETATM 1337  O2  POP A 179       1.288  37.475   9.712  1.00 33.46           O',
            'HETATM 1338  O3  POP A 179       1.948  36.362  11.841  1.00 30.47           O',
            'HETATM 1388  O   HOH A 200       2.391  38.378  14.597  1.00 23.11           O',
            'HETATM 1389  O   HOH A 201       1.535  33.854  14.371  1.00 27.83           O',
            'HETATM 1409  O   HOH A 221       3.282  37.464   7.811  1.00 36.79           O',
            'HETATM 1419  O   HOH A 231       3.976  32.286  14.525  1.00 31.56           O',
            'HETATM 1445  O   HOH A 257       2.292  33.719   9.368  1.00 44.24           O'
        ]
    assert res == out
