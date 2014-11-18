#!/usr/bin/env python

# Sebastian Raschka 2014
# Python PyProt script to convert amino acid residues from a PDB file into a FASTA string.
#
# run
# ./pdb_to_fasta.py -h
# for help
#


#############################
# Amino acid abbreviations
#############################
#
# Unusual/modified amino acids
#
# ASH (protonated ASP) = D
# CYX (disulfide-bonded CYS) = C
# GLH (protonated GLU) = E
# HID/HIE/HIP (different protonation states of HIS) = H
# HYP (hydroxyproline) = P
# MSE (selenomethionine) = M
# CSE (selenocysteine) = U
# LNT (N-((2S)-2-amino-1,1-dihydroxy-4-methylpentyl)-L-threonine)

# Ambiguous amino acids
#
# ASX (asparagine or aspartic acid) = B
# GLX (glutamine or glutamic acid = Z

import argparse
import pyprot



AMINO_ACIDS_3TO1 = {'CYS': 'C', 'ASP': 'D', 'GLN': 'Q', 'ILE': 'I',
                     'ALA': 'A', 'TYR': 'Y', 'TRP': 'W', 'HIS': 'H',
                     'LEU': 'L', 'ARG': 'R', 'VAL': 'V', 'GLU': 'E',
                     'PHE': 'F', 'GLY': 'G', 'MET': 'M', 'ASN': 'N',
                     'PRO': 'P', 'SER': 'S', 'LYS': 'K', 'THR': 'T',
                     # extended set of amino acids:
                     'MSE': 'M', 'CSE': 'U', 'LNT': 'X', 'GLH': 'E',
                     'HID': 'H', 'HIE': 'H', 'HIP': 'H', 'HYP': 'P',
                     # ambigous amino acids:
                     'ASX': 'B', 'GLX': 'Z'
                    }

AMINO_ACIDS_1TO3 = {'A': 'ALA', 'C': 'CYS', 'D': 'ASP', 'E': 'GLU',
                     'F': 'PHE', 'G': 'GLY', 'H': 'HIS', 'I': 'ILE',
                     'K': 'LYS', 'L': 'LEU', 'M': 'MET', 'N': 'ASN',
                     'P': 'PRO', 'Q': 'GLN', 'R': 'ARG', 'S': 'SER',
                     'T': 'THR', 'V': 'VAL', 'W': 'TRP', 'Y': 'TYR',
                     # extended set of amino acids:
                     'U': 'CSE', 'X': 'LNT',
                     # ambigous amino acids:
                     'B': 'ASX', 'Z': 'GLX'
                    }






parser = argparse.ArgumentParser(
    description='Converts amino acid residues from PDB file into a FASTA string',

    formatter_class=argparse.RawTextHelpFormatter
    )



parser.add_argument('-i', '--input', help='Input PDB file')
parser.add_argument('-l', '--ligand', action='store_true', help='includes HETATM residues.')
parser.add_argument('-o', '--out', metavar='out.fasta', type=str, 
        help='writes FASTA strings to an output file instead of printing it to the screen')


args = parser.parse_args()


if not args.input:
    print('Please provide an input file via the -i flag. Use --help for more information.\n') 
    quit()


in_pdb = pyprot.Pdb(args.input)

fastas = sorted(in_pdb.to_fasta(hetatm=args.ligand).items())

if args.out:
    with open(args.out, 'w') as out:
        for chain in fastas:
            out.write('>Chain {}:\n'.format(chain[0]))
            for amino_code in chain[1]:
                out.write(amino_code)
            out.write('\n')
    
else:
    for chain in fastas:
        print('>Chain {}:'.format(chain[0]))
        amino_list = []
        for amino_code in chain[1]:
            amino_list.append(amino_code)
        print("".join(amino_list))
        print('')      