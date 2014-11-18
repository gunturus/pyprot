#!/usr/bin/env python

# Sebastian Raschka 2014
#
# Python PyProt script to renumber atoms and residues in a PDB file.
#
# run
# ./pdb_renumber.py -h
# for help
#



import argparse
import pyprot


parser = argparse.ArgumentParser(
    description='Renumber residues in a pdb file',
    formatter_class=argparse.RawTextHelpFormatter
    )


parser.add_argument('-i', '--input', help='Input PDB file')
parser.add_argument('-s', '--start', help='Number of the first residue in the renumbered file (default = 1)')
parser.add_argument('-a', '--atoms' ,action='store_true', help='Renumbers atoms')
parser.add_argument('-r', '--residues', action='store_true', help='Renumbers residues')
parser.add_argument('-c', '--chainreset', action='store_true', help='Resets the residue renumbering after encountering a new chain.')

args = parser.parse_args()

if not args.input:
    print('{0}\nPlease provide an input file.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()

if not args.start:
    start = 1
else:
    start = int(args.start)

if not args.atoms and not args.residues:
    print('{0}\nPlease provide at least the --atoms or --residues flag.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()

pdb1 = pyprot.Pdb(args.input)
if args.atoms:
    pdb1.cont = pdb1.renumber_atoms(start=start)
if args.residues:
    pdb1.cont = pdb1.renumber_residues(start=start, reset=args.chainreset)

for line in pdb1.cont:
    print(line)


