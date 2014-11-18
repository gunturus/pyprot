#!/usr/bin/env python

# Sebastian Raschka 2014
#
# Python PyProt script to extracts atoms within a radius from a PDB file.
#
# run
# ./pdb_grab_atom_radius.py -h
# for help
#





import pyprot 
import argparse

parser = argparse.ArgumentParser(
    description='Extracts atoms within a radius from a PDB file.\n'\
                'By default, all atoms in the PDB file are included in the calculation.',
    formatter_class=argparse.RawTextHelpFormatter
    )


# positional arguments
parser.add_argument('-i', '--input', help='Input PDB file')
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
parser.add_argument('-n', '--include', type=str, 
        default='ATOM,HETATM', 
        metavar='coordinate-ID',
        help='Coordinate lines to include (default: "ATOM,HETATM")')
parser.add_argument('-o', '--out', metavar='out.fasta', type=str, 
            help='writes atoms to an output file instead of printing it to the screen')
             
             
args = parser.parse_args()                      

if not args.input:
    print('{0}\nPlease provide an input file.\n{0}'.format(50* '-'))
    parser.print_help()
    quit()

pdb = pyprot.Pdb(args.input)            



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
            



