<a id='Sections'></a>

#Sections

- PDB files

	- [Center of mass calculation](#center_of_mass)

- Mol2 files


<br>
<br>

<a id='center_of_mass'></a>

##Center of mass calculation

[[back to section overview](#Sections)]

<pre>
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