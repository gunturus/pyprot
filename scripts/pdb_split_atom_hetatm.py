#!/usr/bin/env python

# Sebastian Raschka 2014
#
# Python PyProt script to autmatically create separate PDB files
# from ATOM and HETATM lines in a PDB file.
#
# run
# ./pdb_split_atom_hetatm.py -h
# for help
#

import argparse
import pyprot
import os

parser = argparse.ArgumentParser(
    description='Autmatically creates separate PDB files from ATOM and HETATM lines in a PDB file.',
    formatter_class=argparse.RawTextHelpFormatter
    )

parser.add_argument('-i', '--input', type=str, help='Path to directory that contains PDB files.')

args = parser.parse_args()


    
if not args.input:
    print('{0}\nPlease provide an input directory.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()    
    

atom_out = os.path.join(args.input, 'pdb_atom')
hetatm_out = os.path.join(args.input, 'pdb_hetatm')

for d in (atom_out, hetatm_out):
    if not os.path.exists(d):
        os.mkdir(d)

pdb_list = [os.path.join(args.input, pdb) for pdb in os.listdir(args.input)
            if pdb.endswith('.pdb')]



n = len(pdb_list)

if not n:
    print('{0}\nPDB list is empty. Please check the input directory for PDB files.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()    


for pdb in pdb_list:
    pdb_obj = pyprot.Pdb(pdb)
    pdb_atom = pyprot.Pdb(pdb_obj.atom_ter)
    pdb_hetatm = pyprot.Pdb(pdb_obj.hetatm)
    
    pdb_atom.save_pdb(os.path.join(atom_out, os.path.basename(pdb)))
    pdb_hetatm.save_pdb(os.path.join(hetatm_out, os.path.basename(pdb)))
