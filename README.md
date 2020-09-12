# 4cid_jupyter_extension
This project aims to create and develop a jupyter notebook extension that helps students with their exercises in lectures in `Python Introduction` (See https://github.com/ceedee666/python_introduction)

Miner is a Jupyter Extension that suggests the next appropriate task level and task Group based on certain criteria.
User data, ex. number of runs, is "collected" and saved as metadata in the notebook.

I took the jupyter extension execution time will be modifying it.

**Concept Requirements**:
1. Each notebook contains only one exercise. The cell for this exercise is identified. The exercise cell is the 3rd cell.
2. Users data is collected and stored locally for each user of exercises notebooks. I.e. decentralized.

The following criteria are considered for the selection of the next level:
1. The number of executions of the exercise cell until success. How often the student tries his solution is determining for his fitness in programming.
1. Other suggestions for further criteria are welcome. 

# Contributing

## Extensions
Jupyter Notebook Extensions are simple add-ons which can significantly improve your productivity in the notebook environment.
They automate tedious tasks such as formatting code or add features like creating a table of contents.
While there are numerous existing extensions, we can also write our own extension to do extend the functionality of Jupyter.

### Steps to modify/activate extensions

1. run the following code in a command prompt to activate nbExtensions:
`pip install jupyter_contrib_nbextensions && jupyter contrib nbextensions install`
All extensions will be then found inside you environment. For example in windows Anacondas environment all nbextensions will be found
in ``C:\Users\User\anaconda3\envs\env\Lib\site-packages\jupyter_contrib_nbextensions``, Where `env` is the environment name.

1. to install the package run pip install setup.py inside project root directory.

1. alternatively you want to install run the following two commands to activate the extension manually
    ``jupyter nbextension install <extension_name> --sys-prefix`` 
    
    ``jupyter nbextension enable <extension_name> --sys-prefix``
    
     for example if you want to install ``miner`` run the following two commands inside the directory `extensions\ext_default_cell`:
    
    ``jupyter nbextension install miner --sys-prefix`` 
    
    ``jupyter nbextension enable miner --sys-prefix``

1. When you make a change to the extension files while developing and you want to see the effects in 
a Jupyter Notebook,you need to run the commands in the previous step
1. In your jupyter server page you can also activate/deactivate each extension under the tab ``Nbextensions``
1. alternatively you can disable and remove an extension with the following commands:
 
    disable a package with:
    ``jupyter nbextension disable <extension_name> --py --sys-prefix``
    
    If you want to remove it from your environment:
    ``jupyter nbextension uninstall <extension_name> --py --sys-prefix``
    
    Alternatively, you can also remove it with pip (if you already installed it as a package):
    ``pip uninstall <extension_name>``

### Structure of a Jupyter Notebook Extension
There are 3 parts (at minimum) to any Jupyter Notebook extension:
1. ``description.yaml`` : A configuration file read by Jupyter
1. ``main.js`` : The Javascript code for the extension itself
1. ``README.md`` : A markdown description of extension

### Project structure

Jupyter extensions can be distributed as packages as shown in [here](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html#Example---Server-extension-and-nbextension)
So ex. the package structure of ``miner`` extension looks like this:

│   .gitignore
│   MANIFEST.in
│   README.md
│   requirements.txt
│   setup.py
│
├───miner
│   │   __init__.py
│   │
│   └───static
│           description.yml
│           main.js
│           README.md
│
└───jupyter-config
    └───nbconfig
        └───notebook.d
                miner.json



