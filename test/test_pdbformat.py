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
    assert(renumbered[100] == expect)
