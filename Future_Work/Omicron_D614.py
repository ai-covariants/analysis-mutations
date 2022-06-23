#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# In[2]:


def pca(data):
    del data['Unnamed: 0']
    X = data.drop(['target'], axis = 1)
    target = data['target']
    x = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2)
    PC = pca.fit_transform(x)
    PDF = pd.DataFrame(data = PC,columns = ['Principal Component 1', 'Principal Component 2'])
    FDF = pd.concat([PDF, data['target']], axis = 1)
    print('Variance of each component:', pca.explained_variance_ratio_)
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1 (97.0%)', fontsize = 18)
    ax.set_ylabel('Principal Component 2 (1.3%)', fontsize = 18)
    ax.set_title('Principal Component Analysis', fontsize = 20)
    targets = ['D614','Omicron']
    colors = ['r','b']
    for target, color in zip(targets,colors):
        indicesToKeep = FDF['target'] == target
        ax.scatter(FDF.loc[indicesToKeep, 'Principal Component 1']
               , FDF.loc[indicesToKeep, 'Principal Component 2']
               , c = color
               , s = 40)
    ax.legend(targets)
    plt.savefig('PCA.png')
    
    

data = pd.read_csv('selected_covid_data.csv')
pca(data)


# In[ ]:





# In[ ]:




