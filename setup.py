from distutils.core import setup

import pyprot

setup(
    name = 'PyProt',
    version = '1.0.0',
    packages = ['pyprot',],
    description = 'Protein structure file manipulation API',
    license = 'GPLv3',
    author = 'Sebastian Raschka',
    author_email = 'se.raschka@gmail.com',
    url = 'http://github.com/rasbt/pyprot/',
    keywords = 'proteins PDB MOL2',
    tests_require=['nose'],
    install_requires=['pystats>=0.0.1'],
    requires=['optparse',]
    data_files = [('', ['LICENSE.txt']),
                    ('', ['README.md']),
                    ('', ['README.html']),
                    ('', ['CHANGELOG.txt']),
                    ('scripts', ['scripts/center_of_mass.py']),
                    ('scripts', ['scripts/fix_mol2_to_refcharge.py']),
                    ('scripts', ['scripts/get_chains.py']),
                    ('scripts', ['scripts/grab_radius.py']),
                    ('scripts', ['scripts/intermol_funcgroup_dist.py']),
                    ('scripts', ['scripts/intramol_funcgroup_dist.py']),
                    ('scripts', ['scripts/median_bfactor.py']),
                    ('scripts', ['scripts/pdb_to_fasta.py']),
                    ('scripts', ['scripts/rmsd.py']),
                    ('scripts', ['scripts/split_multimol2.py']),
                    ('scripts', ['scripts/strip_protein.py']),
                   ],
    include_package_data = True,
    platforms='any',
    classifiers = [ 
        'Programming Language :: Python 3.x',
        'Development Status :: Stable',
        'Natural Language :: English',
        'Environment :: Desktop Environment',
        'Intended Audience :: Computational Biologists',
        'License :: GPLv3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
        
