# sr 05/20/2014

# Renumbers amino acid residues in a PDB file. Starts at residue number 1 by default.
# [shell]>> python renumber_residues.py in_file.pdb out.pdb [start]
#
#   EXAMPLE: python renumber_residues.py mypdb.pdb renumbered.pdb 3
#

import sys
import pyprot.pdb

try:
    start = int(sys.argv[3])
except IndexError:
    start = 1
except ValueError:
    print(sys.argv[3], 'is not an integer.')

try:
    in_pdb = pyprot.pdb.pdbobj.PdbObj(sys.argv[1])
    in_pdb.cont = in_pdb.renumber_residues(start)
    in_pdb.save_pdb(sys.argv[2])


except:
    print("ERROR\nUSAGE: python renumber_residues.py in_file.pdb out.pdb [start]")
    print("\nEXAMPLE: python renumber_residues.py mypdb.pdb renumbered.pdb 4\n")
