[[back to overview](../../README.md)]

# Split multimol2 files


The `mol2_split.py` splits a file that contains multiple MOL2 structures into individual MOL2 files where the names of the output files correspond to the name of the molecule in the input file.

### Usage

run `python ./split_multimol2.py --help` for the usage information:

<pre>
usage: mol2_split.py [-h] [-v] MOL2_FILE OUT_DIR

Splits a multi-MOL2 file into individual MOL2 files

positional arguments:
  MOL2_FILE
  OUT_DIR

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
</pre>

<br>
<br>

### Example

Input: A file that contains multiple MOL2 structures.

	python ./mol2_split.py confs.mol2 my_out_dir

Output: MOL2 structures split into separate files.

![](../../images/tools/ex_mol2_split.png)