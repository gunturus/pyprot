# PyProt Scripts and Tools

<a class="mk-toclify" id="table-of-contents"></a>

###Table of Contents
- [Working with PDB files](#working-with-pdb-files)
    - [Center of Mass](#center-of-mass)
    - [Grab atoms within a radius](#grab-atoms-within-a-radius)
    - [Root-mean-square deviation (RMSD)](#root-mean-square-deviation-rmsd)
- [Working with MOL2 files](#working-with-mol2-files)
    - [Transfer charges](#transfer-charges)

<br>
<br>
<br>
<br>

<a class="mk-toclify" id="working-with-pdb-files"></a>
# Working with PDB files
[[back to top](#table-of-contents)]


<br>
<br>

<a class="mk-toclify" id="center-of-mass"></a>
## Center of Mass

[[back to top](#table-of-contents)]

Calculates the center of mass for a protein and/or ligand structure in a PDB file weighted by atom types. By default, all atoms with valid ATOM and HETATM entries in the PDB file's coordinate section are included in the center of mass calculation.

**Example:**

	./pdb_center_of_mass.py -p ./tests/data/pdbs/3EIY.pdb 
	[8.979, 41.661, 12.495]

![](../images/ex_pdb_center_of_mass.png)


(**Tip**: you can can create a pseudo-atom at a given coordinate in PyMol via  
`pseudoatom masscenter, b=40, color=red, pos=[8.979, 41.661, 12.495]`)


**Usage**

<pre>
pdb_center_of_mass.py -h
usage: pdb_center_of_mass.py [-h] [-p] [-l] PDBfile

Calculates the weighted center of mass for structures in a PDB file.
By default, all atoms in the PDB file are included in the calculation.

positional arguments:
  PDBfile

optional arguments:
  -h, --help     show this help message and exit
  -p, --protein  Center of mass for atoms in ATOM sections only
  -l, --ligand   Center of mass for atoms in HETATM sections only

Example:
pdb_center_of_mass.py ~/Desktop/3EIY.pdb -p
[8.979, 41.661, 12.495]

Note that for the center of mass calculation, the relative
atomic weights are taken into account (atomic mass unit [u]).

A list of the atomic weights can be found, e.g., at
http://en.wikipedia.org/wiki/List_of_elements
</pre>

<br>
<br>
<br>
<br>

<a class="mk-toclify" id="grab-atoms-within-a-radius"></a>

## Grab atoms within a radius

[[back to top](#table-of-contents)]

The pdb_grab_atom_radius.py script extracts atoms within a radius from a coordinate center.

**Example**  

<pre>./pdb_grab_atom_radius.py 3B7V.pdb -c 13.863,26.129,19.407 -r 7.0 -o 3B7V_rad7.pdb</pre>

![](../images/ex_grab_radius.png)


**Usage** 

run `python pdb_grab_atom_radius.py --help` for the usage information:

	usage: pdb_grab_atom_radius.py [-h] [-r int/float] [-c X,Y,Z] [-i coordinate-ID]
	                           [-o out.fasta]
	                           PDBfile

	Extracts atoms within a radius from a PDB file.
	By default, all atoms in the PDB file are included in the calculation.

	positional arguments:
	  PDBfile

	optional arguments:
	  -h, --help            show this help message and exit
	  -r int/float, --radius int/float
	                        radius in Angstrom for atoms to extract (default 10.0)
	  -c X,Y,Z, --coordinates X,Y,Z
	                        center for extracting atoms (default "0,0,0")
	  -i coordinate-ID, --include coordinate-ID
	                        Coordinate lines to include (default: "ATOM,HETATM")
	  -o out.fasta, --out out.fasta
	                        writes atoms to an output file instead of printing it to the screen

<br>
<br>
<br>
<br>

<a class="mk-toclify" id="root-mean-square-deviation-rmsd"></a>

## Root-mean-square deviation (RMSD)

[[back to top](#table-of-contents)]

The RMSD measures the average distance between atoms of 2 protein or ligand structures via the equation


![](../images/rmsd_equation.png)


where *a<sub>i</sub>* refers to the atoms of molecule 1, and *b<sub>i</sub>* to the atoms of molecule 2, respectively. The subscripts x, y, z are denoting the x-y-z coordinates for every atom.

The RMSD is most commonly calculated without taking hydrogen-atoms into consideration (typically only C-alpha or main-chain atoms in proteins).


**Example 1**  

RMSD between the alpha-carbon (main-chain) atoms of 2 closely aligned protein structures

	./pdb_rmsd.py ~/Desktop/1T48_995.pdb ~/Desktop/1T49_995.pdb -ca
	0.4785


![](../images/ex_pdb_rmsd_prot.png)


**Example 2**  

RMSD between the carbon-atoms of 2 ligand conformations.
	
	./pdb_rmsd.py ~/Desktop/lig1.pdb ~/Desktop/lig22.pdb -l -c
	1.7249


![](../images/ex_pdb_rmsd.png)

**Usage**


	./scripts/pdb_rmsd.py -h

<pre>
usage: pdb_rmsd.py [-h] [-l] [-c] [-ca] PDBfile1 PDBfile2

The RMSD measures the average distance between atoms 
of 2 protein or ligand structures.
By default, all atoms but hydrogen atoms of the protein are included in the RMSD calculation.
NOTE: Both structures must contain the same number of atoms in similar order.

positional arguments:
  PDBfile1
  PDBfile2

optional arguments:
  -h, --help     show this help message and exit
  -l, --ligand   Calculates RMSD between ligand (HETATM) atoms.
  -c, --carbon   Calculates the RMSD between carbon atoms only.
  -ca, --calpha  Calculates the RMSD between alpha-carbon atoms only.

Example:
pdb_rmsd.py ~/Desktop/pdb1.pdb ~/Desktop/pdb2.pdb
0.7377</pre>

<br>
<br>
<br>
<br>

<a class="mk-toclify" id="working-with-mol2-files"></a>
# Working with MOL2 files
[[back to top](#table-of-contents)]

<br>
<br>
<br>
<br>

<a class="mk-toclify" id="transfer-charges"></a>
## Transfer charges
[[back to top](#table-of-contents)]

Transfers partial charges from one mol2 file to another mol2 file.


![](../images/ex_mol2_transfer_charge.png)


**Example**


<pre>./mol2_transfer_charge.py ~/Desktop/mol1.mol2 ~/Desktop/mol2.mol2
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
</pre>

**Usage**

<pre>./mol2_transfer_charge.py -h
usage: mol2_transfer_charge.py [-h] [-o OUT] [-r REFERENCE_COLUMN]
                               [-t TARGET_COLUMN]
                               MOL2File1 MOL2File2

Takes a reference mol2 file as input and applies its charges
to a second mol2 file

positional arguments:
  MOL2File1
  MOL2File2

optional arguments:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     Writes output to a new mol2 file.
  -r REFERENCE_COLUMN, --reference_column REFERENCE_COLUMN
                        Position of the chargecolumn in reference molecule.
                        -1 by default for the last column.
                        E.g., -2 if charge is in the second last column.
  -t TARGET_COLUMN, --target_column TARGET_COLUMN
                        Position of the chargecolumn in the to-be-fixed molecule.
                        -1 by default for the last column.
                        E.g., -2 if charge is in the second last column.</pre>

