#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pysam import FastaFile
import pandas as pd
import random
import numpy as np
##key in the file name 

fasta_data = "genomic.fna"
data = FastaFile(fasta_data)


# In[2]:


##randomly choose one from the fai file created
first_sequence = data['JX869059.2']
first_sequence
##check len of my sequence
len(first_sequence)


# In[3]:


##data cleaning to remove letter N
##please ensure only ACGT are present
first_sequence = first_sequence.replace("N","")


# In[4]:





##check the length of my current sequence
len(first_sequence)


# In[5]:


##check with original sequence
print(first_sequence[2000:2900:100])
print(first_sequence[3000:3900:100])
print(first_sequence[4000:4900:100])
print(first_sequence[5000:5900:100])
print(first_sequence[6000:6900:100])
print(first_sequence[7000:7900:100])
print(first_sequence[8000:8900:100])
print(first_sequence[8000:8900:100])
print(first_sequence[9000:9900:100])


# In[6]:



##not a function but straightforward
sequence_new = first_sequence
n = 2000
while (n < 10000):
    for sequence in sequence_new[n]:
        if sequence == 'A':
            sequence_new = sequence_new[0:n]+'G'+sequence_new[n+1:]
        elif sequence =='G':
            sequence_new = sequence_new[0:n]+'A'+sequence_new[n+1:]
        elif sequence =='C':
            sequence_new = sequence_new[0:n]+'T'+sequence_new[n+1:]
        else:
            sequence_new = sequence_new[0:n]+'C'+sequence_new[n+1:]  
    print(n, sequence_new[n:n+900:100])
    n += 1000
        
            
print('Loop stop')


# In[7]:




##one change only (template)
def onechange(first_gamma):
    sequence_new = first_gamma
    n = 2000
    while (n < 10000):
        for sequence in sequence_new[n]:
            if sequence == 'A':
                sequence_new = sequence_new[0:n]+'G'+sequence_new[n+1:]
            elif sequence =='G':
                sequence_new = sequence_new[0:n]+'A'+sequence_new[n+1:]
            elif sequence =='C':
                sequence_new = sequence_new[0:n]+'T'+sequence_new[n+1:]
            else:
                sequence_new = sequence_new[0:n]+'C'+sequence_new[n+1:]  
        print(n, sequence_new[n:n+900:100])
        n += 1000
        
            
    print('Loop stop')
    
  




##now execute
ming = onechange(first_sequence)
ming


# In[8]:




##ten or one mutation where 1 indicate one mutation and other number indicate 10 mutation
def change(first_sequence,x):
    n = 2000
    if x == 1:
        while (n < 10000):
            sequence_new = first_sequence
            for sequence in sequence_new[n]:
                if sequence == 'A':
                    sequence_new = sequence_new[0:n]+'G'+sequence_new[n+1:]
                elif sequence =='G':
                    sequence_new = sequence_new[0:n]+'A'+sequence_new[n+1:]
                elif sequence =='C':
                    sequence_new = sequence_new[0:n]+'T'+sequence_new[n+1:]
                else:
                    sequence_new = sequence_new[0:n]+'C'+sequence_new[n+1:]  
            print('Check the previous 1000 sequence and current mutated 900 sequence:',n, sequence_new[n-1000:n+900:100])
            string = ">New Sequence\n"
            print(string, sequence_new,  file=open('mutation'+str(n)+'.fasta', 'w'))
            n += 1000
    else:
        while n < 10000:
            sequence_new = first_sequence
            for x in range(n,n+900,100):
                for sequence in sequence_new[x]:
                    if sequence == 'A':
                        sequence_new = sequence_new[0:x]+'G'+sequence_new[x+1:]
                    elif sequence =='G':
                        sequence_new = sequence_new[0:x]+'A'+sequence_new[x+1:]
                    elif sequence =='C':
                        sequence_new = sequence_new[0:x]+'T'+sequence_new[x+1:]
                    else:
                        sequence_new = sequence_new[0:x]+'C'+ sequence_new[x+1:]  
            print('Check the previous 1000 sequence and next current 900 sequence:',n, sequence_new[n-1000:n+900:100])
            string = ">New Sequence\n"
            print(string, sequence_new,  file=open('mutation'+str(n)+'.fasta', 'w'))
            n += 1000
            
            
    print('Loop stop')


##for example i perform 10 mutation in sequence
mming = change(first_sequence,2)
mming

