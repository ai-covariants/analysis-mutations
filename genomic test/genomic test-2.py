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




def kmer_laurence(k,ffile):

    # this dictionary will contain the kmer counts for each sequence

    kmerCounts = dict()

    for seq_record in ffile:
    # extract just the accession number to use as ID
        id = str(seq_record.id)[1:] 
        # count the occurance of each kmer and store in the dictionary
        kmerCounts[id] = countKmers(str(seq_record.seq), kmers)

        print(seq_record, ' seq_record')

    kmerNorm = kmerCounts

    return kmerNorm


#-----------------------------------------------------------------



def build_kmers(sequence, ksize): # found online - used
    kmers = []
    n_kmers = len(sequence) - ksize + 1

    for i in range(n_kmers):
        kmer = sequence[i:i + ksize]
        kmers.append(kmer)

    return kmers


def clean_df(data): 

    series = data.squeeze() 
    series = series.str.split(",", expand = True)
    series 

    df = pd.DataFrame(series)  

    ##replace none with 0
    df = df.drop_duplicates()
    df = df.fillna(0)
    df = df.replace("[]","0")
    df = df.dropna()
    
    columns = df[0]
    pd.set_option('display.max_rows', columns.shape[0]+1) 
    df = df.iloc[1: , :]
    
    
    test_df = pd.DataFrame(df) 
    idx = test_df.iloc[:, 0]
    test_df = test_df.iloc[: , 1:]
    
    
    
    freq_df = pd.DataFrame(columns = test_df.stack().unique()) 
    

    for i in test_df.index:
        freq_df.loc[i] = test_df.loc[i].value_counts() 

    freq_df = freq_df.fillna(0)  

    ##sum needs to be greater than the number of rows
    freq_df = freq_df[freq_df.columns[freq_df.sum()> freq_df.shape[0]]] 
    freq_df = freq_df[~freq_df.index.duplicated(keep='first')] 

    ##notice that last one is 0 hence delete it!
    freq_df = freq_df.iloc[:, :-1] 
    freq_df.index = idx
    df = freq_df.reindex(sorted(freq_df.columns), axis=1)  
    print(df.shape)
    

    return df


def kmer_ming(k,ffile):

    G = []

    for seq_record in ffile:
        # extract just the accession number to use as ID
        id_name = str(seq_record.id)
        sequence = seq_record
        seq = sequence.seq.rstrip("N")
        covid = build_kmers(seq,k)
        G.append('{},{}'.format(id_name, covid))

    df = pd.DataFrame(G)
 
    kmer = clean_df(df) 

    return kmer








# create all possible kmers for a given length of k
k = 3

method = 2  # 
kmers = createKmers('ACGT', k)

# input fasta containing all sequences to be analysed
inputFasta = 'genomic.fna'



ffile = SeqIO.parse(inputFasta, 'fasta')
# iterate through each sequence in the fasta file

if method == 1: #laurence
    kmerNorm = kmer_laurence(k,ffile)

    dfnorm = pd.DataFrame.from_dict(kmerNorm, orient = 'index',columns = kmers)

    print(dfnorm)

    dfnorm.to_csv("k-mer-lau"+str(k)+".csv")


if method == 2: #ming
    kmer_df = kmer_ming(k,ffile)
    
    kmer_df.to_csv("k-mer-ming"+str(k)+".csv")


# In[ ]:




