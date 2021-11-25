#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio.SeqIO.FastaIO import SimpleFastaParser
#import functools
#import operator

from Bio.Seq import Seq
from Bio import SeqIO

from sklearn.decomposition import PCA
import matplotlib.pyplot as plot

# Creating a Sequence


from matplotlib import pyplot as plt

from collections import Counter

import pandas as pd
import numpy as np
import math
import seaborn as sb

 


def build_kmers(sequence, ksize): # found online - used
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers

k = 3


##try k = 3
##k = 18 onwards is useless
 

G = []
inputFasta = 'data/sample.fasta'
ffile = SeqIO.parse(inputFasta, 'fasta')
# iterate through each sequence in the fasta file
for seq_record in ffile:
    # extract just the accession number to use as ID
    id_name = str(seq_record.id)
    sequence = seq_record
    seq = sequence.seq.rstrip("N")
    covid = build_kmers(seq,k)
    G.append('{},{}'.format(id_name, covid))

 

# perform PCA analysis
df = pd.DataFrame(G)
print (df)
df.to_csv("Genome_3mer.csv")
 


