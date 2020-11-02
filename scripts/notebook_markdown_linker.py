#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This utility script collects all jupyter notebooks from folders and subfolders 
# in the parent folder of the current working directory and prints a list of markdown links.

from pathlib import Path

links = [f"- [{p.stem}]({p.relative_to(Path.cwd().parent)})" for p in Path.cwd().parent.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts]

for link in sorted(links):
    print(link)
