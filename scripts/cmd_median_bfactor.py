# sr 11/25/2013
# Median B-Factor Value from PDB files
#
# usage: 
# [shell]>> python3 cmd_median_bfactor.py mypdbfile.pdb [lig/calpha/main_chain]
#
# If second parameter [lig] is provided, the median for
# HETATM entries instead of ATOM entries will be returned.
#
# If second parameter [calpha] is provided, the median for
# only C-Alpha atoms of the Protein ATOM entries will be returned.
#
# If second parameter [main_chain] is provided, the median for
# only main chain atoms (C, CA, O, N) of the Protein ATOM entries will be returned.


import sys
import pyprot.pdb

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("USAGE: python3 cmd_median_bfactor.py mypdbfile.pdb [lig/calpha/main_chain]")

else:
    new_pdb = pyprot.pdb.PdbObj(sys.argv[1])
    if len(sys.argv) == 3: 
        if sys.argv[2] == "lig":
            print(new_pdb.median_bfactor(protein = False, ligand = True))
        elif sys.argv[2] == "calpha":
            print(new_pdb.median_bfactor(main_chain = "calpha"))
        elif sys.argv[2] == "main_chain":
            print(new_pdb.median_bfactor(main_chain = "on"))
        else:
            print("USAGE: python3 cmd_median_bfactor.py mypdbfile.pdb [lig/calpha/main_chain]")
    else:
        print(new_pdb.median_bfactor())
