[[back to overview](../../README.md)]

# Split multi-MOL2 files


The `mol2_split.py` splits a file that contains multiple MOL2 structures into individual MOL2 files where the names of the output files correspond to the name of the molecule in the input file.

### Usage

Run `./split_multimol2.py --help` for usage information:

<pre>
usage: mol2_split.py [-h] [-i INPUT] [-o OUTPUT]

Splits a multi-MOL2 file into individual mol2 files

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        MOL2 input file.
  -o OUTPUT, --output OUTPUT
                        Output directory for the individual mol2 files.
</pre>

<br>
<br>

### Example

**Input:** A file that contains multiple MOL2 structures.

	./mol2_split.py -i ~/Desktop/confs.mol2 -o ~/Desktop/my_out_dir

**File Output:** MOL2 structures split into separate files.

![](../../images/tools/ex_mol2_split.png)