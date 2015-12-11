# Datascience Bootcamp

## Objective
Build solid foundation in Python for use in data science.

## Instructor
- name: Henry Xie
- email: henrysxie@gmail.com
- website: [simplefractal.com](http://simplefractal.com)

## Agenda with Objectives
- [Day 1](https://github.com/henrysxie/datascience-bootcamp-part-one/blob/master/day_1.md)
- [Day 2](https://github.com/henrysxie/datascience-bootcamp-part-one/blob/master/day_2.md)

## What do you need?
- Terminal for Mac users, Command Prompt for Windows users
- Python 2.7+ (Run `python --version` in your Terminal or Command Prompt to see what you have installed)
- Anacondas (see setup instructions below)

## Install Anaconda
- This is a package of Python libraries you need to do Data Science
- Install Anaconda with python 2.7
- Instructions for [Mac](http://docs.continuum.io/anaconda/install.html#mac-install)
- Instructions for [Windows](http://docs.continuum.io/anaconda/install.html#windows-install)
- Open a NEW terminal window and setup your environment using the `conda` command line tool:
```bash
conda create --name datascience-bootcamp pandas matplotlib ipython ipython-notebook
source activate datascience-bootcamp
ipython -pylab
>>> import pandas
```