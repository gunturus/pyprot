#!/usr/bin/env python

# Sebastian Raschka 2014
#
# Python PyProt script to autmatically download PDB files.
# from the Protein Data Bank (rcsb.org).
#
# run
# ./pdb_download.py -h
# for help
#

import argparse
import pyprot
import os
import pyprind

parser = argparse.ArgumentParser(
    description='Autmatically downloads PDB files from the Protein Data Bank (rcsb.org).',
    epilog='The input file should contain 1 4-letter PDB code per line. E.g.,\n'\
            '3EIY\n1HTG\n1RX1\n[...]',
    formatter_class=argparse.RawTextHelpFormatter
    )


parser.add_argument('-i', '--input', type=str, help='Path to a text file with PDB codes.')
parser.add_argument('-o', '--output', type=str, help='Path of an output directory')



args = parser.parse_args()


    
if not args.input:
    print('{0}\nPlease provide an input text file.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()    
    
if not args.output:
    print('{0}\nPlease provide a name for the output directory.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()

if not os.path.exists(args.output):
    os.mkdir(args.output)

pdb_list = []
with open(args.input, 'r') as infile:
    for line in infile:
        line = line.strip().lower()
        if len(line) == 4:
            pdb_list.append(line)

n = len(pdb_list)

if not n:
    print('{0}\nPDB list is empty. Please check the format of the input file.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()    

pbar = pyprind.ProgBar(n)

for pdb in pdb_list:
    pdb_obj = pyprot.Pdb()
    pdb_obj.cont = pdb_obj.fetch_rcsb(pdb_code=pdb)
    pdb_obj.save_pdb(os.path.join(args.output, pdb)+'.pdb')
    pbar.update()
