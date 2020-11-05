#!/usr/bin/env python3
from io import open
from glob import glob
from os.path import dirname, join
from os.path import basename, splitext
from setuptools import find_packages, setup
from sys import exit, version_info, stderr


def read_lines(*names, **kwargs):
    with open(
            join(dirname(__file__), *names),
            encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.readlines()


required_py = 3, 6
if version_info < required_py:
    print(
        "A version of python > %d.%d is required!" % required_py[:2],
        "Current version: %d.%d" % version_info[:2],
        "You may have run the wrong interpreter.",
        file=stderr, sep='\n',
    )
    exit(1)

setup(
    name='polychess',
    entry_points={
        'console_scripts': [
            'polychess = game:main',
        ],
    },
    author='Roshan Nepaul, Pierre Szelag, Hugo Morange-Gapihan, Damien Djomby',
    url='https://github.com/nowtryz/PolyChess',
    packages=find_packages('polychess'),
    package_dir={'': 'polychess'},
    py_modules=[splitext(basename(path))[0] for path in glob('polychess/*.py')],
    include_package_data=True,
    python_requires='>=%d.%d' % required_py[:2],
    install_requires=read_lines('requirements.txt'),
    setup_requires=[
        'pytest-runner',
    ],
)
