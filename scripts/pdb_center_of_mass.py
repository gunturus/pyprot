#!/usr/bin/env python

# Sebastian Raschka 2014
#
# Python PyProt script to calculate the Center of Mass Calculation of proteins and/or ligands
# in PDB files.
#
# run
# ./pdb_center_of_mass.py -h
# for help
#

import argparse
import pyprot

parser = argparse.ArgumentParser(
    description='Calculates the weighted center of mass for structures in a PDB file.\n'\
                'By default, all atoms in the PDB file are included in the calculation.',
    epilog='Example:\n'\
            'pdb_center_of_mass.py ~/Desktop/3EIY.pdb -p\n'\
            '[8.979, 41.661, 12.495]'
            '\n\nNote that for the center of mass calculation, the relative\natomic'\
            ' weights are taken into account (atomic mass unit [u]).\n\n'\
            'A list of the atomic weights can be found, e.g., at\n'\
            'http://en.wikipedia.org/wiki/List_of_elements',
    formatter_class=argparse.RawTextHelpFormatter
    )


parser.add_argument('-i', '--input', type=str, help='Input PDB file.')
parser.add_argument('-p', '--protein', action='store_true', help='Center of mass for atoms in ATOM sections only')
parser.add_argument('-l', '--ligand', action='store_true', help='Center of mass for atoms in HETATM sections only')


args = parser.parse_args()

if not args.input:
    print('{0}\nPlease provide an input file.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()

pdb = pyprot.Pdb(args.input)


if args.ligand and not args.protein:
    print(pdb.center_of_mass(protein=False, ligand=True))

elif not args.ligand and args.protein:
    print(pdb.center_of_mass(protein=True, ligand=False))

else:
    print(pdb.center_of_mass(protein=True, ligand=True))
