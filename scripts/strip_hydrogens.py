# sr 11/26/2013

# Removes all hydrogen atoms from a protein structure
# usage:
# [shell]>> python strip_hydrogens.py in_file.pdb out.pdb
#

import sys
import pyprot.pdb

try:
    assert len(sys.argv) == 3

    in_pdb = pyprot.pdb.pdbobj.PdbObj(sys.argv[1])
    out_pdb = pyprot.pdb.pdbobj.PdbObj(in_pdb.strip_h())

    in_pdb.save(sys.argv[2])


except:
    print("ERROR\nUSAGE: python strip_hydrogens.py in_file.pdb out.pdb")
