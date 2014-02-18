# Sebastian Raschka 02/18/2014

# Takes a reference mol2 file as input and applies the charges
# to a second mol2 file.

import sys
import os
import pyprot.mol2

try:
    assert len(sys.argv) == 4 or len(sys.argv) == 6
    ref_mol2 = sys.argv[1]
    fix_mol2 = sys.argv[2]
    out_mol2 = sys.argv[3]    
    if len(sys.argv) == 6:
        ref_col = float(sys.argv[4])
        fix_col = float(sys.argv[5])
    else:
        ref_col = -1
        fix_col = -1

    # get mol2 in line list format
    ref_mol2 = pyprot.mol2.mol2_io.split_multimol2(ref_mol2)
    ref_mol2 = next(ref_mol2)[1].split('\n')
    fix_mol2 = pyprot.mol2.mol2_io.split_multimol2(fix_mol2)
    fix_mol2 = next(fix_mol2)[1].split('\n')
 
   
    # apply the charge fix
    out_cont = pyprot.mol2.mol2_manip.fix2ref_charge(
            ref_mol2 = ref_mol2,
            fix_mol2 = fix_mol2,
            ref_col = ref_col,
            fix_col = fix_col
            )
    with open(out_mol2, 'w') as out_file:
        out_file.write('\n'.join(out_cont))

except KeyboardInterrupt:
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

    python3 cmd_fix_mol2_to_refcharge.py myref.mol2 myfix_mol2 myout_mol2 -2 -1
 
EXAMPLE (Charge in the 2nd last column in reference mol2):

    python3 cmd_fix_mol2_to_refcharge.py myref.mol2 myfix.mol2 myout.mol2 -2 -1""")
