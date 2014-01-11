# sr 11/26/2013

# Reduces a protein structure to main its 
#    a) main chain atoms
#    b) c-alpha atoms
#    or
#    c) removes hydrogen atoms
#
# usage: 
# [shell]>> python3 cmd_reduce_protein.py in_file.pdb [mc/ca/no_h] out.pdb 
#
#   EXAMPLE: python3 cmd_reduce_protein.py mypdb.pdb mc mypdb_main_chain.pdb 
#

import sys
import pyprot.pdb

try:
    assert sys.argv[2] in ["mc", "ca", "no_h"]
    in_pdb = pyprot.pdb.PdbObj(sys.argv[1])
    
    if sys.argv[2] == "mc":
        in_pdb.cont = in_pdb.main_chain()
    elif sys.argv[2] == "ca":
        in_pdb.cont = in_pdb.calpha()
    else:
        in_pdb.cont = in_pdb.no_hydro()

    in_pdb.save_pdb(sys.argv[3])   

except IOError:
    print("ERROR\nUSAGE: python3 cmd_reduce_protein.py in_file.pdb [mc/ca/no_h] out.pdb")
    print("\nEXAMPLE: python3 python3 cmd_reduce_protein.py mypdb.pdb mc mypdb_main_chain.pdb\n")
 
