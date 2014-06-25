#!/usr/bin/env python

# Sebastian Raschka 2014
#
# Takes a reference mol2 file as input and applies its charges
# to a second mol2 file.
#

import argparse
import pyprot.mol2manip
import pyprot.mol2io

parser = argparse.ArgumentParser(
    description='Takes a reference mol2 file as input and applies its charges\n'\
        'to a second mol2 file',
    formatter_class=argparse.RawTextHelpFormatter
    )


parser.add_argument('MOL2File1')
parser.add_argument('MOL2File2')


parser.add_argument('-o', '--out', type=str, help='Writes output to a new mol2 file.')
parser.add_argument('-r', '--reference_column', type=int, default=-1,
        help='Position of the charge'\
        'column in reference molecule.\n-1 by '\
        'default for the last column.\nE.g., -2 if charge is in the second last column.')
parser.add_argument('-t', '--target_column', type=int, default=-1,
        help='Position of the charge'\
        'column in the to-be-fixed molecule.\n-1 by default '\
        'for the last column.\nE.g., -2 if charge is in the second last column.')


args = parser.parse_args()

# get mol2 in line list format
ref_mol2 = pyprot.mol2io.split_multimol2(args.MOL2File1)
ref_mol2 = next(ref_mol2)[1].split('\n')

fix_mol2 = pyprot.mol2io.split_multimol2(args.MOL2File2)
fix_mol2 = next(fix_mol2)[1].split('\n')



# apply the charge fix
out_cont = pyprot.mol2manip.swap_charge(
        template_mol2=ref_mol2,
        target_mol2=fix_mol2,
        template_col=args.reference_column,
        target_col=args.target_column
        )

if args.out:
    with open(args.out, 'w') as out_file:
        out_file.write('\n'.join(out_cont))
else:
    print('\n'.join(out_cont))
