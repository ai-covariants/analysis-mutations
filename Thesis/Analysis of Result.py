#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pysam import FastaFile
from matplotlib import pyplot as plt
from itertools import product
from Bio import SeqIO
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plot
import numpy as np
import plotly.express as px
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy.linalg import eigh


mers = pd.read_csv('mers_kmer.csv')
mers


# In[2]:


mm = {'Strain':['MERS:JX869059.2','MERS:KF600612.1','MERS:KC776174.1',
                'MERS:KP209307.1','MERS:KY673148.1','MERS:KF600630.1',
               'MERS:MN723542.1','MERS:KF186564.1']}
mm = pd.DataFrame(mm,columns=['Strain'])
mmd = pd.concat([mm], ignore_index=True)

m = [mers, mmd]
mers = pd.concat(m, axis = 1)
del mers['Unnamed: 0']
mers


# In[3]:


omicron = pd.read_csv('omicron_kmer.csv')
omicron


# In[4]:


o = {'Strain':['Omicron:USA/UT-UPHL-211211887190','Omicron:Switzerland/BL-ETHZ-35009242',
              'Omicron:Israel/ICH-760598216','Omicron:India/DL-GSLLNH',
               'Omicron:Botswana/R44B41_BHP_00084864','Omicron:Germany/HE-RKI-I-385980',
              'Omicron:Spain/IB-HUSE-03236','Omicron:France/IDF-HMN-21122210612/2021']}
o = pd.DataFrame(o,columns=['Strain'])
o = pd.concat([o], ignore_index=True)
m = [omicron, o]
omicron = pd.concat(m, axis = 1)
del omicron['Unnamed: 0']
omicron


# In[5]:


wuhan = pd.read_csv('wuhan_kmer.csv')
wuhan


# In[6]:


ww = {'Strain':['Wuhan-HU-1']}
ww = pd.DataFrame(ww,columns=['Strain'])
dd = pd.concat([ww]*1, ignore_index=True)

w = [wuhan, dd]
wuhan = pd.concat(w, axis = 1)
del wuhan['Unnamed: 0']
wuhan


# In[7]:


gamma = pd.read_csv('gamma_kmer.csv')
gamma


# In[8]:


gg = {'Strain':['Gamma:EPI_ISL_3842262','Gamma:EPI_ISL_5645882','Gamma:EPI_ISL_3983576',
               'Gamma:EPI_ISL_4415922','Gamma:EPI_ISL_2756234','Gamma:EPI_ISL_4422674',
               'Gamma:EPI_ISL_4417797','Gamma:EPI_ISL_2344540']}
gg = pd.DataFrame(gg,columns=['Strain'])
dg = pd.concat([gg]*1, ignore_index=True)

g = [gamma, dg]
gamma = pd.concat(g, axis = 1)
del gamma['Unnamed: 0']
gamma


# In[9]:


new = [mers, omicron, wuhan,gamma]
dfnew = pd.concat(new)
dfnew = dfnew.reset_index(drop=True)
dfnew


# In[10]:


target = dfnew['Strain']

X = dfnew.drop(['Strain'], axis = 1)


# In[11]:


pca=PCA(n_components=2) 
pca_data =pca.fit_transform(X) 
print('shape of PCA data',pca_data.shape)


# In[12]:


X_to = pca_data[:, 0]
Y_to = pca_data[:, 1]
plt.rcParams['font.size'] = '60'
plt.figure(figsize=(60,40))
plt.scatter(X_to, Y_to,s=200,color="orange")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
#plt.savefig('PCA_Comparision.png')
plt.savefig('PCA_Comparision.png')
plt.show()


# In[13]:


##with annotation
annotations=['MERS:JX869059.2','MERS:KF600612.1','MERS:KC776174.1',
                'MERS:KP209307.1','MERS:KY673148.1','MERS:KF600630.1',
               'MERS:MN723542.1','MERS:KF186564.1',
            'Omicron:USA/UT-UPHL-211211887190','Omicron:Switzerland/BL-ETHZ-35009242',
              'Omicron:Israel/ICH-760598216','Omicron:India/DL-GSLLNH',
               'Omicron:Botswana/R44B41_BHP_00084864','Omicron:Germany/HE-RKI-I-385980',
              'Omicron:Spain/IB-HUSE-03236','Omicron:France/IDF-HMN-21122210612/2021',
            'Wuhan-HU-1','Gamma:EPI_ISL_3842262','Gamma:EPI_ISL_5645882','Gamma:EPI_ISL_3983576',
               'Gamma:EPI_ISL_4415922','Gamma:EPI_ISL_2756234','Gamma:EPI_ISL_4422674',
               'Gamma:EPI_ISL_4417797','Gamma:EPI_ISL_2344540']

X_to = pca_data[:, 0]
Y_to = pca_data[:, 1]

plt.figure(figsize=(100,100))
plt.scatter(X_to, Y_to,s=1000,color="orange")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
for i, label in enumerate(annotations):
    plt.annotate(label, (X_to[i], Y_to[i]), fontsize = 50,ha='left',
            va='baseline')
#plt.savefig('PCA_Comparision.png')
plt.show()

