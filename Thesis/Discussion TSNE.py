#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.manifold import TSNE
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


time_start = time.time()
tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
tsne_results_1 = tsne.fit_transform(X)


# In[12]:


dfnew['TSNE-2D-1'] = tsne_results_1[:,0]
dfnew['TSNE-2D-2'] = tsne_results_1[:,1]

X1 =  tsne_results_1[:,0]
Y1 = tsne_results_1[:,1] 
    
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




plt.figure(figsize=(32,18))
plt.scatter(X1, Y1,s=30,color="red")
plt.xlabel("TSNE-2D-1", fontsize = 40)
plt.ylabel("TSNE-2D-2", fontsize = 40)
#plt.title("1T - 8 identical MERS sequence",fontsize=16)
for i, label in enumerate(annotations):
    plt.annotate(label, (X1[i], Y1[i]), fontsize = 20)

plt.savefig('TSNE_Comparison.png')
plt.show()

