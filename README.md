PyProt makes working with protein files very convenient. It supports popular protein structure file formats such as PDB and MOL2.

# Documentation

[content]

# Installation

1. Download pyprot from [https://github.com/rasbt/pyprot/archive/master.zip]()
2. Unzip the zip archive and `cd` into the `pyprot` directory
3. Execute the command `python3 setup.py install`

# Quickstart

[content]

# Examples 

[content]

# Scripts and Command Line Tools

I have prepared scripts using pyprot objects that allows easy usage via  
the command line from a terminal.  

## Center of Mass for Proteins and Ligands
To calculate the center of mass for a protein execute the script  
`/scripts/cmd_center_of_mass.py` from the command line.  


To calculate the center of mass of a protein, use:  
<pre>python3 path/to/cmd_center_of_mass.py path/to/PDBfile.pdb  
[15.885, 7.561, 39.859]</pre>

To calculate the center of mass of a ligand molecule, use:  
<pre>python3 path/to/cmd_center_of_mass.py path/to/PDBfile.pdb lig  
[16.722, 5.369, 35.945]</pre>

## Calculate Median and Mean B-Factor (temperature factor) Values

The examples below show how to calculate the median b-factors of a protein  
or ligand from a PDB file. The same syntax applies to calculate the 'mean'  
if `median` is substituted by `mean` in the examples shown below.   
  

To return the median B-factor value of a protein, use the script
<pre>/scripts/cmd_median_bfact.py my_pdb.pdb
44.24</pre>

To get the median B-factor value from a ligand molecule, use:
<pre>/scripts/cmd_median_bfact.py my_pdb.pdb lig
67.21</pre>

To get the median B-factor value from the protein's c-alpha atoms only, use:
<pre>/scripts/cmd_median_bfact.py my_pdb.pdb calpha
67.21</pre>

 
