from setuptools import setup

import pyprot

setup(
    name = "pyprot",
    version = pyprot.__version__,
    packages = ["pyprot"],
    description = "Protein file manipulation API",
    license = "GPLv3",
    author = "Sebastian Raschka",
    author_email = "bluewoodtree@gmail.com",
    url = "http://github.com/rasbt/pyprot/",
    keywords = "proteins PDB MOL2",
    #tests_require = ["unittest"]
    #install_requires = ["abc", "def"]
    #cmdclass = {"test":unittest},
    #long_description = long_description,
    #package_data = {
    #    "": ["*.txt", "*.rst"], },
    include_package_data = True,

    platforms = "any",
    #test_suite = "pyprot.test.test_pyprot",
    classifiers = [ 
        "Programming Language :: Python 3.x",
        "Development Status :: Pre-Alpha",
        "Natural Language :: English",
        "Environment :: Desktop Environment",
        "Intended Audience :: Computational Biologists",
        "License :: GPLv3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    #extras_require = {
    #    "testing": ["unittest"],
    #}
)
        
