from distutils.core import setup

setup(
    name = 'PyProt',
    description = 'Tools for Protein structure file manipulation',
    version = '1.1.0',
    author='Sebastian Raschka',
    author_email='se.raschka@gmail.com',
    url='https://github.com/rasbt/pyprot',
    packages=['pyprot'],

    license = 'GPLv3',
    keywords = 'proteins PDB MOL2',
    tests_require=['nose'],
    data_files = [('', ['LICENSE.txt']),
                    ('', ['README.md']),
                    ('', ['README.html']),
                    ('', ['CHANGELOG.txt']),
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
    long_description="""

The PyPrind (Python Progress Indicator) module provides a progress bar and a percentage indicator
object that let you track the progress of a loop structure or other iterative computation.
Typical applications include the processing of large data sets to provide an intuitive estimate
at runtime about the progress of the computation.

For more details and examples please see the package documentation.


 Contact
=============

If you have any questions or comments about PyPrind, please feel free to contact me via
eMail: se.raschka@gmail.com
or Twitter: https://twitter.com/rasbt

""",
    )
