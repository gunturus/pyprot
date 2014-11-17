[[back to overview](../../README.md)]

# B-factor statistics


Script to calculate B-factor statistics of PDB file.


### Usage

Run `./pdb_bfactor_stats.py` for more usage information.


<pre>
pdb_bfactor_stats.py -h
usage: pdb_bfactor_stats.py [-h] [-p] [-l] [-a ATOMS] PDBfile

Calculates B-factor statistics of PDB file

positional arguments:
  PDBfile

optional arguments:
  -h, --help            show this help message and exit
  -p, --protein         includes ATOM residues.
  -l, --ligand          includes HETATM residues.
  -a ATOMS, --atoms ATOMS
                        options: all, mainchain, calpha
</pre>


### Examples

- B-factor statistics of all protein atoms

<pre>
/pdb_bfactor_stats.py ~/Desktop/1RX1.pdb --protein
Median B-factor: 14.58
Average B-factor: 19.951
Standard Deviation: 16.577
Standard Error: 0.466
Number of B-factors: 1268
</pre>


- B-factor of main-chain atoms only.
<pre>
./pdb_bfactor_stats.py ~/Desktop/1RX1.pdb --protein --atoms mainchain
Median B-factor: 12.975
Average B-factor: 15.906
Standard Deviation: 11.089
Standard Error: 0.44
Number of B-factors: 636
</pre>