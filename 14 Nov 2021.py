#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.linalg import eigh


data = pd.read_csv('dictionary_edited.csv')
data


# In[2]:


y = data['target']
X = data.drop(['target'], axis = 1)
X 


# In[3]:


##scale the input
ss = StandardScaler()
ss_df = ss.fit_transform(X)
ss_df.shape


# In[4]:


##covariance and its dimension
covariance_matrix = np.matmul(ss_df.T, ss_df)
covariance_matrix.shape


# In[5]:


##dimension of eigenvector
values, vectors = eigh(covariance_matrix, eigvals = (62,63))
print("Dimensions of Eigenvector:", vectors.shape)


# In[6]:


##dimension of eigenvector transpose
vectors = vectors.T
print("Dimensions of Eigenvector(Tranpose):", vectors.shape)


# In[7]:


df_final = np.matmul(vectors, ss_df.T)
print("vectros:", vectors.shape, "n", "ss_df:", ss_df.T.shape, "n", "final_df:", df_final.shape)


# In[8]:


##dataframe
finalTrans = np.vstack((df_final, y)).T
dataFrame = pd.DataFrame(finalTrans, columns = ['Principal Component 1', 'Principal Component 2', 'Target'])
dataFrame


# In[9]:


##plot 
sns.FacetGrid(dataFrame, hue = 'Target', size = 8).map(sns.scatterplot, 'Principal Component 2', 'Principal Component 2').add_legend()
plt.show()

