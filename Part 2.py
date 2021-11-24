#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from collections import defaultdict
from sklearn.decomposition import PCA
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plot

data = pd.read_csv('Genome_3mer.csv')

del data['Unnamed: 0']

data


# In[ ]:





# In[2]:


series = data.squeeze()
series


# In[3]:


series = series.str.split(",", expand = True)
series


# In[4]:


df = pd.DataFrame(series)
df


# In[ ]:





# In[5]:


##replace none with 0
df = df.drop_duplicates()
df = df.fillna(0)
df = df.replace("[]","0")
df = df.dropna()
df


# In[6]:


columns = df[0]
pd.set_option('display.max_rows', columns.shape[0]+1)
columns


# In[7]:


idx = pd.Index(df[0])
idx = idx[1:183]
idx


# In[8]:


##delete first row 
df = df.iloc[1: , :]
##delete first column
test_df = df.iloc[: , 1:]

test_df = pd.DataFrame(test_df)
test_df


# In[9]:


freq_df = pd.DataFrame(index = test_df.index, columns = test_df.stack().unique())
freq_df


# In[10]:


for i in test_df.index:
    freq_df.loc[i] = test_df.loc[i].value_counts()


# In[11]:


freq_df = freq_df.fillna(0)
freq_df


# In[12]:


##sum needs to be greater than the number of rows
freq_df = freq_df[freq_df.columns[freq_df.sum()>182]]
freq_df


# In[13]:


freq_df.index = idx

freq_df


# In[14]:


freq_df = freq_df[~freq_df.index.duplicated(keep='first')]
freq_df


# In[15]:


##notice that last one is 0 hence delete it!
freq_df = freq_df.iloc[:, :-1]
freq_df


# In[16]:


freq_df = freq_df.reindex(sorted(freq_df.columns), axis=1)
freq_df


# In[17]:


df = freq_df.apply(lambda x: x/sum(x), axis=1)
df


# In[18]:


# perform PCA analysis
pca = PCA(n_components=10)
principalComponents = pca.fit_transform(df)

principalDf = pd.DataFrame(data = principalComponents, columns=list(range(1,11)), index=df.index)

# plot the first two componenents
principalDf.plot.scatter(x=1, y=2)

