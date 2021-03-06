# knox-d
MI-graph (Machine learning graph)

machine learning experts, do things

## Setup: virtualenv environment
Make sure pip is up-to-date:

`python -m pip install --upgrade pip`

Install `virtualenv`:

`python -m pip install virtualenv`

### Activate environment
To create an environment run:

`python -m venv env`

to create an environment with the name "env". Now to activate the environment run the activate script based on your OS in "env/Scripts".

On windows 10 you can run:

`env/Scripts/Activate.ps1`

in your powershell, to activate the environment.

If running scripts is denied - run the following command to remove the restriction. [Stackoverflow](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system)

`set-executionpolicy remotesigned`

### Install dependencies
To install dependencies run:

`pip install -r .\requirements.txt`

If you encounter problems see [this](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

## Setup: conda environment
Install conda from [their website](https://docs.anaconda.com/anaconda/install/). (We recommend the mini version / miniconda)

Initialize the environment with:
- `conda create --name knox-env python=3.8`
- `activate knox-env`
- `pip install -r requirements.txt`
- `python -c "import nltk; nltk.download('punkt')`
- `python -m spacy download en_core_web_sm`
And you are good to go.


## Test dependencies
For developers, you also need to install the test requirements:
- `pip install -r tests/requirements.txt`

## pylint
Before you make a pull request to master, you should run branch though pylint.

you can use `pylint_runner` to run all folders in the solution, or with pylint like so
Run: 
```bash
pip install pylint
```
And then
```bash
pylint folder/
```
