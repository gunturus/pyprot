import pyprot.pdb as ppdb

pdb1 = ppdb.PdbObj("./test/test_data/3EIY.pdb")
pdb2 = ppdb.PdbObj("./test/test_data/small_3EIY.pdb")


def test_constructor():
    assert len(pdb1.cont) == 2147
    assert len(pdb1.atom) == 1330
    assert len(pdb1.hetatm) == 151
    assert len(pdb1.conect) == 54

def test_calpha():
    atom = [
    'ATOM      2  CA  SER A   2       3.259  54.783  -0.368  1.00 52.54           C',
    'ATOM      8  CA  PHE A   3       4.261  51.413   1.102  1.00 48.73           C', 
    'ATOM     19  CA  SER A   4       4.593  49.745  -2.323  1.00 47.00           C', 
    'ATOM     25  CA  ASN A   5       7.351  52.145  -3.480  1.00 41.42           C', 
    'ATOM     33  CA  VAL A   6       9.636  51.959  -0.457  1.00 32.41           C'
    ]
    assert atom == pdb2.calpha()

def test_main_chain():
    atom = [
    'ATOM      1  N   SER A   2       2.527  54.656  -1.667  1.00 52.73           N',
    'ATOM      2  CA  SER A   2       3.259  54.783  -0.368  1.00 52.54           C',
    'ATOM      3  C   SER A   2       4.127  53.553  -0.105  1.00 52.03           C', 
    'ATOM      4  O   SER A   2       5.274  53.451  -0.594  1.00 52.45           O', 
    'ATOM      7  N   PHE A   3       3.563  52.626   0.674  1.00 50.61           N', 
    'ATOM      8  CA  PHE A   3       4.261  51.413   1.102  1.00 48.73           C', 
    'ATOM      9  C   PHE A   3       4.881  50.670  -0.064  1.00 48.17           C', 
    'ATOM     10  O   PHE A   3       6.035  50.257   0.019  1.00 47.56           O', 
    'ATOM     18  N   SER A   4       4.122  50.518  -1.151  1.00 47.69           N', 
    'ATOM     19  CA  SER A   4       4.593  49.745  -2.323  1.00 47.00           C', 
    'ATOM     20  C   SER A   4       5.896  50.254  -2.977  1.00 45.29           C', 
    'ATOM     21  O   SER A   4       6.627  49.479  -3.592  1.00 45.34           O', 
    'ATOM     24  N   ASN A   5       6.184  51.544  -2.832  1.00 43.32           N', 
    'ATOM     25  CA  ASN A   5       7.351  52.145  -3.480  1.00 41.42           C', 
    'ATOM     26  C   ASN A   5       8.584  52.307  -2.574  1.00 39.00           C', 
    'ATOM     27  O   ASN A   5       9.629  52.802  -3.000  1.00 38.69           O', 
    'ATOM     32  N   VAL A   6       8.466  51.922  -1.312  1.00 35.70           N', 
    'ATOM     33  CA  VAL A   6       9.636  51.959  -0.457  1.00 32.41           C'
    ]
    
    assert atom == pdb2.main_chain()


    
    

