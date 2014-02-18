# sr 01/12/2013

# Strips PDB file from water molecules or hydrogen atoms
# [shell]>> python3 cmd_strip_protein.py in_file.pdb [h/h2o] out.pdb 
#
#   EXAMPLE: python3 cmd_strip_protein.py mypdb.pdb h2o mypdb_no_water.pdb 
#

import sys
import pyprot.pdb

try:
    assert sys.argv[2] in ["h", "h2o"]
    in_pdb = pyprot.pdb.pdbobj.PdbObj(sys.argv[1])
    
    if sys.argv[2] == "h":
        in_pdb.cont = in_pdb.strip_hydro()
    elif sys.argv[2] == "h2o":
        in_pdb.cont = in_pdb.strip_water()
    in_pdb.save_pdb(sys.argv[3])   

except:
    print("ERROR\nUSAGE: python3 cmd_strip_protein.py in_file.pdb [h/h2o] out.pdb")
    print("\nEXAMPLE: python3 cmd_strip_protein.py mypdb.pdb h2o mypdb_no_water.pdb\n")
 
