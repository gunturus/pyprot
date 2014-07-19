#!/usr/bin/env python

# Sebastian Raschka 2014
# Script that extracts atoms within a radius from a PDB file






import pyprot 
import argparse

parser = argparse.ArgumentParser(
    description='Extracts atoms within a radius from a PDB file.\n'\
                'By default, all atoms in the PDB file are included in the calculation.',
    formatter_class=argparse.RawTextHelpFormatter
    )


# positional arguments
parser.add_argument('PDBfile')
parser.add_argument('-r', '--radius',
        type=float, 
        metavar='int/float',
        default='10.0',
        help='radius in Angstrom for atoms to extract (default 10.0)')
        
parser.add_argument('-c', '--coordinates',
        type=str, 
        metavar='X,Y,Z',
        default='0,0,0',
        help='center for extracting atoms (default "0,0,0")')

# optional arguments
parser.add_argument('-i', '--include', type=str, 
        default='ATOM,HETATM', 
        metavar='coordinate-ID',
        help='Coordinate lines to include (default: "ATOM,HETATM")')
parser.add_argument('-o', '--out', metavar='out.fasta', type=str, 
            help='writes atoms to an output file instead of printing it to the screen')
             
             
args = parser.parse_args()                      
pdb = pyprot.Pdb(args.PDBfile)            



coords = args.coordinates.split(',')
coords = [float(i) for i in coords]

residues = pdb.grab_radius(args.radius, coords)    

if args.out:
    with open(args.out, 'w') as out:
        for line in residues:
            out.write(line + '\n')
            
else:
    for line in residues:
        print(line)
            



