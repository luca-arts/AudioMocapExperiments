# template_title

Project page for research project template_title by researcher

## Introduction

### Research questions

1. xxxx
2. xxxx

## folder structure

In notebooks, per topic there's a directory with notebooks to evaluate different approaches. In the accompanying markdown file we note down the expected result and findings.


## get started

We have two approaches: working locally or working via cloud (e.g. google colab)

1. Open a terminal and go to the git directory
2. If running locally: 
    1. Create the environment via `python setup.py --env`
    2. Activate the conda environment `conda activate <given environment name>`
3. Next adapt the README.md file by running `python setup.py --project "<your project name>" "<your name>"`


Now we have a basic repo setup which you can push to your newly created git repo.

If you want to start experimenting with a topic, you need to create a folder for this topic, e.g. you want to experiment with "image classification", then you enter the following:

`python setup.py --topic "image_classification"`

This will create the folder with all names correct already.

The idea is that you experiment first in the [playground](./notebooks/template/playground) by saving notebooks you've created locally or via Google Colab first here.
In the [topic](./notebooks/template/) folder directly you have one notebook in which you list the succesful experiments.


## Google Colab flow

How do we integrate google colab and git swiftly.

<!-- TODO add flow -->