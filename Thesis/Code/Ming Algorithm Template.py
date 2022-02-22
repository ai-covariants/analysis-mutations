#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pysam import FastaFile
import pandas as pd
import random
##key in the file name 


# In[2]:


##similarly for mers
fasta_mers = "genomic.fna"
mers = FastaFile(fasta_mers)
##randomly choose one from the fai file created
first_mers = mers['JX869059.2']
first_mers


##one mutation
def onechange(first_mers):
    mers_new = first_mers
    n = 2000
    while (n < 10000):
        for sequence in mers_new[n]:
            if sequence == 'A':
                mers_new = mers_new[0:n]+'G'+mers_new[n+1:]
            elif sequence =='G':
                mers_new = mers_new[0:n]+'A'+mers_new[n+1:]
            elif sequence =='C':
                mers_new = mers_new[0:n]+'T'+mers_new[n+1:]
            else:
                mers_new = mers_new[0:n]+'C'+mers_new[n+1:]  
        print(n, mers_new[n:n+900:100])
        n += 1000
        
            
    print('Loop stop')
    


ming = onechange(first_mers)
ming


# In[8]:

##option for one mutation or ten mutations
def change(first_mers,x):
    mers_new = first_mers
    n = 2000
    if x == 1:
        while (n < 10000):
            for sequence in mers_new[n]:
                if sequence == 'A':
                    mers_new = mers_new[0:n]+'G'+mers_new[n+1:]
                elif sequence =='G':
                    mers_new = mers_new[0:n]+'A'+mers_new[n+1:]
                elif sequence =='C':
                    mers_new = mers_new[0:n]+'T'+mers_new[n+1:]
                else:
                    mers_new = mers_new[0:n]+'C'+mers_new[n+1:]  
            print(n, mers_new[n:n+900:100])
            n += 1000
    else:
        while n < 10000:
            for x in range(n,n+900,100):
                for sequence in mers_new[x]:
                    if sequence == 'A':
                        mers_new = mers_new[0:x]+'G'+mers_new[x+1:]
                    elif sequence =='G':
                        mers_new = mers_new[0:x]+'A'+mers_new[x+1:]
                    elif sequence =='C':
                        mers_new = mers_new[0:x]+'T'+mers_new[x+1:]
                    else:
                        mers_new = mers_new[0:x]+'C'+mers_new[x+1:]  
            print(n, mers_new[n:n+900:100])
            n += 1000
            
    print('Loop stop')


# In[9]:


mming = change(first_mers,2)
mming

