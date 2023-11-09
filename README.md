# pdtmp: a Python Distribution TeMPlate

This repo is designed to be used as a template for any project involving more than a few scripts in Python. It combines the possibility to have a command-line interface, a distributed package on pypi (pip-installable) and a local installation, without thinking about architecture more than once, version numbers...

## How to setup ?

Copy the contents of this repo at the root of your project, and fill out the `__namespace__.py` with your informations. Change the name of `folder_containing_the_software` to something fitting your project (don't forget to change it in the `__namespace__.py` aslo), and put your python modules inside. Fill out the `folder_containing_the_software/main.py` template file to call your program!


## How to deploy?

The `justfile` handles deployment for you. Everything is automated; once you've installed [just](https://github.com/casey/just) go at the root of the project and type `just build` to create a local build of your project, or `just pypi` to upload it as a pip-installable package. For this, you will need to have `twine` znd a pypi account ready; see [this article.](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

