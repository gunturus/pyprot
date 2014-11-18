#!/usr/bin/env python

# Sebastian Raschka 2014
# Python PyProt script that splits a multi-MOL2 file into individual mol2 files.
#
# run
# ./mol2_split.py -h
# for help
#


import sys
import os
import argparse
from pyprot.mol2io import split_multimol2



parser = argparse.ArgumentParser(
    description='Splits a multi-MOL2 file into individual mol2 files',
    formatter_class=argparse.RawTextHelpFormatter
    )

parser.add_argument('-i', '--input', type=str, help='MOL2 input file.')
parser.add_argument('-o', '--output', type=str, help='Output directory for the individual mol2 files.')


args = parser.parse_args()


if not args.input:
    print('Please provide an input file via the -i flag. Use --help for more information.\n') 
    quit()
if not args.output:
    print('Please provide an output file via the -o flag. Use --help for more information.\n') 
    quit()
    


if not os.path.exists(args.output):
    os.mkdir(args.output)

single_mol2s = split_multimol2(args.input)
for mol2 in single_mol2s:
    out_mol2 = os.path.join(args.output, mol2[0]) + '.mol2'
    with open(out_mol2, 'w') as out_file:
        for line in mol2[1]:
            out_file.write(line)



