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
import pyprot



parser = argparse.ArgumentParser(
    description='Splits a multi-MOL2 file into individual mol2 files',
    formatter_class=argparse.RawTextHelpFormatter
    )

parser.add_argument('MOL2_FILE')
parser.add_argument('OUT_DIR')
parser.add_argument('-v', '--version', action='version', version='mol2_split.py v. 1.0')

args = parser.parse_args()

if not os.path.exists(args.OUT_DIR):
    os.mkdir(args.OUT_DIR)

single_mol2s = split_multimol2(args.MOL2_FILE)
for mol2 in single_mol2s:
    out_mol2 = os.path.join(out_dir, mol2[0]) + '.mol2'
    with open(out_mol2, 'w') as out_file:
        for line in mol2[1]:
            out_file.write(line)



