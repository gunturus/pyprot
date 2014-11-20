<a class="mk-toclify" id="pyprot-installation"></a>
# PyProt Installation


- [Installing the `pyprot` package](#installing-the-pyprot-package)
- [Using the command line scripts](#using-the-command-line-scripts)
- Optional: [Adding the scripts to your PATH](#optional-adding-the-scripts-to-your-path)






<br>
<br>
**Note that PyProt was only tested to work with Python 3.x.**

<br>
<br>

<a class="mk-toclify" id="installing-the-pyprot-package"></a>


## Installing the `pyprot` package

[[back to top](#pyprot-installation)]

#### a) Installing pyprot via pip

If you have [pip](https://pypi.python.org/pypi/pip) installed on your system, `pyprot` can be installed via the command

	pip install pyprot

<br>

#### b) Downloading and installing pyprot from GitHub

1. Download pyprot from this GitHub repository at [https://github.com/rasbt/pyprot/archive/master.zip](https://github.com/rasbt/pyprot/archive/master.zip).
2. After unzipping the archive, `cd` into the `pyprot` directory.
3. Install `pyprot` it via the command `python setup.py install`,

<br>
<br>

<a class="mk-toclify" id="using-the-command-line-scripts"></a>

## Using the command line scripts

[[back to top](#pyprot-installation)]

Python scripts based on the `pyprot` classes for common protein file operations is provided in the subdirectory `./scripts` and can be directly be executed via Python from this directory once `pyprot` is installed. 

If  you installed `pyprot` via pip, you can download the the scripts bundle separately ([pyprot-scripts.zip](https://github.com/rasbt/pyprot/blob/master/scripts/pyprot-scripts.zip?raw=true)).

The scripts can be executed via

	python path-to-script/script-name.py

or

	./path-to-script/script-name.py

<br>
<br>

<a class="mk-toclify" id="optional-adding-the-scripts-to-your-path"></a>

## [Optional] Adding the scripts to your PATH
[[back to top](#pyprot-installation)]

Since the usage of those provided scripts is optional, they will not be automatically installed if you install `pyprot`. I recommend you to copy them to a different directory on your drive, e.g., `~/home/username/pyprot-scripts/` and add the script directory to your `PATH`.


<br>
#### Appending the script directory to PATH

E.g., if you are using a bash shell, you can add the line

	export PATH=$PATH:/home/username/pyprot_scripts/

to your `~/.bash_profile` or `~/.bashrc` file.

You can do this directly from the command line via

	echo "export PATH=$PATH:/home/username/pyprot_scripts/" >> .bash_profile


