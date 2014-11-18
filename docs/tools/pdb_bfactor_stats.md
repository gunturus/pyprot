[[back to overview](../../README.md)]

# B-factor statistics


Script to calculate B-factor statistics of a PDB file.


### Usage

Run `./pdb_bfactor_stats.py` for more usage information.


<pre>
usage: pdb_bfactor_stats.py [-h] [-i INPUT] [-p] [-l] [-a ATOMS]

Calculates B-factor statistics of PDB file

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input PDB file.
  -p, --protein         includes ATOM residues.
  -l, --ligand          includes HETATM residues.
  -a ATOMS, --atoms ATOMS
                        options: all, mainchain, calpha
</pre>

<br>
<br>

### Example 1

- B-factor statistics of all protein atoms.

**Input:** 

`./pdb_bfactor_stats.py --input ~/Desktop/1RX1.pdb --protein`

**Screen Output:** 

<pre>

Median B-factor: 14.58
Average B-factor: 19.951
Standard Deviation: 16.577
Standard Error: 0.466
Number of B-factors: 1268
</pre>

<br>
<br>

### Example 2

- B-factor of main-chain atoms only.

**Input:** 
`./pdb_bfactor_stats.py --input ~/Desktop/1RX1.pdb --protein --atoms mainchain`


**Screen Output:** 

<pre>
Median B-factor: 12.975
Average B-factor: 15.906
Standard Deviation: 11.089
Standard Error: 0.44
Number of B-factors: 636
</pre>