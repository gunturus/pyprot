# Sebastian Raschka 02/26/2014
# Center of Mass Calculation
#
# usage:
# [shell]>> python center_of_mass.py my.pdb [lig]
#
# If second parameter [lig] is provided, the center of mass for
# HETATM entries instead of ATOM entries will be calculated

import sys
import pyprot

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("USAGE: python center_of_mass.py my.pdb [lig]")

else:
    new_pdb = pyprot.Pdb(sys.argv[1])
    if len(sys.argv) == 3:
        if sys.argv[2] == "lig":
            print(new_pdb.center_of_mass(protein = False, ligand = True))
        else:
            print("USAGE: python center_of_mass.py myp.pdb [lig]")
    else:
         print(new_pdb.center_of_mass())
