#!/usr/bin/env python
# coding: utf-8

# Copyright (c) - Maher Albezem

"""
Packaging
"""

# inspired from
# http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html#Example---Server-extension-and-nbextension

import os
from setuptools import setup, find_packages

NAME = "miner"

INSTALL_REQUIRES = [
    'notebook>=6.0',
]

with open('README.md') as readme:
    README = readme.read()

# Enable the nbextension (like jupyter nbextension enable --sys-prefix)
DATA_FILES = [
    ("etc/jupyter/nbconfig/notebook.d", [
        "jupyter-config/nbconfig/notebook.d/miner.json"
    ]),
]

# Install the nbextension (like jupyter nbextension install --sys-prefix).
# More precisely, everything in the miner/static directory and its
# subdirectories should be installed
nbext = ["share", "jupyter", "nbextensions", NAME]
for (path, dirs, files) in os.walk(os.path.join("miner", "static")):
    # Files to install
    srcfiles = [os.path.join(path, f) for f in files]
    # Installation path components, removing miner/static from "path"
    dst = nbext + path.split(os.sep)[2:]
    DATA_FILES.append((os.path.join(*dst), srcfiles))

setup_args = dict(
    name=NAME,
    version=1.0,
    packages=find_packages(),
    data_files=DATA_FILES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    description="Adds and runs a default cell at the top of each new notebook.",
    long_description=README,
    long_description_content_type='text/markdown',
    author="Maher Albezem",
    author_email="maher.albezem@alumni.fh-aachen.de",
    project_urls={
        'source': "https://github.com/ceedee666/python_introduction"
    },
    platforms="Linux, Mac OS X, Windows",
    keywords=["jupyter", "ipython", "execute_time", "miner"],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
)

if __name__ == '__main__':
    setup(**setup_args)
