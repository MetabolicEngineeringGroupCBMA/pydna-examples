#!/usr/bin/env python
# coding: utf-8

# # Primer screening with pydna
#
# This notebook shown how to screen a list of primers against a DNA sequence to find primers that bind the sequence.
#
# In this example, the built in primer list and ApE is used. The correct path for both ApE and the primer list has to be added to the pydna.ini file. See an example below.
#
# ![pydna_ini](pydna_ini.png)
#
# To open the config folder, call this function:

# In[8]:


from pydna import open_config_folder


# In[9]:


# NBVAL_SKIP
open_config_folder()


# if necessary, add a line like:
#
#     ape=tclsh /home/bjorn/.ApE/apeextractor/ApE.vfs/lib/app-AppMain/AppMain.tcl
#
# and:
#
#     primers=/home/bjorn/Dropbox/wikidata/Primers.txt
#
# The text file containing primer has to contain sequences in fasta or Genbank format.

# In[10]:


from pydna.readers import read


# In[11]:


dna = read("pYPKa.gb")


# In[12]:


# NBVAL_SKIP
from pydna.myprimers import PrimerList
from pydna.amplify import Anneal


# In[13]:


# NBVAL_SKIP
list_primers=PrimerList()

# In[7]:


# NBVAL_SKIP
ann = Anneal(list_primers, dna)


# In[ ]:


# NBVAL_SKIP
from pydna.editor import ape


# In[ ]:


# NBVAL_SKIP
ape(ann.template)


# The command above should open the template sequence in ape like this:
#
# ![ape](ape_primer_screen.png)
#
# Forward primers are marked in green.
# Reverse primers are maked in red.
# Only the annealing part of the primer is visible.
