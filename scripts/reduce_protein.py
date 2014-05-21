# sr 11/26/2013

# Reduces a protein structure to main-chain or c-alpha atoms:
#    a) removes everything but main chain atoms
#    b) removes everything but only c-alpha atoms
#
# usage:
# [shell]>> python reduce_protein.py in_file.pdb [mc/ca] out.pdb
#
#   EXAMPLE: python reduce_protein.py mypdb.pdb mc mypdb_main_chain.pdb
#

import sys
import pyprot.pdb

try:
    assert sys.argv[2] in ["mc", "ca"]
    in_pdb = pyprot.pdb.pdbobj.PdbObj(sys.argv[1])

    if sys.argv[2] == "mc":
        in_pdb.cont = in_pdb.main_chain()
    elif sys.argv[2] == "ca":
        in_pdb.cont = in_pdb.calpha()
    in_pdb.save_pdb(sys.argv[3])

except:
    print("ERROR\nUSAGE: python reduce_protein.py in_file.pdb [mc/ca] out.pdb")
    print("\nEXAMPLE: python reduce_protein.py mypdb.pdb mc mypdb_main_chain.pdb\n")
