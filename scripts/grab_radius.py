# sr 01/09/2013
# Grab atoms within a radius from a PDB file
#
# usage:
# [shell]>> python grab_radius.py in.pdb radius coordinates out.pdb
#
# Grabs atoms within a specified radius from specified x,y,z coordinates from
# a pdb file and writes those PDB contents to a new pdb file.
#

import sys
import pyprot.pdb

try:
    pdb_in = pyprot.pdb.pdbobj.PdbObj(sys.argv[1])
    radius = float(sys.argv[2])
    coordinates = (sys.argv[3]).split(',')
    pdb_out = sys.argv[4]

    res = pdb_in.grab_radius(radius, [float(i) for i in coordinates])
    with open(pdb_out, 'w') as out_file:
        for line in res:
            out_file.write(line + '\n')

except:
    print("ERROR\nUSAGE: python grab_radius.py in.pdb radius coordinates out.pdb")
    print("\nEXAMPLE: python grab_radius.py mypdb.pdb 5.2 4.698,36.387,11.996 mypdb_rad9.pdb\n")
