"""
Sebastian Raschka 2014

Unit tests for trim_columns method in PdbFormat class
from pyprot.pdbformat.
PdbFormat is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb("./tests/data/pdbs/short_1vr1_colfix.pdb")


def test_trim_columns():
    pdb_out = pyprot.Pdb()
    pdb_out.cont = pdb1.trim_columns()
    for row in pdb_out.cont:
        assert(len(row) <= 80), 'column\n%s\n is longer than 80 chars.' %(row)
