# sr 11/26/2013

# Removes all water molecules from a protein structure
# usage:
# [shell]>> python strip_water.py in_file.pdb out.pdb
#

import sys
import pyprot.pdb

try:
    assert len(sys.argv) == 3

    in_pdb = pyprot.pdb.pdbobj.PdbObj(sys.argv[1])
    out_pdb = pyprot.pdb.pdbobj.PdbObj(in_pdb.strip_water())

    in_pdb.save(sys.argv[2])


except:
    print("ERROR\nUSAGE: python strip_water.py in_file.pdb out.pdb")
