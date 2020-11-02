#!/usr/bin/env bash

shopt -s globstar
cd notebooks

#command to convert all notebooks
jupyter nbconvert **/*.ipynb

exit $?
