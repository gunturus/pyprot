PyProt makes working with protein files very convenient. It supports popular protein structure file formats such as PDB and MOL2.

# Documentation
[insert link to documentation]

[content]

# Installation

[content]

# Quickstart

[content]

# Example Application

[content]

# Scripts and Command Line Tools

I have prepared scripts using pyprot objects that allows easy usage via  
the command line from a terminal.  

## Center of Mass for Proteins and Ligands
To calculate the center of mass for a protein execute the script  
`/scripts/cmd_center_of_mass.py` from the command line.  


To calculate the center of mass of a protein, use:  
`python3 path/to/cmd_center_of_mass.py path/to/PDBfile.pdb`  
`[15.885, 7.561, 39.859]`

To calculate the center of mass of a ligand molecule, use:  
`python3 path/to/cmd_center_of_mass.py path/to/PDBfile.pdb lig`  
`[16.722, 5.369, 35.945]`




