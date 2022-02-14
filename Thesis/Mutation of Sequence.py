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


# In[5]:


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

##Comparision
print('Sequence for Original Sequence',first_mers[2000:3000:100])
print('Sequence for Second Sequence',second_mers[2000:3000:100])
print('Sequence for Tenth Sequence',tenth_mers[2000:3000:100]) 


# In[6]:


def third_sequence(first_mers):
    n = 3000
    third_mers = first_mers
    for sequence in third_mers:
        if sequence == 'A':
            third_mers = third_mers[0:3000]+'G'+third_mers[3001:]
             
        elif sequence =='G':
            third_mers = third_mers[0:3000]+'A'+third_mers[3001:]
        elif sequence =='C':
            third_mers = third_mers[0:3000]+'T'+third_mers[3001:]
        else:
            third_mers = third_mers[0:3000]+'C'+third_mers[3001:]
            
    return third_mers
        

third_mers = third_sequence(first_mers)


##Comparision
print('Sequence for Original Sequence',first_mers[3000:4000:100])
print('Sequence for Third Sequence',third_mers[3000:4000:100])


# In[7]:


def eleventh_sequence_component(third_mers, sumx3):
    eleventh_mers = third_mers
    for n in sumx3:
        for sequence in list(eleventh_mers[3100]):
            if sequence == 'A':
                eleventh_mers = eleventh_mers[0:3100]+'G'+eleventh_mers[3101:]
             
            elif sequence =='G':
                eleventh_mers = eleventh_mers[0:3100]+'A'+eleventh_mers[3101:]
            elif sequence =='C':
                eleventh_mers = eleventh_mers[0:3100]+'T'+eleventh_mers[3101:]
            elif sequence =='T':
                eleventh_mers = eleventh_mers[0:3100]+'C'+ eleventh_mers[3101:]
            else:
                print('NO')
         
       

   
        for sequence in list(eleventh_mers[3200]):
            if sequence == 'A':
                eleventh_mers = eleventh_mers[0:3200]+'G'+ eleventh_mers[3201:]
             
            elif sequence =='G':
                eleventh_mers = eleventh_mers[0:3200]+'A'+eleventh_mers[3201:]
            elif sequence =='C':
                eleventh_mers = eleventh_mers[0:3200]+'T'+eleventh_mers[3201:]
            elif sequence =='T':
                eleventh_mers = eleventh_mers[0:3200]+'C'+ eleventh_mers[3201:]
            else:
                print('NO')
          
    
        for sequence in list(eleventh_mers[3300]):
            if sequence == 'A':
                eleventh_mers = eleventh_mers[0:3300]+'G'+ eleventh_mers[3301:]
             
            elif sequence =='G':
                eleventh_mers = eleventh_mers[0:3300]+'A'+eleventh_mers[3301:]
            elif sequence =='C':
                eleventh_mers = eleventh_mers[0:3300]+'T'+eleventh_mers[3301:]
            elif sequence =='T':
                eleventh_mers = eleventh_mers[0:3300]+'C'+ eleventh_mers[3301:]
            else:
                print('NO')
                
                
        for sequence in list(eleventh_mers[3400]):
            if sequence == 'A':
                eleventh_mers = eleventh_mers[0:3400]+'G'+ eleventh_mers[3401:]
             
            elif sequence =='G':
                eleventh_mers = eleventh_mers[0:3400]+'A'+eleventh_mers[3401:]
            elif sequence =='C':
                eleventh_mers = eleventh_mers[0:3400]+'T'+eleventh_mers[3401:]
            elif sequence =='T':
                eleventh_mers = eleventh_mers[0:3400]+'C'+ eleventh_mers[3401:]
            else:
                print('NO')
        
    
        for sequence in list(eleventh_mers[3500]):
            if sequence == 'A':
                eleventh_mers = eleventh_mers[0:3500]+'G'+ eleventh_mers[3501:]
             
            elif sequence =='G':
                eleventh_mers = eleventh_mers[0:3500]+'A'+eleventh_mers[3501:]
            elif sequence =='C':
                eleventh_mers = eleventh_mers[0:3500]+'T'+eleventh_mers[3501:]
            elif sequence =='T':
                eleventh_mers = eleventh_mers[0:3500]+'C'+ eleventh_mers[3501:]
            else:
                print('NO')
         
        
    
        for sequence in list(eleventh_mers[3600]):
            if sequence == 'A':
                eleventh_mers = eleventh_mers[0:3600]+'G'+ eleventh_mers[3601:]
             
            elif sequence =='G':
                eleventh_mers = eleventh_mers[0:3600]+'A'+eleventh_mers[3601:]
            elif sequence =='C':
                eleventh_mers = eleventh_mers[0:3600]+'T'+eleventh_mers[3601:]
            elif sequence =='T':
                eleventh_mers = eleventh_mers[0:3600]+'C'+ eleventh_mers[3601:]
            else:
                print('NO')
                
        for sequence in list(eleventh_mers[3700]):
            if sequence == 'A':
                eleventh_mers = eleventh_mers[0:3700]+'G'+ eleventh_mers[3701:]
             
            elif sequence =='G':
                eleventh_mers = eleventh_mers[0:3700]+'A'+eleventh_mers[3701:]
            elif sequence =='C':
                eleventh_mers = eleventh_mers[0:3700]+'T'+eleventh_mers[3701:]
            elif sequence =='T':
                eleventh_mers = eleventh_mers[0:3700]+'C'+ eleventh_mers[3701:]
            else:
                print('NO')
                
        
        
        for sequence in list(eleventh_mers[3800]):
            if sequence == 'A':
                eleventh_mers = eleventh_mers[0:3800]+'G'+ eleventh_mers[3801:]
             
            elif sequence =='G':
                eleventh_mers = eleventh_mers[0:3800]+'A'+eleventh_mers[3801:]
            elif sequence =='C':
                eleventh_mers = eleventh_mers[0:3800]+'T'+eleventh_mers[3801:]
            elif sequence =='T':
                eleventh_mers = eleventh_mers[0:3800]+'C'+ eleventh_mers[3801:]
            else:
                print('NO')
                
           
    
        for sequence in list(eleventh_mers[3900]):
            if sequence == 'A':
                eleventh_mers = eleventh_mers[0:3900]+'G'+ eleventh_mers[3901:]
             
            elif sequence =='G':
                eleventh_mers = eleventh_mers[0:3900]+'A'+eleventh_mers[3901:]
            elif sequence =='C':
                eleventh_mers = eleventh_mers[0:3900]+'T'+eleventh_mers[3901:]
            elif sequence =='T':
                eleventh_mers = eleventh_mers[0:3900]+'C'+ eleventh_mers[3901:]
            else:
                print('NO')
    
                


                
        return eleventh_mers
    
    
    
    
sumx3 = [3100,3200,3300,3400,3500,3600,3700,3800,3900]   
eleventh_mers = eleventh_sequence_component(third_mers,sumx3)

##Comparision
print('Sequence for Original Sequence',first_mers[3000:4000:100])
print('Sequence for Third Sequence',third_mers[3000:4000:100])
print('Sequence for Eleventh Sequence',eleventh_mers[3000:4000:100]) 


# In[8]:


def fourth_sequence(first_mers):
    n = 3000
    fourth_mers = first_mers
    for sequence in fourth_mers:
        if sequence == 'A':
            fourth_mers = fourth_mers[0:4000]+'G'+fourth_mers[4001:]
             
        elif sequence =='G':
            fourth_mers = fourth_mers[0:4000]+'A'+fourth_mers[4001:]
        elif sequence =='C':
            fourth_mers = fourth_mers[0:4000]+'T'+fourth_mers[4001:]
        else:
            fourth_mers = fourth_mers[0:4000]+'C'+fourth_mers[4001:]
            
    return fourth_mers
        

fourth_mers = fourth_sequence(first_mers)


##Comparision for 1st and 3rd sequence
print('Sequence for Original Sequence',first_mers[4000:5000:100])
print('Sequence for Fourth Sequence',fourth_mers[4000:5000:100])


# In[9]:


def twelveth_sequence_component(fourth_mers, sumx4):
    twelveth_mers = fourth_mers
    for n in sumx4:
        for sequence in list(twelveth_mers[4100]):
            if sequence == 'A':
                twelveth_mers = twelveth_mers[0:4100]+'G'+ twelveth_mers[4101:]
             
            elif sequence =='G':
                twelveth_mers = twelveth_mers[0:4100]+'A'+ twelveth_mers[4101:]
            elif sequence =='C':
                twelveth_mers = twelveth_mers[0:4100]+'T'+ twelveth_mers[4101:]
            elif sequence =='T':
                twelveth_mers = twelveth_mers[0:4100]+'C'+ twelveth_mers[4101:]
            else:
                print('NO')
         
       

    for sequence in list(twelveth_mers[4200]):
            if sequence == 'A':
                twelveth_mers = twelveth_mers[0:4200]+'G'+ twelveth_mers[4201:]
             
            elif sequence =='G':
                twelveth_mers = twelveth_mers[0:4200]+'A'+ twelveth_mers[4201:]
            elif sequence =='C':
                twelveth_mers = twelveth_mers[0:4200]+'T'+ twelveth_mers[4201:]
            elif sequence =='T':
                twelveth_mers = twelveth_mers[0:4200]+'C'+ twelveth_mers[4201:]
            else:
                print('NO')
          
    
    for sequence in list(twelveth_mers[4300]):
            if sequence == 'A':
                twelveth_mers = twelveth_mers[0:4300]+'G'+ twelveth_mers[4301:]
             
            elif sequence =='G':
                twelveth_mers = twelveth_mers[0:4300]+'A'+ twelveth_mers[4301:]
            elif sequence =='C':
                twelveth_mers = twelveth_mers[0:4300]+'T'+ twelveth_mers[4301:]
            elif sequence =='T':
                twelveth_mers = twelveth_mers[0:4300]+'C'+ twelveth_mers[4301:]
            else:
                print('NO')
    
           
        
        
    for sequence in list(twelveth_mers[4400]):
            if sequence == 'A':
                twelveth_mers = twelveth_mers[0:4400]+'G'+ twelveth_mers[4401:]
             
            elif sequence =='G':
                twelveth_mers = twelveth_mers[0:4400]+'A'+ twelveth_mers[4401:]
            elif sequence =='C':
                twelveth_mers = twelveth_mers[0:4400]+'T'+ twelveth_mers[4401:]
            elif sequence =='T':
                twelveth_mers = twelveth_mers[0:4400]+'C'+ twelveth_mers[4401:]
            else:
                print('NO')


                
                
                
    for sequence in list(twelveth_mers[4500]):
            if sequence == 'A':
                twelveth_mers = twelveth_mers[0:4500]+'G'+ twelveth_mers[4501:]
             
            elif sequence =='G':
                twelveth_mers = twelveth_mers[0:4500]+'A'+ twelveth_mers[4501:]
            elif sequence =='C':
                twelveth_mers = twelveth_mers[0:4500]+'T'+ twelveth_mers[4501:]
            elif sequence =='T':
                twelveth_mers = twelveth_mers[0:4500]+'C'+ twelveth_mers[4501:]
            else:
                print('NO')
                
                
                
                
    for sequence in list(twelveth_mers[4600]):
            if sequence == 'A':
                twelveth_mers = twelveth_mers[0:4600]+'G'+ twelveth_mers[4601:]
             
            elif sequence =='G':
                twelveth_mers = twelveth_mers[0:4600]+'A'+ twelveth_mers[4601:]
            elif sequence =='C':
                twelveth_mers = twelveth_mers[0:4600]+'T'+ twelveth_mers[4601:]
            elif sequence =='T':
                twelveth_mers = twelveth_mers[0:4600]+'C'+ twelveth_mers[4601:]
            else:
                print('NO')         
                
        
        
    for sequence in list(twelveth_mers[4700]):
            if sequence == 'A':
                twelveth_mers = twelveth_mers[0:4700]+'G'+ twelveth_mers[4701:]
             
            elif sequence =='G':
                twelveth_mers = twelveth_mers[0:4700]+'A'+ twelveth_mers[4701:]
            elif sequence =='C':
                twelveth_mers = twelveth_mers[0:4700]+'T'+ twelveth_mers[4701:]
            elif sequence =='T':
                twelveth_mers = twelveth_mers[0:4700]+'C'+ twelveth_mers[4701:]
            else:
                print('NO')
        
        
        
        
    for sequence in list(twelveth_mers[4800]):
            if sequence == 'A':
                twelveth_mers = twelveth_mers[0:4800]+'G'+ twelveth_mers[4801:]
             
            elif sequence =='G':
                twelveth_mers = twelveth_mers[0:4800]+'A'+ twelveth_mers[4801:]
            elif sequence =='C':
                twelveth_mers = twelveth_mers[0:4800]+'T'+ twelveth_mers[4801:]
            elif sequence =='T':
                twelveth_mers = twelveth_mers[0:4800]+'C'+ twelveth_mers[4801:]
            else:
                print('NO')
        
       
    
    for sequence in list(twelveth_mers[4900]):
            if sequence == 'A':
                twelveth_mers = twelveth_mers[0:4900]+'G'+ twelveth_mers[4901:]
             
            elif sequence =='G':
                twelveth_mers = twelveth_mers[0:4900]+'A'+ twelveth_mers[4901:]
            elif sequence =='C':
                twelveth_mers = twelveth_mers[0:4900]+'T'+ twelveth_mers[4901:]
            elif sequence =='T':
                twelveth_mers = twelveth_mers[0:4900]+'C'+ twelveth_mers[4901:]
            else:
                print('NO')
        
                
    return twelveth_mers
    
    
    
    
sumx4 = [4100,4200,4300,4400,4500,4600,4700,4800,4900]   
twelveth_mers = twelveth_sequence_component(fourth_mers,sumx4)

##Comparision
print('Sequence for Original Sequence',first_mers[4000:5000:100])
print('Sequence for Fourth Sequence',fourth_mers[4000:5000:100])
print('Sequence for Twelveth Sequence',twelveth_mers[4000:5000:100])


# In[10]:


def fifth_sequence(first_mers):
    n = 3000
    fifth_mers = first_mers
    for sequence in fifth_mers:
        if sequence == 'A':
            fifth_mers = fifth_mers[0:5000]+'G'+ fifth_mers[5001:]
             
        elif sequence =='G':
            fifth_mers = fifth_mers[0:5000]+'A'+ fifth_mers[5001:]
        elif sequence =='C':
            fifth_mers = fifth_mers[0:5000]+'T'+ fifth_mers[5001:]
        else:
            fifth_mers = fifth_mers[0:5000]+'C'+ fifth_mers[5001:]
            
    return fifth_mers
        

fifth_mers = fifth_sequence(first_mers)


##Comparision
print('Sequence for Original Sequence',first_mers[5000:6000:100])
print('Sequence for Fifth Sequence',fifth_mers[5000:6000:100])


# In[11]:


def thirteenth_sequence_component(fifth_mers, sumx5):
    thirteenth_mers = fifth_mers
    for n in sumx5:
        for sequence in list(thirteenth_mers[5100]):
            if sequence == 'A':
                thirteenth_mers = thirteenth_mers[0:5100]+'G'+ thirteenth_mers[5101:]
             
            elif sequence =='G':
                thirteenth_mers = thirteenth_mers[0:5100]+'A'+ thirteenth_mers[5101:]
            elif sequence =='C':
                thirteenth_mers = thirteenth_mers[0:5100]+'T'+ thirteenth_mers[5101:]
            elif sequence =='T':
                thirteenth_mers = thirteenth_mers[0:5100]+'C'+ thirteenth_mers[5101:]
            else:
                print('NO')
         
       
    for sequence in list(thirteenth_mers[5200]):
            if sequence == 'A':
                thirteenth_mers = thirteenth_mers[0:5200]+'G'+ thirteenth_mers[5201:]
             
            elif sequence =='G':
                thirteenth_mers = thirteenth_mers[0:5200]+'A'+ thirteenth_mers[5201:]
            elif sequence =='C':
                thirteenth_mers = thirteenth_mers[0:5200]+'T'+ thirteenth_mers[5201:]
            elif sequence =='T':
                thirteenth_mers = thirteenth_mers[0:5200]+'C'+ thirteenth_mers[5201:]
            else:
                print('NO')
    
     
    for sequence in list(thirteenth_mers[5300]):
            if sequence == 'A':
                thirteenth_mers = thirteenth_mers[0:5300]+'G'+ thirteenth_mers[5301:]
             
            elif sequence =='G':
                thirteenth_mers = thirteenth_mers[0:5300]+'A'+ thirteenth_mers[5301:]
            elif sequence =='C':
                thirteenth_mers = thirteenth_mers[0:5300]+'T'+ thirteenth_mers[5301:]
            elif sequence =='T':
                thirteenth_mers = thirteenth_mers[0:5300]+'C'+ thirteenth_mers[5301:]
            else:
                print('NO')    
                
                
                
                
                
    for sequence in list(thirteenth_mers[5400]):
            if sequence == 'A':
                thirteenth_mers = thirteenth_mers[0:5400]+'G'+ thirteenth_mers[5401:]
             
            elif sequence =='G':
                thirteenth_mers = thirteenth_mers[0:5400]+'A'+ thirteenth_mers[5401:]
            elif sequence =='C':
                thirteenth_mers = thirteenth_mers[0:5400]+'T'+ thirteenth_mers[5401:]
            elif sequence =='T':
                thirteenth_mers = thirteenth_mers[0:5400]+'C'+ thirteenth_mers[5401:]
            else:
                print('NO') 
                
                
                
                
                
    for sequence in list(thirteenth_mers[5500]):
            if sequence == 'A':
                thirteenth_mers = thirteenth_mers[0:5500]+'G'+ thirteenth_mers[5501:]
             
            elif sequence =='G':
                thirteenth_mers = thirteenth_mers[0:5500]+'A'+ thirteenth_mers[5501:]
            elif sequence =='C':
                thirteenth_mers = thirteenth_mers[0:5500]+'T'+ thirteenth_mers[5501:]
            elif sequence =='T':
                thirteenth_mers = thirteenth_mers[0:5500]+'C'+ thirteenth_mers[5501:]
            else:
                print('NO')  
                
                
                
                
    for sequence in list(thirteenth_mers[5600]):
            if sequence == 'A':
                thirteenth_mers = thirteenth_mers[0:5600]+'G'+ thirteenth_mers[5601:]
             
            elif sequence =='G':
                thirteenth_mers = thirteenth_mers[0:5600]+'A'+ thirteenth_mers[5601:]
            elif sequence =='C':
                thirteenth_mers = thirteenth_mers[0:5600]+'T'+ thirteenth_mers[5601:]
            elif sequence =='T':
                thirteenth_mers = thirteenth_mers[0:5600]+'C'+ thirteenth_mers[5601:]
            else:
                print('NO')            
                
                
    
    
    for sequence in list(thirteenth_mers[5700]):
            if sequence == 'A':
                thirteenth_mers = thirteenth_mers[0:5700]+'G'+ thirteenth_mers[5701:]
             
            elif sequence =='G':
                thirteenth_mers = thirteenth_mers[0:5700]+'A'+ thirteenth_mers[5701:]
            elif sequence =='C':
                thirteenth_mers = thirteenth_mers[0:5700]+'T'+ thirteenth_mers[5701:]
            elif sequence =='T':
                thirteenth_mers = thirteenth_mers[0:5700]+'C'+ thirteenth_mers[5701:]
            else:
                print('NO')
    
    
    
    for sequence in list(thirteenth_mers[5800]):
            if sequence == 'A':
                thirteenth_mers = thirteenth_mers[0:5800]+'G'+ thirteenth_mers[5801:]
             
            elif sequence =='G':
                thirteenth_mers = thirteenth_mers[0:5800]+'A'+ thirteenth_mers[5801:]
            elif sequence =='C':
                thirteenth_mers = thirteenth_mers[0:5800]+'T'+ thirteenth_mers[5801:]
            elif sequence =='T':
                thirteenth_mers = thirteenth_mers[0:5800]+'C'+ thirteenth_mers[5801:]
            else:
                print('NO')
    
    for sequence in list(thirteenth_mers[5900]):
            if sequence == 'A':
                thirteenth_mers = thirteenth_mers[0:9100]+'G'+ thirteenth_mers[5901:]
             
            elif sequence =='G':
                thirteenth_mers = thirteenth_mers[0:5900]+'A'+ thirteenth_mers[5901:]
            elif sequence =='C':
                thirteenth_mers = thirteenth_mers[0:5900]+'T'+ thirteenth_mers[5901:]
            elif sequence =='T':
                thirteenth_mers = thirteenth_mers[0:5900]+'C'+ thirteenth_mers[5901:]
            else:
                print('NO')
    
    
    
        
    return thirteenth_mers
    
    
    
    
sumx5 = [5100,5200,5300,5400,5500,5600,5700,5800,5900]   
thirteenth_mers = thirteenth_sequence_component(fifth_mers,sumx5)

##Comparision
print('Sequence for Original Sequence',first_mers[5000:6000:100])
print('Sequence for Fifth Sequence',fifth_mers[5000:6000:100])
print('Sequence for Thirteenth Sequence',thirteenth_mers[5000:6000:100])


# In[12]:


def sixth_sequence(first_mers):
    n = 6000
    sixth_mers = first_mers
    for sequence in sixth_mers:
        if sequence == 'A':
            sixth_mers = sixth_mers[0:6000]+'G'+ sixth_mers[6001:]
             
        elif sequence =='G':
            sixth_mers = sixth_mers[0:6000]+'A'+ sixth_mers[6001:]
        elif sequence =='C':
            sixth_mers = sixth_mers[0:6000]+'T'+ sixth_mers[6001:]
        else:
            sixth_mers = sixth_mers[0:6000]+'C'+ sixth_mers[6001:]
            
    return sixth_mers
        

sixth_mers = sixth_sequence(first_mers)


##Comparision
print('Sequence for Original Sequence',first_mers[6000:7000:100])
print('Sequence for Sixth Sequence',sixth_mers[6000:7000:100])


# In[13]:


def fourteenth_sequence_component(sixth_mers, sumx6):
    fourteenth_mers = sixth_mers
    for n in sumx6:
        for sequence in list(fourteenth_mers[6100]):
            if sequence == 'A':
                fourteenth_mers = fourteenth_mers[0:6100]+'G'+ fourteenth_mers[6101:]
             
            elif sequence =='G':
                fourteenth_mers = fourteenth_mers[0:6100]+'A'+ fourteenth_mers[6101:]
            elif sequence =='C':
                fourteenth_mers = fourteenth_mers[0:6100]+'T'+ fourteenth_mers[6101:]
            elif sequence =='T':
                fourteenth_mers = fourteenth_mers[0:6100]+'C'+ fourteenth_mers[6101:]
            else:
                print('NO')
         
       
    for sequence in list(fourteenth_mers[6200]):
            if sequence == 'A':
                fourteenth_mers = fourteenth_mers[0:6200]+'G'+ fourteenth_mers[6201:]
             
            elif sequence =='G':
                fourteenth_mers = fourteenth_mers[0:6200]+'A'+ fourteenth_mers[6201:]
            elif sequence =='C':
                fourteenth_mers = fourteenth_mers[0:6200]+'T'+ fourteenth_mers[6201:]
            elif sequence =='T':
                fourteenth_mers = fourteenth_mers[0:6200]+'C'+ fourteenth_mers[6201:]
            else:
                print('NO')
    
     
    for sequence in list(fourteenth_mers[6300]):
            if sequence == 'A':
                fourteenth_mers = fourteenth_mers[0:6300]+'G'+ fourteenth_mers[6301:]
             
            elif sequence =='G':
                fourteenth_mers = fourteenth_mers[0:6300]+'A'+ fourteenth_mers[6301:]
            elif sequence =='C':
                fourteenth_mers = fourteenth_mers[0:6300]+'T'+ fourteenth_mers[6301:]
            elif sequence =='T':
                fourteenth_mers = fourteenth_mers[0:6300]+'C'+ fourteenth_mers[6301:]
            else:
                print('NO')    
                
                
                
                
                
    for sequence in list(fourteenth_mers[6400]):
            if sequence == 'A':
                fourteenth_mers = fourteenth_mers[0:6400]+'G'+ fourteenth_mers[6401:]
             
            elif sequence =='G':
                fourteenth_mers = fourteenth_mers[0:6400]+'A'+ fourteenth_mers[6401:]
            elif sequence =='C':
                fourteenth_mers = fourteenth_mers[0:6400]+'T'+ fourteenth_mers[6401:]
            elif sequence =='T':
                fourteenth_mers = fourteenth_mers[0:6400]+'C'+ fourteenth_mers[6401:]
            else:
                print('NO')
                
                
    for sequence in list(fourteenth_mers[6500]):
            if sequence == 'A':
                fourteenth_mers = fourteenth_mers[0:6500]+'G'+ fourteenth_mers[6501:]
             
            elif sequence =='G':
                fourteenth_mers = fourteenth_mers[0:6500]+'A'+ fourteenth_mers[6501:]
            elif sequence =='C':
                fourteenth_mers = fourteenth_mers[0:6500]+'T'+ fourteenth_mers[6501:]
            elif sequence =='T':
                fourteenth_mers = fourteenth_mers[0:6500]+'C'+ fourteenth_mers[6501:]
            else:
                print('NO')             
                
    for sequence in list(fourteenth_mers[6600]):
            if sequence == 'A':
                fourteenth_mers = fourteenth_mers[0:6600]+'G'+ fourteenth_mers[6601:]
             
            elif sequence =='G':
                fourteenth_mers = fourteenth_mers[0:6600]+'A'+ fourteenth_mers[6601:]
            elif sequence =='C':
                fourteenth_mers = fourteenth_mers[0:6600]+'T'+ fourteenth_mers[6601:]
            elif sequence =='T':
                fourteenth_mers = fourteenth_mers[0:6600]+'C'+ fourteenth_mers[6601:]
            else:
                print('NO')            
    
  

    for sequence in list(fourteenth_mers[6700]):
            if sequence == 'A':
                fourteenth_mers = fourteenth_mers[0:6700]+'G'+ fourteenth_mers[6701:]
             
            elif sequence =='G':
                fourteenth_mers = fourteenth_mers[0:6700]+'A'+ fourteenth_mers[6701:]
            elif sequence =='C':
                fourteenth_mers = fourteenth_mers[0:6700]+'T'+ fourteenth_mers[6701:]
            elif sequence =='T':
                fourteenth_mers = fourteenth_mers[0:6700]+'C'+ fourteenth_mers[6701:]
            else:
                print('NO')
    
   


    for sequence in list(fourteenth_mers[6800]):
            if sequence == 'A':
                fourteenth_mers = fourteenth_mers[0:6800]+'G'+ fourteenth_mers[6801:]
             
            elif sequence =='G':
                fourteenth_mers = fourteenth_mers[0:6800]+'A'+ fourteenth_mers[6801:]
            elif sequence =='C':
                fourteenth_mers = fourteenth_mers[0:6800]+'T'+ fourteenth_mers[6801:]
            elif sequence =='T':
                fourteenth_mers = fourteenth_mers[0:6800]+'C'+ fourteenth_mers[6801:]
            else:
                print('NO')

    
    
    
    for sequence in list(fourteenth_mers[6900]):
            if sequence == 'A':
                fourteenth_mers = fourteenth_mers[0:6900]+'G'+ fourteenth_mers[6901:]
             
            elif sequence =='G':
                fourteenth_mers = fourteenth_mers[0:6900]+'A'+ fourteenth_mers[6901:]
            elif sequence =='C':
                fourteenth_mers = fourteenth_mers[0:6900]+'T'+ fourteenth_mers[6901:]
            elif sequence =='T':
                fourteenth_mers = fourteenth_mers[0:6900]+'C'+ fourteenth_mers[6901:]
            else:
                print('NO')
        
    return fourteenth_mers
    
    
    
    
sumx6 = [6100,6200,6300,6400,6500,6600,6700,6800,6900]
fourteenth_mers = fourteenth_sequence_component(sixth_mers,sumx6)

##Comparision
print('Sequence for Original Sequence',first_mers[6000:7000:100])
print('Sequence for Sixth Sequence',sixth_mers[6000:7000:100])
print('Sequence for Fourteenth Sequence',fourteenth_mers[6000:7000:100])


# In[14]:


def seventh_sequence(first_mers):
    n = 7000
    seventh_mers = first_mers
    for sequence in list(seventh_mers[n]):
        if sequence == 'A':
            seventh_mers = seventh_mers[0:7000]+'G'+ seventh_mers[7001:]
             
        elif sequence =='G':
            seventh_mers = seventh_mers[0:7000]+'A'+ seventh_mers[7001:]
        elif sequence =='C':
            seventh_mers = seventh_mers[0:7000]+'T'+ seventh_mers[7001:]
        else:
            seventh_mers = seventh_mers[0:7000]+'C'+ seventh_mers[7001:]
            
    return seventh_mers
        

seventh_mers = seventh_sequence(first_mers)


##Comparision
print('Sequence for Original Sequence',first_mers[7000:8000:100])
print('Sequence for Seventh Sequence',seventh_mers[7000:8000:100])


# In[15]:


def fifteenth_sequence_component(seventh_mers, sumx7):
    fifteenth_mers = seventh_mers
    for n in sumx7:
        for sequence in list(fifteenth_mers[7100]):
            if sequence == 'A':
                fifteenth_mers = fifteenth_mers[0:7100]+'G'+ fifteenth_mers[7101:]
             
            elif sequence =='G':
                fifteenth_mers = fifteenth_mers[0:7100]+'A'+ fifteenth_mers[7101:]
            elif sequence =='C':
                fifteenth_mers = fifteenth_mers[0:7100]+'T'+ fifteenth_mers[7101:]
            elif sequence =='T':
                fifteenth_mers = fifteenth_mers[0:7100]+'C'+ fifteenth_mers[7101:]
            else:
                print('NO')
         
    for sequence in list(fifteenth_mers[7200]):
            if sequence == 'A':
                fifteenth_mers = fifteenth_mers[0:7200]+'G'+ fifteenth_mers[7201:]
             
            elif sequence =='G':
                fifteenth_mers = fifteenth_mers[0:7200]+'A'+ fifteenth_mers[7201:]
            elif sequence =='C':
                fifteenth_mers = fifteenth_mers[0:7200]+'T'+ fifteenth_mers[7201:]
            elif sequence =='T':
                fifteenth_mers = fifteenth_mers[0:7200]+'C'+ fifteenth_mers[7201:]
            else:
                print('NO')   
    
    
    
    for sequence in list(fifteenth_mers[7300]):
            if sequence == 'A':
                fifteenth_mers = fifteenth_mers[0:7300]+'G'+ fifteenth_mers[7301:]
             
            elif sequence =='G':
                fifteenth_mers = fifteenth_mers[0:7300]+'A'+ fifteenth_mers[7301:]
            elif sequence =='C':
                fifteenth_mers = fifteenth_mers[0:7300]+'T'+ fifteenth_mers[7301:]
            elif sequence =='T':
                fifteenth_mers = fifteenth_mers[0:7300]+'C'+ fifteenth_mers[7301:]
            else:
                print('NO')
    
    
    for sequence in list(fifteenth_mers[7400]):
            if sequence == 'A':
                fifteenth_mers = fifteenth_mers[0:7400]+'G'+ fifteenth_mers[7401:]
             
            elif sequence =='G':
                fifteenth_mers = fifteenth_mers[0:7400]+'A'+ fifteenth_mers[7401:]
            elif sequence =='C':
                fifteenth_mers = fifteenth_mers[0:7400]+'T'+ fifteenth_mers[7401:]
            elif sequence =='T':
                fifteenth_mers = fifteenth_mers[0:7400]+'C'+ fifteenth_mers[7401:]
            else:
                print('NO')
                
                
    for sequence in list(fifteenth_mers[7500]):
            if sequence == 'A':
                fifteenth_mers = fifteenth_mers[0:7500]+'G'+ fifteenth_mers[7501:]
             
            elif sequence =='G':
                fifteenth_mers = fifteenth_mers[0:7500]+'A'+ fifteenth_mers[7501:]
            elif sequence =='C':
                fifteenth_mers = fifteenth_mers[0:7500]+'T'+ fifteenth_mers[7501:]
            elif sequence =='T':
                fifteenth_mers = fifteenth_mers[0:7500]+'C'+ fifteenth_mers[7501:]
            else:
                print('NO')            
    
    
    for sequence in list(fifteenth_mers[7600]):
            if sequence == 'A':
                fifteenth_mers = fifteenth_mers[0:7600]+'G'+ fifteenth_mers[7601:]
             
            elif sequence =='G':
                fifteenth_mers = fifteenth_mers[0:7600]+'A'+ fifteenth_mers[7601:]
            elif sequence =='C':
                fifteenth_mers = fifteenth_mers[0:7600]+'T'+ fifteenth_mers[7601:]
            elif sequence =='T':
                fifteenth_mers = fifteenth_mers[0:7600]+'C'+ fifteenth_mers[7601:]
            else:
                print('NO')
    
    
    for sequence in list(fifteenth_mers[7700]):
            if sequence == 'A':
                fifteenth_mers = fifteenth_mers[0:7700]+'G'+ fifteenth_mers[7701:]
             
            elif sequence =='G':
                fifteenth_mers = fifteenth_mers[0:7700]+'A'+ fifteenth_mers[7701:]
            elif sequence =='C':
                fifteenth_mers = fifteenth_mers[0:7700]+'T'+ fifteenth_mers[7701:]
            elif sequence =='T':
                fifteenth_mers = fifteenth_mers[0:7700]+'C'+ fifteenth_mers[7701:]
            else:
                print('NO')
    
    
    for sequence in list(fifteenth_mers[7800]):
            if sequence == 'A':
                fifteenth_mers = fifteenth_mers[0:7800]+'G'+ fifteenth_mers[7801:]
             
            elif sequence =='G':
                fifteenth_mers = fifteenth_mers[0:7800]+'A'+ fifteenth_mers[7801:]
            elif sequence =='C':
                fifteenth_mers = fifteenth_mers[0:7800]+'T'+ fifteenth_mers[7801:]
            elif sequence =='T':
                fifteenth_mers = fifteenth_mers[0:7800]+'C'+ fifteenth_mers[7801:]
            else:
                print('NO')
                
                
    for sequence in list(fifteenth_mers[7900]):
            if sequence == 'A':
                fifteenth_mers = fifteenth_mers[0:7900]+'G'+ fifteenth_mers[7901:]
             
            elif sequence =='G':
                fifteenth_mers = fifteenth_mers[0:7900]+'A'+ fifteenth_mers[7901:]
            elif sequence =='C':
                fifteenth_mers = fifteenth_mers[0:7900]+'T'+ fifteenth_mers[7901:]
            elif sequence =='T':
                fifteenth_mers = fifteenth_mers[0:7900]+'C'+ fifteenth_mers[7901:]
            else:
                print('NO')            
    
    return fifteenth_mers
    
    
    
    
sumx7 = [7100,7200,7300,7400,7500,7600,7700,7800,7900]
fifteenth_mers = fifteenth_sequence_component(seventh_mers,sumx7)

##Comparision
print('Sequence for Original Sequence',first_mers[7000:8000:100])
print('Sequence for Seventh Sequence',seventh_mers[7000:8000:100])
print('Sequence for Fifteenth Sequence',fifteenth_mers[7000:8000:100])


# In[16]:


def eighth_sequence(first_mers):
    n = 8000
    eighth_mers = first_mers
    for sequence in list(eighth_mers[n]):
        if sequence == 'A':
            eighth_mers = eighth_mers[0:8000]+'G'+ eighth_mers[8001:]
             
        elif sequence =='G':
            eighth_mers = eighth_mers[0:8000]+'A'+ eighth_mers[8001:]
        elif sequence =='C':
            eighth_mers = eighth_mers[0:8000]+'T'+ eighth_mers[8001:]
        else:
            eighth_mers = eighth_mers[0:8000]+'C'+ eighth_mers[8001:]
            
    return eighth_mers
        

eighth_mers = eighth_sequence(first_mers)


##Comparision
print('Sequence for Original Sequence',first_mers[8000:9000:100])
print('Sequence for Eighth Sequence',eighth_mers[8000:9000:100])


# In[17]:


def sixteenth_sequence_component(eighth_mers, sumx8):
    sixteenth_mers = eighth_mers
    for n in sumx8:
        for sequence in list(sixteenth_mers[8100]):
            if sequence == 'A':
                sixteenth_mers = sixteenth_mers[0:8100]+'G'+ sixteenth_mers[8101:]
             
            elif sequence =='G':
                sixteenth_mers = sixteenth_mers[0:8100]+'A'+ sixteenth_mers[8101:]
            elif sequence =='C':
                sixteenth_mers = sixteenth_mers[0:8100]+'T'+ sixteenth_mers[8101:]
            elif sequence =='T':
                sixteenth_mers = sixteenth_mers[0:8100]+'C'+ sixteenth_mers[8101:]
            else:
                print('NO')
         
    for sequence in list(sixteenth_mers[8200]):
            if sequence == 'A':
                sixteenth_mers = sixteenth_mers[0:8200]+'G'+ sixteenth_mers[8201:]
             
            elif sequence =='G':
                sixteenth_mers = sixteenth_mers[0:8200]+'A'+ sixteenth_mers[8201:]
            elif sequence =='C':
                sixteenth_mers = sixteenth_mers[0:8200]+'T'+ sixteenth_mers[8201:]
            elif sequence =='T':
                sixteenth_mers = sixteenth_mers[0:8200]+'C'+ sixteenth_mers[8201:]
            else:
                print('NO')
    
    
    for sequence in list(sixteenth_mers[8300]):
            if sequence == 'A':
                sixteenth_mers = sixteenth_mers[0:8300]+'G'+ sixteenth_mers[8301:]
             
            elif sequence =='G':
                sixteenth_mers = sixteenth_mers[0:8300]+'A'+ sixteenth_mers[8301:]
            elif sequence =='C':
                sixteenth_mers = sixteenth_mers[0:8300]+'T'+ sixteenth_mers[8301:]
            elif sequence =='T':
                sixteenth_mers = sixteenth_mers[0:8300]+'C'+ sixteenth_mers[8301:]
            else:
                print('NO')
    
    for sequence in list(sixteenth_mers[8400]):
            if sequence == 'A':
                sixteenth_mers = sixteenth_mers[0:8400]+'G'+ sixteenth_mers[8401:]
             
            elif sequence =='G':
                sixteenth_mers = sixteenth_mers[0:8400]+'A'+ sixteenth_mers[8401:]
            elif sequence =='C':
                sixteenth_mers = sixteenth_mers[0:8400]+'T'+ sixteenth_mers[8401:]
            elif sequence =='T':
                sixteenth_mers = sixteenth_mers[0:8400]+'C'+ sixteenth_mers[8401:]
            else:
                print('NO')
    
    
    for sequence in list(sixteenth_mers[8500]):
            if sequence == 'A':
                sixteenth_mers = sixteenth_mers[0:8500]+'G'+ sixteenth_mers[8501:]
             
            elif sequence =='G':
                sixteenth_mers = sixteenth_mers[0:8500]+'A'+ sixteenth_mers[8501:]
            elif sequence =='C':
                sixteenth_mers = sixteenth_mers[0:8500]+'T'+ sixteenth_mers[8501:]
            elif sequence =='T':
                sixteenth_mers = sixteenth_mers[0:8500]+'C'+ sixteenth_mers[8501:]
            else:
                print('NO')
    
    
    for sequence in list(sixteenth_mers[8600]):
            if sequence == 'A':
                sixteenth_mers = sixteenth_mers[0:8600]+'G'+ sixteenth_mers[8601:]
             
            elif sequence =='G':
                sixteenth_mers = sixteenth_mers[0:8600]+'A'+ sixteenth_mers[8601:]
            elif sequence =='C':
                sixteenth_mers = sixteenth_mers[0:8600]+'T'+ sixteenth_mers[8601:]
            elif sequence =='T':
                sixteenth_mers = sixteenth_mers[0:8600]+'C'+ sixteenth_mers[8601:]
            else:
                print('NO')
    
    for sequence in list(sixteenth_mers[8700]):
            if sequence == 'A':
                sixteenth_mers = sixteenth_mers[0:8700]+'G'+ sixteenth_mers[8701:]
             
            elif sequence =='G':
                sixteenth_mers = sixteenth_mers[0:8700]+'A'+ sixteenth_mers[8701:]
            elif sequence =='C':
                sixteenth_mers = sixteenth_mers[0:8700]+'T'+ sixteenth_mers[8701:]
            elif sequence =='T':
                sixteenth_mers = sixteenth_mers[0:8700]+'C'+ sixteenth_mers[8701:]
            else:
                print('NO')
    
    
    for sequence in list(sixteenth_mers[8800]):
            if sequence == 'A':
                sixteenth_mers = sixteenth_mers[0:8800]+'G'+ sixteenth_mers[8801:]
             
            elif sequence =='G':
                sixteenth_mers = sixteenth_mers[0:8800]+'A'+ sixteenth_mers[8801:]
            elif sequence =='C':
                sixteenth_mers = sixteenth_mers[0:8800]+'T'+ sixteenth_mers[8801:]
            elif sequence =='T':
                sixteenth_mers = sixteenth_mers[0:8800]+'C'+ sixteenth_mers[8801:]
            else:
                print('NO')
    
    for sequence in list(sixteenth_mers[8900]):
            if sequence == 'A':
                sixteenth_mers = sixteenth_mers[0:8900]+'G'+ sixteenth_mers[8901:]
             
            elif sequence =='G':
                sixteenth_mers = sixteenth_mers[0:8900]+'A'+ sixteenth_mers[8901:]
            elif sequence =='C':
                sixteenth_mers = sixteenth_mers[0:8900]+'T'+ sixteenth_mers[8901:]
            elif sequence =='T':
                sixteenth_mers = sixteenth_mers[0:8900]+'C'+ sixteenth_mers[8901:]
            else:
                print('NO')
    
    return sixteenth_mers
    
    
    
    
sumx8 = [8100,8200,8300,8400,8500,8600,8700,8800,8900]
sixteenth_mers = sixteenth_sequence_component(eighth_mers,sumx8)

##Comparision
print('Sequence for Original Sequence',first_mers[8000:9000:100])
print('Sequence for Eighth Sequence',eighth_mers[8000:9000:100])
print('Sequence for Sixteenth Sequence',sixteenth_mers[8000:9000:100])


# In[18]:


def nineth_sequence(first_mers):
    n = 9000
    nineth_mers = first_mers
    for sequence in list(nineth_mers[n]):
        if sequence == 'A':
            nineth_mers = nineth_mers[0:9000]+'G'+ nineth_mers[9001:]
             
        elif sequence =='G':
            nineth_mers = nineth_mers[0:9000]+'A'+ nineth_mers[9001:]
        elif sequence =='C':
            nineth_mers = nineth_mers[0:9000]+'T'+ nineth_mers[9001:]
        else:
            nineth_mers = nineth_mers[0:9000]+'C'+ nineth_mers[9001:]
            
    return nineth_mers
        

nineth_mers = nineth_sequence(first_mers)


##Comparision
print('Sequence for Original Sequence',first_mers[9000:10000:100])
print('Sequence for Nineth Sequence',nineth_mers[9000:10000:100])


# In[19]:


def seventeenth_sequence_component(nineth_mers, sumx9):
    seventeenth_mers = nineth_mers
    for n in sumx9:
        for sequence in list(seventeenth_mers[9100]):
            if sequence == 'A':
                seventeenth_mers = seventeenth_mers[0:9100]+'G'+ seventeenth_mers[9101:]
             
            elif sequence =='G':
                seventeenth_mers = seventeenth_mers[0:9100]+'A'+ seventeenth_mers[9101:]
            elif sequence =='C':
                seventeenth_mers = seventeenth_mers[0:9100]+'T'+ seventeenth_mers[9101:]
            elif sequence =='T':
                seventeenth_mers = seventeenth_mers[0:9100]+'C'+ seventeenth_mers[9101:]
            else:
                print('NO')
         
    for sequence in list(seventeenth_mers[9200]):
            if sequence == 'A':
                seventeenth_mers = seventeenth_mers[0:9200]+'G'+ seventeenth_mers[9201:]
             
            elif sequence =='G':
                seventeenth_mers = seventeenth_mers[0:9200]+'A'+ seventeenth_mers[9201:]
            elif sequence =='C':
                seventeenth_mers = seventeenth_mers[0:9200]+'T'+ seventeenth_mers[9201:]
            elif sequence =='T':
                seventeenth_mers = seventeenth_mers[0:9200]+'C'+ seventeenth_mers[9201:]
            else:
                print('NO')
                
                
    for sequence in list(seventeenth_mers[9300]):
            if sequence == 'A':
                seventeenth_mers = seventeenth_mers[0:9300]+'G'+ seventeenth_mers[9301:]
             
            elif sequence =='G':
                seventeenth_mers = seventeenth_mers[0:9300]+'A'+ seventeenth_mers[9301:]
            elif sequence =='C':
                seventeenth_mers = seventeenth_mers[0:9300]+'T'+ seventeenth_mers[9301:]
            elif sequence =='T':
                seventeenth_mers = seventeenth_mers[0:9300]+'C'+ seventeenth_mers[9301:]
            else:
                print('NO')            
                
    for sequence in list(seventeenth_mers[9400]):
            if sequence == 'A':
                seventeenth_mers = seventeenth_mers[0:9400]+'G'+ seventeenth_mers[9401:]
             
            elif sequence =='G':
                seventeenth_mers = seventeenth_mers[0:9400]+'A'+ seventeenth_mers[9401:]
            elif sequence =='C':
                seventeenth_mers = seventeenth_mers[0:9400]+'T'+ seventeenth_mers[9401:]
            elif sequence =='T':
                seventeenth_mers = seventeenth_mers[0:9400]+'C'+ seventeenth_mers[9401:]
            else:
                print('NO')            
                
    for sequence in list(seventeenth_mers[9500]):
            if sequence == 'A':
                seventeenth_mers = seventeenth_mers[0:9500]+'G'+ seventeenth_mers[9501:]
             
            elif sequence =='G':
                seventeenth_mers = seventeenth_mers[0:9500]+'A'+ seventeenth_mers[9501:]
            elif sequence =='C':
                seventeenth_mers = seventeenth_mers[0:9500]+'T'+ seventeenth_mers[9501:]
            elif sequence =='T':
                seventeenth_mers = seventeenth_mers[0:9500]+'C'+ seventeenth_mers[9501:]
            else:
                print('NO')  
                
                
                
    for sequence in list(seventeenth_mers[9600]):
            if sequence == 'A':
                seventeenth_mers = seventeenth_mers[0:9600]+'G'+ seventeenth_mers[9601:]
             
            elif sequence =='G':
                seventeenth_mers = seventeenth_mers[0:9600]+'A'+ seventeenth_mers[9601:]
            elif sequence =='C':
                seventeenth_mers = seventeenth_mers[0:9600]+'T'+ seventeenth_mers[9601:]
            elif sequence =='T':
                seventeenth_mers = seventeenth_mers[0:9600]+'C'+ seventeenth_mers[9601:]
            else:
                print('NO')     
                
                
    for sequence in list(seventeenth_mers[9700]):
            if sequence == 'A':
                seventeenth_mers = seventeenth_mers[0:9700]+'G'+ seventeenth_mers[9701:]
             
            elif sequence =='G':
                seventeenth_mers = seventeenth_mers[0:9700]+'A'+ seventeenth_mers[9701:]
            elif sequence =='C':
                seventeenth_mers = seventeenth_mers[0:9700]+'T'+ seventeenth_mers[9701:]
            elif sequence =='T':
                seventeenth_mers = seventeenth_mers[0:9700]+'C'+ seventeenth_mers[9701:]
            else:
                print('NO')            
                
    for sequence in list(seventeenth_mers[9800]):
            if sequence == 'A':
                seventeenth_mers = seventeenth_mers[0:9800]+'G'+ seventeenth_mers[9801:]
             
            elif sequence =='G':
                seventeenth_mers = seventeenth_mers[0:9800]+'A'+ seventeenth_mers[9801:]
            elif sequence =='C':
                seventeenth_mers = seventeenth_mers[0:9800]+'T'+ seventeenth_mers[9801:]
            elif sequence =='T':
                seventeenth_mers = seventeenth_mers[0:9800]+'C'+ seventeenth_mers[9801:]
            else:
                print('NO')
    
    for sequence in list(seventeenth_mers[9900]):
            if sequence == 'A':
                seventeenth_mers = seventeenth_mers[0:9900]+'G'+ seventeenth_mers[9901:]
             
            elif sequence =='G':
                seventeenth_mers = seventeenth_mers[0:9100]+'A'+ seventeenth_mers[9101:]
            elif sequence =='C':
                seventeenth_mers = seventeenth_mers[0:9900]+'T'+ seventeenth_mers[9901:]
            elif sequence =='T':
                seventeenth_mers = seventeenth_mers[0:9900]+'C'+ seventeenth_mers[9901:]
            else:
                print('NO')
    
    return seventeenth_mers
    
    
    
    
sumx9 = [9100,9200,9300,9400,9500,9600,9700,9800,9900]
seventeenth_mers = seventeenth_sequence_component(nineth_mers,sumx9)

##Comparision
print('Sequence for Original Sequence',first_mers[9000:10000:100])
print('Sequence for Nineth Sequence',nineth_mers[9000:10000:100])
print('Sequence for Seventeenth Sequence',seventeenth_mers[9000:10000:100])
