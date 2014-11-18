[[back to overview](../../README.md)]

# Transfer charges

Transfers partial charges from one mol2 file to another mol2 file.


![](../../images/tools/ex_mol2_transfer_charge.png)


### Usage

Run `./mol2_transfer_charge.py` -h for usage information:

<br>	

<pre>	
usage: mol2_transfer_charge.py [-h] [-i1 INPUT1] [-i2 INPUT2] [-o OUTPUT]
                               [-r REFERENCE_COLUMN] [-t TARGET_COLUMN]

Takes a reference mol2 file as input and applies its charges
to a second mol2 file

optional arguments:
  -h, --help            show this help message and exit
  -i1 INPUT1, --input1 INPUT1
                        Reference MOL2 file.
  -i2 INPUT2, --input2 INPUT2
                        Target MOL2 file.
  -o OUTPUT, --output OUTPUT
                        Writes output to a new mol2 file.
  -r REFERENCE_COLUMN, --reference_column REFERENCE_COLUMN
                        Position of the chargecolumn in reference molecule.
                        -1 by default for the last column.
                        E.g., -2 if charge is in the second last column.
  -t TARGET_COLUMN, --target_column TARGET_COLUMN
                        Position of the chargecolumn in the to-be-fixed molecule.
                        -1 by default for the last column.
                        E.g., -2 if charge is in the second last column.
</pre>


### Example

**Input:**

	./mol2_transfer_charge.py -i1 ~/Desktop/mol1.mol2 -i2 ~/Desktop/mol2.mol2

**Screen Output:**

	
	@<TRIPOS>MOLECULE
	mol2_file2
	   9    9     0     0     0
	SMALL
	USER_CHARGES  
	mmff94s_NoEstat = 44.88
	@<TRIPOS>ATOM
	      1 C1         -5.0187   -7.8208   -3.4745 C.ar      1 <0>        -0.0736
	      2 C2         -7.1625   -6.7138   -3.3495 C.ar      1 <0>        -0.0770
	      3 C3         -5.5821   -8.8226   -4.2649 C.ar      1 <0>        -0.1229
	      4 C4         -7.7259   -7.7155   -4.1400 C.ar      1 <0>        -0.1228
	...

