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
