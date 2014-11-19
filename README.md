![pyprot Logo](./images//logos/molecule_logo.png)

**PyProt is a Python package for working with protein structure files. It comes with a collection of ready-to-use scripts for the most common file operations and protein analyses.**



[[download pyprot.zip](https://github.com/rasbt/pyprot/archive/master.zip)] [[link to pyprot on GitHub](http://htmlpreview.github.io/?https://github.com/rasbt/pyprot/blob/master/README.html)]

<hr>
## ReadMe Contents
- [Scripts and command line tools](#scripts-and-command-line-tools)
- [Tutorials](#tutorials)
- [Installation](#installation)

<hr>



<br>
<br>




## Scripts and command line tools

PyProt provides ready-to-use command line scripts that are using the underlying `pyprot` objects to work with PDB and MOL2 files.  
The scripts are located in the subdirectory `./scripts` and can be used after `pyprot` was successfully installed.   

### List of command line tools

- Working with PDB files
    - [Center of Mass](./docs/tools/pdb_center_of_mass.md)
    - [Grab atoms within a radius](./docs/tools/pdb_grab_atom_radius.md)
    - [Root-mean-square deviation (RMSD)](./docs/tools/pdb_rmsd.md)
    - [PDB to FASTA converter](./docs/tools/pdb_to_fasta.md)
    - [PDB atom and residue renumbering](./docs/tools/pdb_renumber.md)
    - [B-factor statistics](./docs/tools/pdb_bfactor_stats.md)

  
- Working with MOL2 files
    - [Transfer charges](./docs/tools/mol2_transfer_charge.md)
    - [Split multi-MOL2 files](./docs/tools/mol2_split.md)
    - [MOL2 functional group filter](./docs/tools/mol2_filter_funcgroups.md)
    - [MOL2 intermolecular functional group screening](./docs/tools/mol2_screening_intermol_funcgroup.md)

<br>
<br>

## Tutorials


<br>
<br>

## Installation

PyProt was build and tested in Python 3.

The `pyprot` package can be installed like any other "normal" Python package via 
	
	pip install pyprot
	
or 

	python setup.py install
	
after downloading it from this repository. Once the pyprot package is installed, the scripts and tools from the `./scripts` subdirectory are ready to use.   
For more details, please see the separate **["Installation Documentation"](./docs/pyprot_installation.md)**