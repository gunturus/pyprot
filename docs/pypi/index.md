![pyprot Logo](https://raw.githubusercontent.com/rasbt/pyprot/master/images/logos/molecule_logo.png)

**PyProt is a Python package for working with protein structure files formats. It comes with a collection of ready-to-use scripts for the most common file operations and protein analyses.**


For more details, please visit PyProt on [GitHub](https://github.com/rasbt/pyprot).

<hr>
## ReadMe Contents
- [Scripts and command line tools](#scripts-and-command-line-tools)
- [Installation](#installation)

<hr>



<br>
<br>




## Scripts and command line tools

pyprot provides ready-to-use command line scripts that are using the underlying `pyprot` objects to work with PDB and Mol2 files.  
The scripts are located in the subdirectory `./scripts` and can be used after `pyprot` was successfully installed.   

### List of command line tools

- Working with PDB files
    - Center of Mass
    - Grab atoms within a radius
    - Root-mean-square deviation (RMSD)
    - PDB to FASTA conversion
    - PDB atom and residue renumbering
    - B-factor statistics
  
- Working with MOL2 files
    - Transfer charges
    - Split multimol2 files



<br>
<br>

## Installation

The pyprot package can be installed like any other "normal" Python package via 
	
	pip install pyprot
	
or 

	python setup.py install
	
after downloading it from this repository. Once the pyprot package is installed, the scripts and tools from the `./scripts` subdirectory are ready to use.   
For more details, please see the separate **["Installation Documentation"]([./docs/pyprot_installation.md](https://github.com/rasbt/pyprot/blob/master/docs/pyprot_installation.md))**