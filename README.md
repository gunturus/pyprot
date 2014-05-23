![PyProt Logo](./images/molecule_logo.png)

**PyProt is a Python package for working with protein structure files formats. It comes with a collection of ready-to-use scripts for the most common file operations and protein analyses.**

[Skip to installation and setup section](#installation)

<a id='top'></a>

<br>
<br>



<a id='scripts_and_tools'></a>
# Scripts and command line tools

An overview of the currently provided scripts that are using the underlying `pyprot` classes to work with PDB and Mol2 files The scripts are located in the subdirectory `./scripts` and can be used after `pyprot` was successfully [installed](#installation).

<a id='script_overview'></a>
<hr>
<br>






- **[Reformatting PDB files](#cleanup)**

	- [Trimming rows](#trim_rows) 	
	
	- [Trimming columns](#trim_columns)
	
	- [Removing hydrogen atoms](#strip_h)  
	
	- [Removing water atoms](#strip_water) 
	
	- [Renumbering atoms](#renumber_atoms) 
	
	- [Renumbering residues](#renumber_residues)  
	
- **[Extracting Information from PDB files](#extract)**

	- [Grabbing atoms within a radius from a PDB file](#grab_radius)
	
	- [Reducing a protein structure to its main-chain or c-alpha atoms](#reduce_protein)   
	
- **[Calculations based on PDB files](#pdb_calc)** 

	- [Calculating the center of mass for proteins and ligands](#center_of_mass)
	
	- [Calculating median and mean B-factor (temperature factor) values](#bfactors)
	
	- [Calculating RMSDs of proteins or ligand molecules](#rmsd)  
	
- **[MOL2 file Manipulations](#mol2_manip)**

	- [Swapping partial charges between MOL2 files](#mol2_charge_swap)
	
	- [Splitting a multi-MOL2 file](#split_multimol2)   
	
- **[MOL2 file filtering](#mol2_filtering)**  
	- [Filtering for intramolecular functional group distance](#intramol_distance)
	
	- [Filtering for intermolecular functional group distance](#intermol_distance)  
	
- **[File conversion](#file_conversion)**  

	- [Converting PDB files to FASTA format](#pdb_to_fasta)   

<hr>
<br>
<br>
<br>
<br>
<br>
<a id='cleanup'></a>
## Reformatting PDB files

[[back to overview](#script_overview)] 

<br>
<a id='trim_rows'></a>
#### Trimming rows
[[back to overview](#script_overview)] 

`trim_rows.py`

Removes rows from a PDB file that do not start with a specified string.
Default lines to keep start with 'ATOM', 'HETATM', 'TER', or 'END'

**USAGE:**

	[shell]>> python trim_rows.py in_file.pdb out.pdb [keep]

**EXAMPLE:** 
   
    python trim_rows.py mypdb.pdb trimmed.pdb ATOM', 'HETATM'



<a id='trim_columns'></a>
<br>
#### Trimming columns
[[back to overview](#script_overview)] 

`trim_columns.py`

Trims a PDB file to a maximum column width, default width = 80.

**USAGE:**

	[shell]>> python trim_columns.py in_file.pdb out.pdb [width]

**EXAMPLE:** 
	
	python trim_columns.py mypdb.pdb trimmed.pdb 85




<a id='strip_h'></a>
<br>
#### Removing hydrogen atoms
[[back to overview](#script_overview)] 

`strip_hydrogens.py`

Removes all hydrogen atoms from a protein structure

**USAGE:**

	python strip_hydrogens.py in_file.pdb out.pdb
	
	
<a id='strip_water'></a>
<br>
#### Removing water molecules
[[back to overview](#script_overview)] 

`strip_water.py`

Removes all water molecules from a protein structure

**USAGE:**

	python strip_water.py in_file.pdb out.pdb


<a id='renumber_atoms'></a>
<br>
#### Renumbering atoms
[[back to overview](#script_overview)] 

`renumber_atoms.py`

Renumbers atoms in a PDB file. Starts at atom number 1 by default.  

**USAGE:**  

	python renumber_atoms.py in_file.pdb out.pdb [start]
    
**EXAMPLE:**  

	python renumber_atoms.py mypdb.pdb renumbered.pdb 4



<a id='renumber_residues'></a>
<br>
#### Renumbering residues
[[back to overview](#script_overview)] 

`renumber_residues.py`

Renumbers amino acid residues in a PDB file. Starts at residue number 1 by default.

**USAGE:**  

	python renumber_residues.py in_file.pdb out.pdb [start]
    
**EXAMPLE:**  

	python renumber_residues.py mypdb.pdb renumbered.pdb 4

<br>
<br>
<a id='extract'></a>
## Extracting information from PDB files

[[back to overview](#script_overview)] 



<br>
<br>
<a id='grab_radius'></a>
### Grabbing atoms within a radius from a PDB file
[[back to overview](#script_overview)] 

`grab_radius.py`

Grabs atoms within a specified radius (in Angstrom) around a specified set of x,y,z coordinates from a PDB file and writes those PDB contents to a new PDB file.

**USAGE:**
	
	[shell]>> python grab_radius.py in.pdb radius coordinates out.pdb

**EXAMPLE:**

	python grab_radius.py mypdb.pdb 9 4.698,36.387,11.996 atoms_9A.pdb


<br>
<br>
<a id='reduce_protein'></a>
### Reducing a protein structure to main-chain or c-alpha atoms
[[back to overview](#script_overview)] 

`reduce_protein.py`

 Reduces a protein structure to main-chain or c-alpha atoms:
   a) removes everything but main chain atoms
   b) removes everything but only c-alpha atoms
 
**USAGE:**

	python reduce_protein.py in_file.pdb [mc/ca] out.pdb

**EXAMPLE:**  

	python reduce_protein.py mypdb.pdb mc mypdb_main_chain.pdb


<br>
<br>
<a id='pdb_calc'></a>
## Calculations based on PDB files

[[back to overview](#script_overview)] 

<br>
<br>
<a id='center_of_mass'></a>
### Calculating the center of mass for proteins and ligands
[[back to overview](#script_overview)] 

`center_of_mass.py`

To calculate the center of mass for a protein with or without considering ligand atoms.


To calculate the center of mass of a protein, use:  

	>> python center_of_mass.py path/to/PDBfile.pdb  
	[15.885, 7.561, 39.859]

To calculate the center of mass of a ligand molecule, use:  

	>> python center_of_mass.py path/to/PDBfile.pdb lig  
	[16.722, 5.369, 35.945]


<br>
<br>
<a id='bfactors'></a>
### Calculating median and mean B-factor (temperature factor) values

[[back to overview](#script_overview)] 

`median_bfactor.py`   
`mean_bfactor.py`

The examples below show how to calculate the median b-factors of a protein  
or ligand from a PDB file. The same syntax applies to calculate the 'mean'  
if `median` is substituted by `mean` in the examples shown below.   
  

To return the median B-factor value of a protein, use the script

	>> python median_bfactor.py my_pdb.pdb
	44.24

To get the median B-factor value from a ligand molecule, use:

	>> python median_bfactor.py my_pdb.pdb lig
	67.21

To get the median B-factor value from the protein's main chain atoms only, use:

	>> python median_bfactor.py my_pdb.pdb main_chain
	67.21

To get the median B-factor value from the protein's c-alpha atoms only, use:

	>> python median_bfactor.py my_pdb.pdb calpha
	67.21


<br>
<br>
<a id='rmsd'></a>
### Calculating RMSDs of proteins or ligand molecules
[[back to overview](#script_overview)] 

`rmsd.py`

If no optional third parameter [lig/ca] is provided, the RMSD (in Angstrom)  
between two provided protein structures in PDB format is calculated, including  
all atoms but hydrogen.  

	>> python rmsd.py file1.pdb file2.pdb
	1.99342343

If the optional 3rd argument is 'lig', the RMSD between 2 ligand molecules is  
calculated, also excluding hydrogens. 

	>> python rmsd.py file1.pdb file2.pdb lig
3.22334535
 
If the If the optional 3rd argument is 'ca,' only C-alpha atoms of the two  
proteins are considered for the RMSD calculation.  

	>> python rmsd.py file1.pdb file2.pdb ca 
	0.93858464



<br>
<br>
<a id='mol2_manip'></a>
## MOL2 file manipulation

[[back to overview](#script_overview)] 

<br>
<br>
<a id='mol2_charge_swap'></a>
### Swapping partial charges between MOL2 files
[[back to overview](#script_overview)] 

`fix_mol2_to_refcharge.py`

Takes a reference mol2 file as input and applies its charges
to a second mol2 file.

**USAGE:**

	python3 fix_mol2_to_refcharge.py ref.mol2 fix_mol2 out_mol2 ref_col fix_col



	- ref.mol2: name of the reference molecule
	- fix_mol2: target mol2 which gets the charges from the reference mol2
	- out_mol2: output mol2 with the new charges
	- ref_col: (optional) Position of the charge column in reference molecule. -1 by default for the last column. -2 if charge is in the second last column.
	- fix_col: (optional) Position of the charge column in the to-be-fixed molecule. -1 by  default for the last column. -2 if charge is in the second last column.

Note: If the charges are not in the last column of the mol2 files, arguments for both `ref_col` and `fix_col` have to be provided.

<br>
**EXAMPLE 1:** (Charge in the last column in both files):

    python3 cmd_fix_mol2_to_refcharge.py myref.mol2 myfix_mol2 myout_mol2 -2 -1

<br>


**EXAMPLE 2:** (Charge in the 2nd last column in reference mol2):

    python3 cmd_fix_mol2_to_refcharge.py myref.mol2 myfix.mol2 myout.mol2 -2 -1
    
<br>
<br>
<a id='split_multimol2'></a>
### Splitting a multi-MOL2 file
[[back to overview](#script_overview)] 

`split_multimol2.py`

Splits a multi-mol2 file into individual mol2 files.

**USAGE:**  

	python split_multimol2.py multi.mol2 output_directory

<br>
<br>
<a id='mol2_filtering'></a>
## MOL2 file filtering
[[back to overview](#script_overview)] 


<br>
<a id='intra_distance'></a>
#### Filtering for intramolecular functional group distance
[[back to overview](#script_overview)] 

`intramol_funcgroup_dist.py`

Takes a single- or multi-molecule MOL2 file and checks if
2 functional groups are within a specified distance (in Angstrom).  
Writes all molecules that match the functional group distance
criteria to a new MOL2 file.

**USAGE:**   

	python intramol_funcgroup_dist.py mol2-file.mol2 functional-groups charge-ranges distance out.mol2
	
**EXAMPLE:**   
    
	python intramol_funcgroup_dist.py my.mol2 'O.2,O.3' '-0.8,-0.5;-0.5,-0.9' '1.0' filtered.mol2



<br>
<a id='intermol_distance'></a>
#### Filtering for intermolecular functional group distance
[[back to overview](#script_overview)] 

`intermol_funcgroup_dist.py`

Checks between a single- or multi-molecule MOL2 file (query) and a reference molecule (target) and
if 2 functional groups (one in the query molecule(s) and one in the target molecule)
are within a specified distance (in Angstrom).  
Writes all molecules that match the functional group distance
criteria to a new MOL2 file.

**USAGE:**   

	python intermol_funcgroup_dist.py query.mol2 target.mol2 functional-groups charge-ranges distance out.mol2
	
**EXAMPLE:**   
    
	python intermol_funcgroup_dist.py my.mol2 myother.mol2 'O.2,O.3' '-0.8,-0.5;-0.5,-0.9' '1.0' filtered.mol2
	
	
<br>	
<br>
<a id='file_conversion'></a>
## File Conversion
[[back to overview](#script_overview)] 


<br>
<a id='pdb_to_fasta'></a>
#### Converting PDB files to FASTA format
[[back to overview](#script_overview)] 	

`pdb_to_fasta.py`

Convert a PDB file into FASTA format.

**USAGE:**  
	
	python pdb_to_fasta.py in_file.pdb out.fasta
	
	
	
	
	
	
<a id='installation'>

<br>
<br>
# Installation
[[back to top](#top)] 

<br>
<br>
**Note that PyProt was only tested to work with Python 3.x.**


#### Installing the `pyprot` package
1. Download pyprot from this GitHub repository at [https://github.com/rasbt/pyprot/archive/master.zip](https://github.com/rasbt/pyprot/archive/master.zip)
2. After unzipping the archive, `cd` into the `pyprot` directory
3. Install `pyprot` it via `python setup.py install`

#### Using the command line scripts
Python scripts based on the `pyprot` classes for common protein file operations is provided in the subdirectory `./scripts` and can be directly be executed via Python from this directory once `pyprot` is installed. For more information about the the scripts, please see the following section [Scripts and Command Line Tools](#scripts_and_tools).

#### [Optional] Adding the scripts to your PATH
Since the usage of those provided scripts is optional, they will not be automatically installed if you install `pyprot`. I recommend you to copy them to a different directory on your drive, e.g., `~/home/username/pyprot_scripts/` and add the script directory to your `PATH`.


<br>
**Step 1: Appending the script directory to PATH**   

E.g., if you are using a bash shell, you can add the line

	export PATH=:$PATH:/home/username/pyprot_scripts/

to your `~/.bash_profile` or `~/.bashrc` file

You can do this directly from the command line via

	echo "export PATH=:$PATH:/home/username/pyprot_scripts/" >> .bash_profile

<br>
**Step 2: Making the scripts executable from the command line**  

In order to call the scripts without issuing the Python command, e.g, 
	
	rmsd.py   

instead of 

	python3 ./path/to/rmsd.py
	
you have to add a python-shebang (e.g., `#!/usr/bin/python`) on top of the scripts. To do this automatically for all python script files in the current directory, you can use the shell script `prepend_python_shebang.sh`.

	sh prepend_python_shebang.sh

<br>
<br>
