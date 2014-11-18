#!/usr/bin/env python

# Sebastian Raschka 2014
#
# Python PyProt script that takes a reference MOL2 file as input and transfer its atom charges
# to a second MOL2 file.
#
# run
# ./mol2_transfer_charge.py -h
# for help
#

import argparse
from pyprot.mol2manip import swap_charge
from pyprot.mol2io import split_multimol2

parser = argparse.ArgumentParser(
    description='Takes a reference mol2 file as input and applies its charges\n'\
        'to a second mol2 file',
    formatter_class=argparse.RawTextHelpFormatter
    )


parser.add_argument('-i1', '--input1', type=str, help='Reference MOL2 file.')
parser.add_argument('-i2', '--input2', type=str, help='Target MOL2 file.')

parser.add_argument('-o', '--output', type=str, help='Writes output to a new mol2 file.')
parser.add_argument('-r', '--reference_column', type=int, default=-1,
        help='Position of the charge'\
        'column in reference molecule.\n-1 by '\
        'default for the last column.\nE.g., -2 if charge is in the second last column.')
parser.add_argument('-t', '--target_column', type=int, default=-1,
        help='Position of the charge'\
        'column in the to-be-fixed molecule.\n-1 by default '\
        'for the last column.\nE.g., -2 if charge is in the second last column.')

args = parser.parse_args()


if not args.input1:
    print('Please provide an input file via the -i1 flag. Use --help for more information.\n') 
    quit()
if not args.input2:
    print('Please provide an input file via the -i2 flag. Use --help for more information.\n') 
    quit()




# get mol2 in line list format
ref_mol2 = split_multimol2(args.input1)
ref_mol2 = next(ref_mol2)[1].split('\n')

fix_mol2 = split_multimol2(args.input2)
fix_mol2 = next(fix_mol2)[1].split('\n')



# apply the charge fix
out_cont = swap_charge(
        template_mol2=ref_mol2,
        target_mol2=fix_mol2,
        template_col=args.reference_column,
        target_col=args.target_column
        )

if args.output:
    with open(args.output, 'w') as out_file:
        out_file.write('\n'.join(out_cont))
else:
    print('\n'.join(out_cont))
