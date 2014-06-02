# sr 11/25/2013
# Mean B-Factor Value from PDB files
#
# usage:
# [shell]>> python mean_bfactor.py mypdbfile.pdb [lig/calpha/main_chain]
#
# If second parameter [lig] is provided, the mean for
# HETATM entries instead of ATOM entries will be returned.
#
# If second parameter [calpha] is provided, the mean for
# only C-Alpha atoms of the Protein ATOM entries will be returned.
#
# If second parameter [main_chain] is provided, the mean for
# only main chain atoms (C, CA, O, N) of the Protein ATOM entries will be returned.


import sys
import pyprot

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("USAGE: python mean_bfactor.py mypdbfile.pdb [lig/calpha/main_chain]")

else:
    new_pdb = pyprot.Pdb(sys.argv[1])
    if len(sys.argv) == 3:
        if sys.argv[2] == "lig":
            print(new_pdb.mean_bfactor(protein = False, ligand = True))
        elif sys.argv[2] == "main_chain":
            print(new_pdb.mean_bfactor(main_chain = "on"))
        elif sys.argv[2] == "calpha":
            print(new_pdb.mean_bfactor(main_chain = "calpha"))
        else:
            print("USAGE: python mean_bfactor.py mypdbfile.pdb [lig/calpha/main_chain]")
    else:
        print(new_pdb.mean_bfactor())
