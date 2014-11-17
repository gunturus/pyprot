[[back to overview](../../README.md)]

# Center of Mass



Calculates the center of mass for a protein and/or ligand structure in a PDB file weighted by atom types. By default, all atoms with valid ATOM and HETATM entries in the PDB file's coordinate section are included in the center of mass calculation.




### Usage

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


### Example

	./pdb_center_of_mass.py -p ./tests/data/pdbs/3EIY.pdb 
	[8.979, 41.661, 12.495]

![](../../images/tools/ex_pdb_center_of_mass.png)


(**Tip**: you can can create a pseudo-atom at a given coordinate in PyMol via  
`pseudoatom masscenter, b=40, color=red, pos=[8.979, 41.661, 12.495]`)
