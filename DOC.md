# Working with PDB files

### Center of Mass

Calculates the center of mass for a protein and/or ligand structure in a PDB file weighted by atom types. By default, all atoms with valid ATOM and HETATM entries in the PDB file's coordinate section are included in the center of mass calculation.

**Example:**

<pre>.pdb_center_of_mass.py -p ./tests/data/pdbs/3EIY.pdb 
[8.979, 41.661, 12.495]</pre>


![](./images/ex_pdb_center_of_mass.png)

(**Tip**: you can can create a pseudo-atom at a given coordinate in PyMol via  
`pseudoatom masscenter, b=40, color=red, pos=[8.979, 41.661, 12.495]`)


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


### Root-mean-square deviation (RMSD)

The RMSD measures the average distance between atoms of 2 protein or ligand structures via the equation

![](./images/rmsd_equation.png)

where *a<sub>i</sub>* refers to the atoms of molecule 1, and *b<sub>i</sub>* to the atoms of molecule 2, respectively. The subscripts x, y, z are denoting the x-y-z coordinates for every atom.

The RMSD is most commonly calculated without taking hydrogen-atoms into consideration (typically only C-alpha or main-chain atoms in proteins).


**Example 1**  

RMSD between the alpha-carbon (main-chain) atoms of 2 closely aligned protein structures
<pre>./pdb_rmsd.py ~/Desktop/1T48_995.pdb ~/Desktop/1T49_995.pdb -ca
0.4785</pre>

![](./images/ex_pdb_rmsd_prot.png)

**Example 2**  

RMSD between the carbon-atoms of 2 ligand conformations.
<pre>./pdb_rmsd.py ~/Desktop/lig1.pdb ~/Desktop/lig22.pdb -l -c
1.7249</pre>


![](./images/ex_pdb_rmsd.png)

<pre>
./scripts/pdb_rmsd.py -h
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
0.7377
</pre>
