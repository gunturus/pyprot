#!/usr/bin/env python

# Sebastian Raschka 2014
#
# Python pyprot script to calculate the Root-mean-square deviation (RMSD) for proteins and/or ligands
# in PDB files.
#
# run
# ./pdb_rmsd.py -h
# for help
#

import argparse
import pyprot

parser = argparse.ArgumentParser(
    description='The RMSD measures the average distance between atoms \n'\
        'of 2 protein or ligand structures.\n'\
        'By default, all atoms but hydrogen atoms of the protein are included in the RMSD calculation.\n'\
        'NOTE: Both structures must contain the same number of atoms in similar order.',
    epilog='Example:\n'\
            'pdb_rmsd.py ~/Desktop/pdb1.pdb ~/Desktop/pdb2.pdb\n'\
            '0.7377',
    formatter_class=argparse.RawTextHelpFormatter
    )


parser.add_argument('PDBfile1')
parser.add_argument('PDBfile2')


parser.add_argument('-l', '--ligand', action='store_true', help='Calculates RMSD between ligand (HETATM) atoms.')
parser.add_argument('-c', '--carbon', action='store_true', help='Calculates the RMSD between carbon atoms only.')
parser.add_argument('-ca', '--calpha', action='store_true', help='Calculates the RMSD between alpha-carbon atoms only.')


args = parser.parse_args()

pdb1 = pyprot.Pdb(args.PDBfile1)
pdb2 = pyprot.Pdb(args.PDBfile2)

if args.carbon and args.calpha:
    print('\nERROR: Please provide EITHER -c OR -ca, not both.\n')
    parser.print_help()
    quit()

if args.ligand and args.carbon:
    print(pdb1.rmsd(sec_molecule=pdb2, ligand=True, atoms="c"))
elif args.ligand and args.calpha:
    print(pdb1.rmsd(sec_molecule=pdb2, ligand=True, atoms="ca"))
elif args.ligand:
    print(pdb1.rmsd(sec_molecule=pdb2, ligand=True, atoms="no_h"))
elif args.calpha:
    print(pdb1.rmsd(sec_molecule=pdb2, ligand=False, atoms="ca"))
elif args.carbon:
    print(pdb1.rmsd(sec_molecule=pdb2, ligand=False, atoms="c"))
else:
    print(pdb1.rmsd(sec_molecule=pdb2, ligand=False, atoms="no_h"))
