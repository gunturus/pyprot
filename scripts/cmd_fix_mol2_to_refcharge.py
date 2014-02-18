# Sebastian Raschka 02/18/2014

# Takes a reference mol2 file as input and applies the charges
# to a second mol2 file.

import sys
import os
import pyprot.mol2

try:
    assert len(sys.argv) == 3
    multimol2 = sys.argv[1]
    out_dir = sys.argv[2]
    
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    
    single_mol2s = pyprot.mol2.mol2_io.split_multimol2(multimol2, generator=True)
    for mol2 in single_mol2s:
        out_mol2 = os.path.join(out_dir, mol2[0]) + '.mol2'
        with open(out_mol2, 'w') as out_file:
            for line in mol2[1]:
                out_file.write(line)

except:
    print("ERROR\nUSAGE: python3 ref.mol2 fix_mol2 out_mol2 ref_col fix_col\n")
    print("""ref.mol2: name of the reference molecule
fix_mol2: target mol2 which gets the charges from the reference mol2
out_mol2: output mol2 with the new charges
ref_col: (optional) Position of the charge column in reference molecule. -1 by
         default for the last column. -2 if charge is in the second last column.
fix_col: (optional) Position of the charge column in the to-be-fixed molecule. -1 by
         default for the last column. -2 if charge is in the second last column.

Note: If the charges are not in the last column of the mol2 files, arguments for both
     ref_col and fix_col have to be provided.

EXAMPLE (Charge in the last column in both files):

    python3 myref.mol2 myfix_mol2 myout_mol2 -2 -1
 
EXAMPLE (Charge in the 2nd last column in reference mol2):

    python3 myref.mol2 myfix_mol2 myout_mol2 -2 -1"""
 
