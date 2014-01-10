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
        res = in_pdb.main_chain()
    elif sys.argv[2] == "ca":
        res = in_pdb.calpha()
    else:
        res = in_pdb.no_hydro()

    with open(sys.argv[3], 'w') as out_pdb:
        for line in res:
            out_pdb.write(line + '\n')

except:
    print("ERROR\nUSAGE: python3 cmd_reduce_protein.py in_file.pdb [mc/ca/no_h] out.pdb")
    print("\nEXAMPLE: python3 python3 cmd_reduce_protein.py mypdb.pdb mc mypdb_main_chain.pdb\n")
 
