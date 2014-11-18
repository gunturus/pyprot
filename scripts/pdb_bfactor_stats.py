#!/usr/bin/env python

# Sebastian Raschka 2014
# Python PyProt script to calculate B-factor statistics of PDB file.
#
# run
# ./pdb_bfactor_stats.py -h
# for help
#


import argparse
import pyprot
import os

parser = argparse.ArgumentParser(
    description='Calculates B-factor statistics of PDB file',

    formatter_class=argparse.RawTextHelpFormatter
    )


parser.add_argument('-i', '--input', type=str, help='Input PDB file.')
parser.add_argument('-p', '--protein', action='store_true', help='includes ATOM residues.')
parser.add_argument('-l', '--ligand', action='store_true', help='includes HETATM residues.')
parser.add_argument('-a', '--atoms', type=str, default='all', help='options: all, mainchain, calpha')


args = parser.parse_args()

if not args.input:
    print('{0}\nPlease provide an input file.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()

if args.atoms and args.atoms not in ('all', 'mainchain', 'calpha'):
    print('Please provide a valid option for --atoms, e.g., : all, mainchain, or calpha')
    quit()
    
if not os.path.isfile(args.input):
    print('Error: File not found')
    quit()
    
if not args.protein and args.ligand and args.atoms in ('mainchain', 'calpha'):
    print('Error: Main-chain and C-alpha only exist for proteins, not ligands.')
    quit()

protein = args.protein
ligand = args.ligand
if not args.protein and not args.ligand:
    protein=True


in_pdb = pyprot.Pdb(args.input)


b_stats = in_pdb.bfactor_stats(protein=protein, ligand=ligand, atoms=args.atoms)
print('Median B-factor: %s' %round(b_stats[0], 3))
print('Average B-factor: %s' %round(b_stats[1], 3))
print('Standard Deviation: %s' %round(b_stats[2], 3))
print('Standard Error: %s' %round(b_stats[3], 3))
print('Number of B-factors: %s' %len(in_pdb.get_bfactors(protein=protein, ligand=ligand, atoms=args.atoms)))