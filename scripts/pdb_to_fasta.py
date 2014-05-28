# sr 01/17/2013
#
# Converts a PDB file into FASTA format.
#
# usage:
# [shell]>> USAGE: python pdb_to_fasta.py in_file.pdb out.fasta"
#

import sys
import pyprot

try:
    assert len(sys.argv) == 3

    in_pdb = pyprot.Pdb(sys.argv[1])
    fastas = sorted(in_pdb.to_fasta().items())

    with open(sys.argv[2], 'w') as out:
        for chain in fastas:
            out.write('>Chain {}:\n'.format(chain[0]))
            for amino_code in chain[1]:
                out.write(amino_code)
            out.write('\n\n')

except:
    print("ERROR\nUSAGE: python pdb_to_fasta.py in_file.pdb out.fasta")
