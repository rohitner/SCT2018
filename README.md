# SCT2018
CE31501 Term Project Group 4

By  [Dibya Prakash Das](https://github.com/dibyadas), [Rishabh Kumar](https://github.com/KumarRishabh), [Rohit Ner](https://github.com/rohitner), [Vishwajeet Kumar](https://github.com/vishwajeetkr), [Shubhika Garg](https://github.com/shubhika03)

* An abstract for the same is present [here](https://github.com/Parth-Vader/ADLAS/blob/master/ADLAS_Abstract.pdf) and the pdf version of the documentation is [here](https://github.com/Parth-Vader/ADLAS/blob/master/ADLAS_Documentation.pdf).


## Documentation

### Overview

Frontend/ contains the source code for the web application written in React. 

Backend/ contains the source code for the app server written in Python using Flask.
To program fuzzy logic, we have used the `scikit-fuzzy` package.

### Frontend Requirements

* React
* Other dependencies can be found in `package.json`

### Backend Requirements

* Python 2.7
* flask
* numpy
* scikit-fuzzy
* matplotlib

### User Guide

`cd` into `frontend/` 

run `yarn`

run `yarn start` to start the development server

`yarn build` to bundle the static files 

And in another terminal, run `python3 backend/app.py`

Add a dir `data` in backend folder and insert the data files from extrasensory website.


### The repository contains the following files:

* `app.py` contains the Flask app.

* `sct.py` contains the fuzzy logic of the application.

* `abcd.py` contains the code to handle the database.