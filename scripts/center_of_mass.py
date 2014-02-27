# Sebastian Raschka 02/26/2014
# Center of Mass Calculation
#
# usage: 
# [shell]>> python3 cmd_center_of_mass.py mypdbfile.pdb [lig]
#
# If second parameter [lig] is provided, the center of mass for
# HETATM entries instead of ATOM entries will be calculated

import sys
import pyprot.pdb

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("USAGE: python3 cmd_center_of_mass.py mypdbfile.pdb [lig]")

else:
    new_pdb = pyprot.pdb.pdbobj.PdbObj(sys.argv[1])
    if len(sys.argv) == 3: 
        if sys.argv[2] == "lig":
            print(new_pdb.center_of_mass(protein = False, ligand = True))
        else:
            print("USAGE: python3 cmd_center_of_mass.py mypdbfile.pdb [lig]")
    else:
         print(new_pdb.center_of_mass())
