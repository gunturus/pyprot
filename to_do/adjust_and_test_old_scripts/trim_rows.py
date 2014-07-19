# sr 05/20/2014

# Removes rows from a PDB file that do not start with a specified string.
# Default lines to keep start with 'ATOM', 'HETATM', 'TER', or 'END'
# [shell]>> python trim_rows.py in_file.pdb out.pdb [keep]
#
#   EXAMPLE: python trim_rows.py mypdb.pdb trimmed.pdb ATOM', 'HETATM'
#

import sys
import pyprot

try:
    keep = sys.argv[3].split(',')
except IndexError:
    keep = ['ATOM', 'HETATM', 'TER', 'END']

try:
    in_pdb = pyprot.Pdb(sys.argv[1])
    in_pdb.cont = in_pdb.trim_rows(keep)
    in_pdb.save_pdb(sys.argv[2])

except:
    print("ERROR\nUSAGE: python trim_rows.py in_file.pdb out.pdb [keep]")
    print("\nEXAMPLE: python trim_rows.py mypdb.pdb trimmed.pdb ATOM,HETATM,TER,END\n")
