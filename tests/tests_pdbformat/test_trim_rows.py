"""
Sebastian Raschka 2014

Unit tests for trim_rows method in PdbFormat class
from pyprot.pdbformat.
PdbFormat is a parent class of the Pdb class.

"""

import pyprot

pdb1 = pyprot.Pdb('./tests/data/pdbs/3EIY.pdb')

import pyprot

def test_trim_rows():
    pdb_out = pyprot.Pdb()
    pdb_out.cont = pdb1.trim_rows()
    for row in pdb_out.cont:
        assert(row[:6].strip() in ['ATOM', 'HETATM', 'TER', 'END']), \
                'row\n%s\nshould have been removed.'
