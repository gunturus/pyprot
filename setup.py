from distutils.core import setup

setup(
    name='PyProt',
    description='Tools for Protein structure file manipulation',
    version='1.0.0',
    author='Sebastian Raschka',
    author_email='se.raschka@gmail.com',
    url='https://github.com/rasbt/pyprot',
    packages=['pyprot'],
    package_dir={'pyprot': 'pyprot'},
    license='GPLv3',
    keywords='proteins PDB MOL2',
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    long_description="""

PyProt is a Python package for working with protein structure files formats. 
It comes with a collection of ready-to-use scripts for the most common file 
operations and protein analyses.

For more details and examples please see the package documentation.

The original project is hosted and developed at: https://github.com/rasbt/pyprot

 Contact
=============

If you have any questions or comments about PyProt, please feel free to contact me via
email: se.raschka@gmail.com
or twitter: https://twitter.com/rasbt

"""
)
