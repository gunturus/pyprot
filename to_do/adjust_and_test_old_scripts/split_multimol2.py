# sr 01/10/2014

# Splits a multi-mol2 file into individual mol2 files.

import sys
import os
import pyprot.mol2io

try:
    assert len(sys.argv) == 3
    multimol2 = sys.argv[1]
    out_dir = sys.argv[2]

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    single_mol2s = pyprot.mol2io.split_multimol2(multimol2)
    for mol2 in single_mol2s:
        out_mol2 = os.path.join(out_dir, mol2[0]) + '.mol2'
        with open(out_mol2, 'w') as out_file:
            for line in mol2[1]:
                out_file.write(line)

except:
    print("ERROR\nUSAGE: python split_multimol2.py multi.mol2 output_directory")
