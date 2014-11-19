#!/usr/bin/env python

# Sebastian Raschka 2014
# Python PyProt script to compare and filter for functional group 
# distances between a reference MOL2 structure and multiple query MOL2 structures.


# run
# ./mol2_filter_funcgroups.py -h
# for help
#


import argparse
from pyprot.mol2filter import intermol_distance_match
from pyprot.mol2filter import create_chargetype_list
from pyprot.mol2io import split_multimol2


parser = argparse.ArgumentParser(
    description='Compare and filter for functional group \n'\
    'distances between a reference MOL2 structure and multiple query MOL2 structures.',
    epilog='Example:\n'\
            './mol2_screening_intermol_funcgroup.py -i1 ~/Desktop/reference.mol2 -i2 ~/Desktop/query.mol2 -o ~/Desktop/filtered.mol2 -c "O.3,-2.0,1.0;N.am,-0.8,-0.2" -d "0,2"',
    formatter_class=argparse.RawTextHelpFormatter
    )

parser.add_argument('-i1', '--input1', type=str, help='MOL2 input file of the reference molecule.')
parser.add_argument('-i2', '--input2', type=str, help='MOL2 input file of the query molecules.')
parser.add_argument('-o', '--output', type=str, help='MOL2 output file for filtered results.')
parser.add_argument('-c', '--criteria', type=str, help='Query atom and charge ranges, e.g., "O.2,-1.2,2;O.3,-20.0,100.0".')
parser.add_argument('-d', '--distance', type=str, help='Min. and max. distance allowed between functional groups, e.g., "0,10".')
parser.add_argument('-m', '--matchall', action='store_true', help='If flag is provided, molecules must satisfy all criteria.')


args = parser.parse_args()

if not args.input1:
    print('Please provide a valid input reference file. Run ./mol2_filter_funcgroups.py -h for help.')
    quit()
if not args.input2:
    print('Please provide a valid input query file. Run ./mol2_filter_funcgroups.py -h for help.')
    quit()
if not args.output:
    print('Please provide a output file path. Run ./mol2_filter_funcgroups.py -h for help.')
    quit()
if not args.criteria:
    print('Please provide some search criteria. Run ./mol2_filter_funcgroups.py -h for help.')
    quit()
if not args.distance:
    print('Please provide distance criteria. Run ./mol2_filter_funcgroups.py -h for help.')
    quit()        
    
clist = create_chargetype_list(group_charge_pairs=args.criteria, atom_list=None)

reference = split_multimol2(multimol2=args.input1)
reference = next(reference)
ref_cont = reference[1].split('\n')
ref_name = reference[0]

query = split_multimol2(multimol2=args.input2)


with open(args.output, 'w') as out_file:
    for q in query:
        res = intermol_distance_match(
                    mol2_ref=ref_cont, 
                    mol2_query=q[1].split('\n'), 
                    chargetype_list=clist,
                    distance=[0,5]
                    )

      
        print('\n{}--{} | '.format(ref_name, q[0]), end='')
        
        zeros = 0
        for v in res.values():
            print('{}x {} | '.format(v[-1], v[0]), end='')
            
            if v[-1] == 0:
                zeros += 1
        
        if (args.matchall and zeros == 0) or (not args.matchall and zeros > 0):
            for line in q[1]:
                out_file.write(line)

    print()