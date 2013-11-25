# sr 11/25/2013
# Median B-Factor Value from PDB files
#
# usage: 
# [shell]>> python3 cmd_median_bfactor.py mypdbfile.pdb [lig]
#
# If second parameter [lig] is provided, the median for
# HETATM entries instead of ATOM entries will be returned.
#
# If second parameter [calpha] is provided, the median for
# only C-Alpha atoms of the Protein ATOM entries will be returned.

import sys
import pyprot

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("USAGE: python3 cmd_median_bfactor.py mypdbfile.pdb [lig/calpha]")

else:
    new_pdb = pyprot.PdbObj(sys.argv[1])
    if len(sys.argv) == 3: 
        if sys.argv[2] == "lig":
            print(new_pdb.median_bfactor(protein = False, ligand = True))
        elif sys.argv[2] == "calpha":
            print(new_pdb.median_bfactor(calpha = True)
        else:
            print("USAGE: python3 cmd_median_bfactor.py mypdbfile.pdb [lig/calpha]")
    else:
        print(new_pdb.median_bfactor())
