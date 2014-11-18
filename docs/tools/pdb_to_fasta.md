[[back to overview](../../README.md)]

# PDB to FASTA converter

A script that converts amino acid residues from PDB files into a FASTA string.

### Usage

Run `python pdb_to_fasta.py --help` for usage information:

<pre>
usage: pdb_to_fasta.py [-h] [-i INPUT] [-l] [-o out.fasta]

Converts amino acid residues from PDB file into a FASTA string

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input PDB file
  -l, --ligand          includes HETATM residues.
  -o out.fasta, --out out.fasta
                        writes FASTA strings to an output file instead of printing it to the screen
(py34)~/github/pyprot
</pre>

<br>
<br>

### Example

**Input:**

	python pdb_to_fasta.py -i 3B7V.pdb -o 3B7V.fasta


**Screenshot of File Output:**

![](../../images/tools/ex_pdb_to_fasta.png)

