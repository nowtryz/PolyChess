from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
    name='polychess',
    author='Roshan Nepaul, Pierre Szelag, Hugo Morange-Gapihan, Damien Djomby',
    url='https://github.com/nowtryz/PolyChess',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    python_requires='>=3.0',
    install_requires=[
        'numpy>=1.16.5'
    ],
    extras_require={
        'rst': ['docutils>=0.11'],
    },
    setup_requires=[
        'pytest-runner',
    ],
)
