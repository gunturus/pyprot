fom setuptools import setup

import pyprot

setup(
    name = "PyProt",
    version = pyprot.__version__,
    packages = ["pyprot",],
    description = "Protein file manipulation API",
    license = "GPL v3",
    author = "Sebastian Raschka",
    author_email = "se.raschka@gmail.com",
    url = "http://github.com/rasbt/pyprot/",
    keywords = "proteins PDB MOL2",
    include_package_data = True,
    platforms = "any",
    classifiers = [ 
        "Programming Language :: Python 3.x",
        "Development Status :: Pre-Alpha",
        "Natural Language :: English",
        "Environment :: Desktop Environment",
        "Intended Audience :: Computational Biologists",
        "License :: GPLv3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
)
        
