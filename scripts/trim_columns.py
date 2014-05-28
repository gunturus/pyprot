# sr 05/20/2014

# Trims a PDB file to a maximum column width, default width = 80.
# [shell]>> python trim_columns.py in_file.pdb out.pdb [width]
#
#   EXAMPLE: python columns.py mypdb.pdb trimmed.pdb 85
#

import sys
import pyprot

try:
    width = int(sys.argv[3])
except IndexError:
    width = 80

try:
    in_pdb = pyprot.Pdb(sys.argv[1])
    in_pdb.cont = in_pdb.trim_columns(width)
    in_pdb.save_pdb(sys.argv[2])

except:
    print("ERROR\nUSAGE: python columns.py in_file.pdb out.pdb [width]")
    print("\nEXAMPLE: python columns.py mypdb.pdb trimmed.pdb 85\n")
