#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pysam import FastaFile
import pandas as pd
import random
import numpy as np
##key in the file name 


# In[2]:


##similarly for mers
fasta_mers = "genomic.fna"
mers = FastaFile(fasta_mers)
##randomly choose one from the fai file created
first_mers = mers['JX869059.2']
first_mers


# In[3]:


##check the length of my sequence
len(first_mers)


# In[4]:


##not a function but straightforward
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


# In[5]:


##check with original sequence
print(first_mers[2000:2900:100])
print(first_mers[3000:3900:100])
print(first_mers[4000:4900:100])
print(first_mers[5000:5900:100])
print(first_mers[6000:6900:100])
print(first_mers[7000:7900:100])
print(first_mers[8000:8900:100])
print(first_mers[8000:8900:100])
print(first_mers[9000:9900:100])


# In[6]:


##one change only (template)
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
    
  


# In[7]:


#check
ming = onechange(first_mers)
ming


# In[8]:


##ten or one mutation where 1 indicate one mutation and other number indicate 10 mutation
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
            print(mers_new,  file=open('mutation'+str(n)+'txt', 'w'))
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
            print(mers_new,  file=open('mutation'+str(n)+'txt', 'w'))
            #df = pd.DataFrame(mers_new)
            #df.to_csv("ming_algorithm"+str(n)+".csv")
            n += 1000
            
            
    print('Loop stop')


# In[9]:


##for example i perform 10 mutation in sequence
mming = change(first_mers,2)
mming

