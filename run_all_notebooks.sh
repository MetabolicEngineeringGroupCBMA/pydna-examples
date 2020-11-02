#!/usr/bin/env bash

shopt -s globstar
cd notebooks

# command to run all notebooks
#jupyter nbconvert --ExecutePreprocessor.kernel_name=python3 --execute --inplace --allow-errors **/*.ipynb
jupyter nbconvert --ExecutePreprocessor.kernel_name=python3 --execute --inplace                **/*.ipynb
exit $?
