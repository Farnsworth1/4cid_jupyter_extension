#!/usr/bin/env python
# coding: utf-8

# Copyright (c) - Maher Albezem

# pylint: disable = C0103

"""
Packaging
"""

# inspired from
# http://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html#Example---Server-extension-and-nbextension

import os
from setuptools import setup, find_packages

NAME = "miner"
version = 0.1
INSTALL_REQUIRES = [
    'notebook>=6.0',
]

with open('miner/static/README.md') as readme:
    README = readme.read()


setup_args = dict(
    name=NAME,
    version=version,
    packages=find_packages(),
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/miner", [
            "miner/static/main.js",
        ]),
        # like `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/notebook.d", [
            "jupyter-config/nbconfig/notebook.d/miner.json"
        ])
    ],
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
