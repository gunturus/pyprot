#!/usr/bin/env python

# Sebastian Raschka 2014
# Python PyProt script to filter for MOL2 molecules that contain certain functional groups.
# Takes a singe-structure or multi-structure MOL2 file
# filtered query molecules that have functional groups in a specified charge range.


# run
# ./mol2_filter_funcgroups.py -h
# for help
#


import argparse
from pyprot.mol2filter import create_chargetype_list
from pyprot.mol2filter import count_matches
from pyprot.mol2filter import match_all
from pyprot.mol2io import split_multimol2

parser = argparse.ArgumentParser(
    description='Filter for MOL2 molecules that contain certain functional groups. \n'\
    'By default, all molecules that match at least 1 criterion are returned, and if \n'\
    '--matchall flag is provided, all criteria must be satified.',
    epilog='Example:\n'\
            './mol2_filter_funcgroups.py -i ./my.mol2 -c "O.2,-1.2,2;O.3,-20.0,100.0" -o ./filtered.mol2',
    formatter_class=argparse.RawTextHelpFormatter
    )

parser.add_argument('-i', '--input', type=str, help='MOL2 input file.')
parser.add_argument('-o', '--output', type=str, help='MOL2 output file for filtered results.')
parser.add_argument('-c', '--criteria', type=str, help='Query atom and charge ranges e.g., "O.2,-1.2,2;O.3,-20.0,100.0".')
parser.add_argument('-m', '--matchall', action='store_true', help='If flag is provided, molecule must satisfy all criteria.')


args = parser.parse_args()

if not args.input:
    print('Please provide a valid input file. Run ./mol2_filter_funcgroups.py -h for help.')
    quit()
if not args.output:
    print('Please provide a output file path. Run ./mol2_filter_funcgroups.py -h for help.')
    quit()
if not args.criteria:
    print('Please provide some search criteria. Run ./mol2_filter_funcgroups.py -h for help.')
    quit()    
    
clist = create_chargetype_list(group_charge_pairs=args.criteria, atom_list=None)
mmol2 = split_multimol2(multimol2=args.input)

filterfunc = count_matches
if args.matchall:
    filterfunc = match_all

with open(args.output, 'w') as out_file:
    for m in mmol2:
        res = filterfunc(mol2_cont=m[1].split('\n'), chargetype_list=clist)
        if res:
            for line in m[1]:
                out_file.write(line)
            print(m[0])