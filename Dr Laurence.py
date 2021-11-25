#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import product
from Bio import SeqIO
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plot
import numpy as np


# create all possible kmers
def createKmers(string, k):
    kmers = [''.join(c) for c in product(string, repeat=k)]
    return(kmers)

# count kmers in string
def countKmers(string, kmers):
    kcount = list()
    for k in kmers:
        kcount = kcount + [string.count(k)]
    return(kcount)

# normalize kmer counts by total number of kmers
def normKmers(kdict):
    norm = dict()
    for key in kdict.keys():
        l = list()
        for i in kdict[key]:
            l = l + [i/sum(kdict[key])]
        norm[key] = l
    return(norm)

# create all possible kmers for a given length of k
k = 7
kmers = createKmers('ACGT', k)

# input fasta containing all sequences to be analysed
inputFasta = 'data/sample.fasta'

# this dictionary will contain the kmer counts for each sequence
kmerCounts = dict()

ffile = SeqIO.parse(inputFasta, 'fasta')
# iterate through each sequence in the fasta file
for seq_record in ffile:
    # extract just the accession number to use as ID
    id = str(seq_record.id)[1:]
    
    # count the occurance of each kmer and store in the dictionary
    kmerCounts[id] = countKmers(str(seq_record.seq), kmers)

kmerNorm = normKmers(kmerCounts)
kmerNorm

# create a dataframe from the dictionary
#df = pd.DataFrame.from_dict(kmerCounts, orient='index', columns=kmers)
#dfnorm = pd.DataFrame.from_dict(kmerNorm, orient='index', columns=kmers)
dfnorm = pd.DataFrame.from_dict(kmerNorm, orient = 'index',columns = kmers)

print(dfnorm)


dfnorm.to_csv("Genome_mer_laurence"+"k"+".csv")
 

