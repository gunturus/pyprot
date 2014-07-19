# sr 11/26/2013

# Removes all hydrogen atoms from a protein structure
# usage:
# [shell]>> python strip_hydrogens.py in_file.pdb out.pdb
#

import sys
import pyprot

try:
    assert len(sys.argv) == 3

    in_pdb = pyprot.Pdb(sys.argv[1])
    out_pdb = pyprot.Pdb(in_pdb.strip_h())

    in_pdb.save_pdb(sys.argv[2])


except:
    print("ERROR\nUSAGE: python strip_hydrogens.py in_file.pdb out.pdb")
