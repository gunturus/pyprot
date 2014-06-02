# sr 05/20/2014

# Renumbers atoms in a PDB file. Starts at atom number 1 by default.
# [shell]>> python renumber_atoms.py in_file.pdb out.pdb [start]
#
#   EXAMPLE: python renumber_atoms.py mypdb.pdb renumbered.pdb 3
#

import sys
import pyprot

try:
    start = int(sys.argv[3])
except IndexError:
    start = 1
except ValueError:
    print(sys.argv[3], 'is not an integer.')

try:
    in_pdb = pyprot.Pdb(sys.argv[1])
    in_pdb.cont = in_pdb.renumber_atoms(start)
    in_pdb.save_pdb(sys.argv[2])


except:
    print("ERROR\nUSAGE: python renumber_atoms.py in_file.pdb out.pdb [start]")
    print("\nEXAMPLE: python renumber_atoms.py mypdb.pdb renumbered.pdb 4\n")
