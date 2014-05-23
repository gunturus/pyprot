import pyprot.pdb as ppdb

pdb1 = ppdb.pdbobj.PdbObj("./test/test_data/pdb/short_1vr1_colfix.pdb")


def test_trim_columns():
    pdb_out = ppdb.pdbobj.PdbObj()
    pdb_out.cont = pdb1.trim_columns()
    for row in pdb_out.cont:
        assert(len(row) <= 80)

def test_trim_rows():
    pdb_out = ppdb.pdbobj.PdbObj()
    pdb_out.cont = pdb1.trim_rows()
    for row in pdb_out.cont:
        assert(row[:6].strip() in ['ATOM', 'HETATM', 'TER', 'END'])

def test_renumber_atoms():
    renumbered = pdb1.renumber_atoms(start=4)
    expect = 'ATOM     91  CA  LYS L  10      -3.668  17.825  17.723  1.00 34.32           C'
    assert(renumbered[100] == expect), '\nexpect:\n%s\ngot:\n%s' %(expect, renumbered[100])

def test_renumber_residues():
    renumbered = pdb1.renumber_residues(start=2)
    expect1 =  'ATOM     14  N   CYS L   4      10.930  16.366  19.574  1.00 28.95           N'
    expect2 =  'ATOM    127  N   LYS L  18      -5.816   5.075  21.742  1.00 28.96           N'
    assert(renumbered[26] == expect1),  '\nexpect:\n%s\ngot:\n%s' %(expect1, renumbered[26])
    assert(renumbered[139] == expect2), '\nexpect:\n%s\ngot:\n%s' %(expect2, renumbered[139])
