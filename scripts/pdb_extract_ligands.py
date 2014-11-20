#!/usr/bin/env python

# Sebastian Raschka 2014
#
# Python PyProt script to automatically extracts ligands from a PDB file
# and creates new PDB files for each ligand.
#
# run
# ./pdb_split_atom_hetatm.py -h
# for help
#

import argparse
import pyprot
import os

parser = argparse.ArgumentParser(
    description='Automatically extracts ligands from a PDB file and creates new PDB files for each ligand.',
    formatter_class=argparse.RawTextHelpFormatter
    )

parser.add_argument('-i', '--input', type=str, help='Path to directory that contains PDB files.')
parser.add_argument('-o', '--output', type=str, help='Path to target directory for ligand PDB files.')

args = parser.parse_args()


    
if not args.input:
    print('{0}\nPlease provide an input directory.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()    

if not args.output:
    print('{0}\nPlease provide an output directory.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()        


if not os.path.exists(args.output):
        os.mkdir(args.output)

pdb_list = [os.path.join(args.input, pdb) for pdb in os.listdir(args.input)
            if pdb.endswith('.pdb')]

n = len(pdb_list)

if not n:
    print('{0}\nPDB list is empty. Please check the input directory for PDB files.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()    


cnt = 1
def write_lig(lines, lig_code, pdb_name):
    global cnt
    pdb_code = os.path.basename(pdb_name).split('.pdb')[0]
    pdb_suffix = '%s_%s_%s.pdb' %(pdb_code, cnt, lig_code)
    pdb_out = os.path.join(args.output, pdb_suffix)
    with open(pdb_out, 'w') as file_out:
        for l in lines:
            file_out.write(l+'\n')
    cnt += 1

for pdb in pdb_list:
    cnt = 1
    pdb_obj = pyprot.Pdb(pdb)
    
    lig_code = ''
    lig_cont = []
    for line in pdb_obj.hetatm:
        cur_code = line[17:21].strip()
        if cur_code != lig_code:
            if lig_code:
                write_lig(lines=lig_cont, 
                       lig_code=lig_code, 
                       pdb_name=pdb)
            lig_cont = [line]
            lig_code = cur_code
        else:
            lig_cont.append(line)

