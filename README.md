PyProt makes working with protein files very convenient. It supports popular protein structure file formats such as PDB and MOL2.

# Documentation

[content]

# Installation

1. Download pyprot from [https://github.com/rasbt/pyprot/archive/master.zip](https://github.com/rasbt/pyprot/archive/master.zip)
2. Unzip the zip archive and `cd` into the `pyprot` directory
3. Execute the command `python3 setup.py install`

# Quickstart

[content]

# Examples 

[content]

# Scripts and Command Line Tools

I have prepared scripts using `pyprot` objects that allows easy usage via  
the command line from a terminal.  
The scripts are located in the subdirectory `./scripts`

<a id='script_overview'></a>
<hr>
<br>
- **[Cleaning up PDB Files](#cleanup)**  
&nbsp;&nbsp;&nbsp;&nbsp;- [Trim Rows](#trim_rows)  
&nbsp;&nbsp;&nbsp;&nbsp;- [Trim Columns](#trim_columns)  
- **[Extracting Information from PDB files](#extract)**  
&nbsp;&nbsp;&nbsp;&nbsp;- [Grab atoms within a radius from a PDB file](#grab_radius)    
- **[Calculations based on PDB files](#pdb_calc)**  
&nbsp;&nbsp;&nbsp;&nbsp;- [Center of Mass for Proteins and Ligands](#center_of_mass)   
&nbsp;&nbsp;&nbsp;&nbsp;- [Calculate Median and Mean B-Factor (temperature factor) Values](#bfactors)  
&nbsp;&nbsp;&nbsp;&nbsp;- [Calculate RMSD of proteins or ligand molecules](#rmsd)  
- **[MOL2 File Manipulations](#mol2_manip)**  
&nbsp;&nbsp;&nbsp;&nbsp;- [Swap partial charges between MOL2 files](#mol2_charge_swap)


 

<hr>
<br>
<br>
<br>
<br>
<br>
<a id='cleanup'></a>
## Cleaning up PDB files

[[back to overview](#script_overview)] 

<br>

<a id='trim_rows'></a>
#### Trim Rows
[[back to overview](#script_overview)] 

Removes rows from a PDB file that do not start with a specified string.
Default lines to keep start with 'ATOM', 'HETATM', 'TER', or 'END'

**USAGE:**

	[shell]>> python3 trim_rows.py in_file.pdb out.pdb [keep]

**EXAMPLE:** 
   
    python3 trim_rows.py mypdb.pdb trimmed.pdb ATOM', 'HETATM'



<a id='trim_columns'></a>
<br>
#### Trim Columns
[[back to overview](#script_overview)] 

Trims a PDB file to a maximum column width, default width = 80.

**USAGE:**

	[shell]>> python3 trim_columns.py in_file.pdb out.pdb [width]

**EXAMPLE:** 
	
	python3 trim_columns.py mypdb.pdb trimmed.pdb 85


<br>
<br>
<a id='extract'></a>
## Extracting Information from PDB files

[[back to overview](#script_overview)] 



<br>
<br>
<a id='grab_radius'></a>
### Grab atoms within a radius from a PDB file
[[back to overview](#script_overview)] 

Grabs atoms within specified radius from a specified x,y,z coordinates from a PDB file and writes those PDB contents to a new PDB file.

**USAGE:**
	
	[shell]>> python3 grab_radius.py in.pdb radius coordinates out.pdb

**EXAMPLE:**

	python3 grab_radius.py mypdb.pdb 5.2 4.698,36.387,11.996 mypdb_rad9.pdb


<br>
<br>
<a id='pdb_calc'></a>
## Calculations based on PDB files

[[back to overview](#script_overview)] 

<br>
<br>
<a id='center_of_mass'></a>
### Center of Mass for Proteins and Ligands
[[back to overview](#script_overview)] 

To calculate the center of mass for a protein execute the script  
`/scripts/center_of_mass.py` from the command line.  


To calculate the center of mass of a protein, use:  
<pre>python3 path/to/center_of_mass.py path/to/PDBfile.pdb  
[15.885, 7.561, 39.859]</pre>

To calculate the center of mass of a ligand molecule, use:  
<pre>python3 path/to/center_of_mass.py path/to/PDBfile.pdb lig  
[16.722, 5.369, 35.945]</pre>


<br>
<br>
<a id='bfactors'></a>
### Calculate Median and Mean B-Factor (temperature factor) Values

[[back to overview](#script_overview)] 

The examples below show how to calculate the median b-factors of a protein  
or ligand from a PDB file. The same syntax applies to calculate the 'mean'  
if `median` is substituted by `mean` in the examples shown below.   
  

To return the median B-factor value of a protein, use the script
<pre>/scripts/median_bfactor.py my_pdb.pdb
44.24</pre>

To get the median B-factor value from a ligand molecule, use:
<pre>/scripts/median_bfactor.py my_pdb.pdb lig
67.21</pre>

To get the median B-factor value from the protein's main chain atoms only, use:
<pre>/scripts/median_bfactor.py my_pdb.pdb main_chain
67.21</pre>

To get the median B-factor value from the protein's c-alpha atoms only, use:
<pre>/scripts/median_bfactor.py my_pdb.pdb calpha
67.21</pre>


<br>
<br>
<a id='rmsd'></a>
### Calculate RMSD of proteins or ligand molecules
[[back to overview](#script_overview)] 

If no optional third parameter [lig/ca] is provided, the RMSD (in Angstrom)  
between two provided protein structures in PDB format is calculated, including  
all atoms but hydrogen.  

<pre> /scripts/rmsd.py file1.pdb file2.pdb
1.99342343 </pre>

If the optional 3rd argument is 'lig', the RMSD between 2 ligand molecules is  
calculated, also excluding hydrogens. 

<pre> /scripts/rmsd.py file1.pdb file2.pdb lig
3.22334535 </pre>
 
If the If the optional 3rd argument is 'ca,' only C-alpha atoms of the two  
proteins are considered for the RMSD calculation.  

<pre> /scripts/rmsd.py file1.pdb file2.pdb ca 
0.93858464 </pre>



<br>
<br>
<a id='mol2_manip'></a>
## MOL2 file Manipulation

[[back to overview](#script_overview)] 

<br>
<br>
<a id='mol2_charge_swap'></a>
### Swap partial charges between MOL2 files
[[back to overview](#script_overview)] 

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