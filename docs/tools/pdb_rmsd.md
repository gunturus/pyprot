[[back to overview](../../README.md)]

# Root-mean-square deviation (RMSD)

The RMSD measures the average distance between atoms of 2 protein or ligand structures via the equation


![](../../images/equations/rmsd_equation.png)


where *a<sub>i</sub>* refers to the atoms of molecule 1, and *b<sub>i</sub>* to the atoms of molecule 2, respectively. The subscripts x, y, z are denoting the x-y-z coordinates for every atom.

The RMSD is most commonly calculated without taking hydrogen-atoms into consideration (typically only C-alpha or main-chain atoms in proteins).

### Usage


Run	`./scripts/pdb_rmsd.py -h` for usage information:

<br>

<pre>
usage: pdb_rmsd.py [-h] [-r REFERENCE] [-t TARGET] [-l] [-c] [-ca]

The RMSD measures the average distance between atoms 
of 2 protein or ligand structures.
By default, all atoms but hydrogen atoms of the protein are included in the RMSD calculation.
NOTE: Both structures must contain the same number of atoms in similar order.

optional arguments:
  -h, --help            show this help message and exit
  -r REFERENCE, --reference REFERENCE
                        Reference PDB file.
  -t TARGET, --target TARGET
                        Target PDB file.
  -l, --ligand          Calculates RMSD between ligand (HETATM) atoms.
  -c, --carbon          Calculates the RMSD between carbon atoms only.
  -ca, --calpha         Calculates the RMSD between alpha-carbon atoms only.

Example:
pdb_rmsd.py -r ~/Desktop/pdb1.pdb -t ~/Desktop/pdb2.pdb
0.7377
</pre>

<br>
<br>

### Example 1 - RMSD between proteins

RMSD between the alpha-carbon (main-chain) atoms of 2 closely aligned protein structures

**Input:** 

	./pdb_rmsd.py -r ~/Desktop/1T48_995.pdb -t ~/Desktop/1T49_995.pdb -ca

**Screen Output:** 

	0.4785

**PyMOL Visualization:** 


![](../../images/tools/ex_pdb_rmsd_prot.png)


<br>
<br>

### Example 2 - RMSD between small ligand molecules

RMSD between the carbon-atoms of 2 ligand conformations.

**Input:** 
	
	./pdb_rmsd.py -r ~/Desktop/lig1.pdb -t ~/Desktop/lig22.pdb -l -c

**Screen Output:** 

	1.7249

**PyMOL Visualization:** 

![](../../images/tools/ex_pdb_rmsd.png)

