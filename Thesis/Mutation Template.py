#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pysam import FastaFile
import pandas as pd
##key in the file name 


# In[2]:


##similarly for mers
fasta_mers = "genomic.fna"
mers = FastaFile(fasta_mers)
##randomly choose one from the fai file created
first_mers = mers['JX869059.2']
first_mers


# In[3]:


len(first_mers)


# In[4]:


##10th sequence
print(first_mers[2000:2900:100]) 


# In[5]:


##11th sequence
for i in range(3000, 3900, 100):
     
    print(first_mers[i]) 


# In[6]:


##12th sequence
for i in range(4000, 4900, 100):
     
    print(first_mers[i]) 


# In[7]:


##13th sequence
for i in range(5000, 5900, 100):
     
    print(first_mers[i]) 


# In[8]:


##14th sequence
for i in range(6000, 6900, 100):
     
    print(first_mers[i]) 


# In[9]:


##15th sequence
for i in range(7000, 7900, 100):
     
    print(first_mers[i]) 


# In[10]:


##16th sequence
for i in range(8000, 8900, 100):
     
    print(first_mers[i]) 


# In[11]:


##17th sequence
for i in range(9000, 9900, 100):
     
    print(first_mers[i]) 


# In[12]:


first_mers[2000:2900:100]


# In[13]:


def second_sequence(first_mers):
    n = 2000
    second_mers = first_mers
    for sequence in second_mers:
        if sequence == 'A':
            second_mers = second_mers[0:2000]+'G'+second_mers[2001:]
             
        elif sequence =='G':
            second_mers = second_mers[0:2000]+'A'+second_mers[2001:]
        elif sequence =='C':
            second_mers = second_mers[0:2000]+'T'+second_mers[2001:]
        else:
            second_mers = second_mers[0:2000]+'C'+second_mers[2001:]
            
    return second_mers
        

second_mers = second_sequence(first_mers)
print(second_mers[2000:2900:100])


# In[14]:


def tenth_sequence_component(second_mers, sumx):
    tenth_mers = second_mers
    for n in sumx:
        for sequence in list(tenth_mers[2100]):
            if sequence == 'A':
                tenth_mers = tenth_mers[0:2100]+'G'+tenth_mers[2101:]
             
            elif sequence =='G':
                tenth_mers = tenth_mers[0:2100]+'A'+tenth_mers[2101:]
            elif sequence =='C':
                tenth_mers = tenth_mers[0:2100]+'T'+tenth_mers[2101:]
            elif sequence =='T':
                tenth_mers = tenth_mers[0:2100]+'C'+tenth_mers[2101:]
            else:
                print('NO')
         
       

   
        for sequence in list(tenth_mers[2200]):
            if sequence == 'A':
                tenth_mers = tenth_mers[0:2200]+'G'+tenth_mers[2201:]
             
            elif sequence =='G':
                tenth_mers = tenth_mers[0:2200]+'A'+tenth_mers[2201:]
            elif sequence =='C':
                tenth_mers = tenth_mers[0:2200]+'T'+tenth_mers[2201:]
            elif sequence =='T':
                tenth_mers = tenth_mers[0:2200]+'C'+tenth_mers[2201:]
            else:
                print('NO')
          
    
        for sequence in list(tenth_mers[2300]):
            if sequence == 'A':
                tenth_mers = tenth_mers[0:2300]+'G'+tenth_mers[2301:]
             
            elif sequence =='G':
                tenth_mers = tenth_mers[0:2300]+'A'+tenth_mers[2301:]
            elif sequence =='C':
                tenth_mers = tenth_mers[0:2300]+'T'+tenth_mers[2301:]
            elif sequence =='T':
                tenth_mers = tenth_mers[0:2300]+'C'+tenth_mers[2301:]
            else:
                print('NO')
                
                
        for sequence in list(tenth_mers[2400]):
            if sequence == 'A':
                tenth_mers = tenth_mers[0:2400]+'G'+tenth_mers[2401:]
             
            elif sequence =='G':
                tenth_mers = tenth_mers[0:2400]+'A'+tenth_mers[2401:]
            elif sequence =='C':
                tenth_mers = tenth_mers[0:2400]+'T'+tenth_mers[2401:]
            elif sequence =='T':
                tenth_mers = tenth_mers[0:2400]+'C'+tenth_mers[2401:]
            else:
                print('NO')
        
    
        for sequence in list(tenth_mers[2500]):
            if sequence == 'A':
                tenth_mers = tenth_mers[0:2500]+'G'+tenth_mers[2501:]
             
            elif sequence =='G':
                tenth_mers = tenth_mers[0:2500]+'A'+tenth_mers[2501:]
            elif sequence =='C':
                tenth_mers = tenth_mers[0:2500]+'T'+tenth_mers[2501:]
            elif sequence =='T':
                tenth_mers = tenth_mers[0:2500]+'C'+tenth_mers[2501:]
            else:
                print('NO')
         
        
    
        for sequence in list(tenth_mers[2600]):
            if sequence == 'A':
                tenth_mers = tenth_mers[0:2600]+'G'+tenth_mers[2601:]
             
            elif sequence =='G':
                tenth_mers = tenth_mers[0:2600]+'A'+tenth_mers[2601:]
            elif sequence =='C':
                tenth_mers = tenth_mers[0:2600]+'T'+tenth_mers[2601:]
            elif sequence =='T':
                tenth_mers = tenth_mers[0:2600]+'C'+tenth_mers[2601:]
            else:
                print('NO')
                
        for sequence in list(tenth_mers[2700]):
            if sequence == 'A':
                tenth_mers = tenth_mers[0:2700]+'G'+tenth_mers[2701:]
             
            elif sequence =='G':
                tenth_mers = tenth_mers[0:2700]+'A'+tenth_mers[2701:]
            elif sequence =='C':
                tenth_mers = tenth_mers[0:2700]+'T'+tenth_mers[2701:]
            elif sequence =='T':
                tenth_mers = tenth_mers[0:2700]+'C'+tenth_mers[2701:]
            else:
                print('NO')
                
        
        
        for sequence in list(tenth_mers[2800]):
            if sequence == 'A':
                tenth_mers = tenth_mers[0:2800]+'G'+tenth_mers[2801:]
             
            elif sequence =='G':
                tenth_mers = tenth_mers[0:2800]+'A'+tenth_mers[2801:]
            elif sequence =='C':
                tenth_mers = tenth_mers[0:2800]+'T'+tenth_mers[2801:]
            elif sequence =='T':
                tenth_mers = tenth_mers[0:2800]+'C'+tenth_mers[2801:]
            else:
                print('NO')
                
           
    
        for sequence in list(tenth_mers[2900]):
            if sequence == 'A':
                tenth_mers = tenth_mers[0:2900]+'G'+tenth_mers[2901:]
             
            elif sequence =='G':
                tenth_mers = tenth_mers[0:2900]+'A'+tenth_mers[2901:]
            elif sequence =='C':
                tenth_mers = tenth_mers[0:2900]+'T'+tenth_mers[2901:]
            elif sequence =='T':
                tenth_mers = tenth_mers[0:2900]+'C'+tenth_mers[2901:]
            else:
                print('NO')
    
                


                
        return tenth_mers
    
    
    
    
sumx = [2100,2200,2300,2400,2500,2600,2700,2800,2900]   
tenth_mers = tenth_sequence_component(second_mers,sumx)

##Comparision for 1st and 10th sequence
print(first_mers[2000:3000:100])
print(second_mers[2000:3000:100])
print(tenth_mers[2000:3000:100]) 
