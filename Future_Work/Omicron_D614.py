#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
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
    plt.rcParams['font.size'] = 20
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1 (97.0%)')
    ax.set_ylabel('Principal Component 2 (1.3%)')
    ax.set_title('Principal Component Analysis')
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


# In[3]:


def pca(data5):
    del data5['Unnamed: 0']
    X5 = data5.drop(['target'], axis = 1)
    target5 = data5['target']
    x5 = StandardScaler().fit_transform(X5)
    pca5 = PCA(n_components=2)
    PC5 = pca5.fit_transform(x5)
    PDF5 = pd.DataFrame(data = PC5,columns = ['Principal Component 1', 'Principal Component 2'])
    FDF5 = pd.concat([PDF5, data['target']], axis = 1)
    print('Variance of each component:', pca5.explained_variance_ratio_)
    fig = plt.figure(figsize = (10,10))
    plt.rcParams['font.size'] = 20
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1 (72.0%)')
    ax.set_ylabel('Principal Component 2 (3.4%)')
    ax.set_title('Principal Component Analysis')
    targets = ['D614','Omicron']
    colors = ['r','b']
    for target, color in zip(targets,colors):
        indicesToKeep = FDF5['target'] == target
        ax.scatter(FDF5.loc[indicesToKeep, 'Principal Component 1']
               , FDF5.loc[indicesToKeep, 'Principal Component 2']
               , c = color
               , s = 40)
    ax.legend(targets)
    plt.savefig('PCA5.png')
    
    

data5 = pd.read_csv('selected_covid_data5.csv')
pca(data5)


# In[4]:


def pca(data7):
    del data7['Unnamed: 0']
    X7 = data7.drop(['target'], axis = 1)
    target7 = data7['target']
    x7 = StandardScaler().fit_transform(X7)
    pca7 = PCA(n_components=2)
    PC7 = pca7.fit_transform(x7)
    PDF7 = pd.DataFrame(data = PC7,columns = ['Principal Component 1', 'Principal Component 2'])
    FDF7 = pd.concat([PDF7, data['target']], axis = 1)
    print('Variance of each component:', pca7.explained_variance_ratio_)
    fig = plt.figure(figsize = (10,10))
    plt.rcParams['font.size'] = 20
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1 (28.1%)')
    ax.set_ylabel('Principal Component 2 (7.4%)')
    ax.set_title('Principal Component Analysis')
    targets = ['D614','Omicron']
    colors = ['r','b']
    for target, color in zip(targets,colors):
        indicesToKeep = FDF7['target'] == target
        ax.scatter(FDF7.loc[indicesToKeep, 'Principal Component 1']
               , FDF7.loc[indicesToKeep, 'Principal Component 2']
               , c = color
               , s = 40)
    ax.legend(targets)
    plt.savefig('PCA7.png')
    
    

data7 = pd.read_csv('selected_covid_data7.csv')
pca(data7)


# In[5]:


def pca_plot(data,data5,data7):
    X = data.drop(['target'], axis = 1)
    target = data['target']
    x = StandardScaler().fit_transform(X)
    pca = PCA(n_components = 10)
    PC = pca.fit_transform(x)
    print('Variance of each component:', pca.explained_variance_ratio_)
    X5 = data5.drop(['target'], axis = 1)
    target5 = data5['target']
    x5 = StandardScaler().fit_transform(X5)
    pca5 = PCA(n_components= 10)
    PC5 = pca5.fit_transform(x5)
    print('Variance of each component:', pca5.explained_variance_ratio_)
    X7 = data7.drop(['target'], axis = 1)
    target7 = data7['target']
    x7 = StandardScaler().fit_transform(X7)
    pca7 = PCA(n_components=10)
    PC7 = pca7.fit_transform(x7)
    print('Variance of each component:', pca7.explained_variance_ratio_)
    fig = plt.figure(figsize = (10,10))
    plt.rcParams['font.size'] = 20
    PC_values = np.arange(pca.n_components_) + 1
    plt.plot(PC_values, pca.explained_variance_ratio_, 'h-', linewidth=2, color='purple')

    PC_values5 = np.arange(pca5.n_components_) + 1
    plt.plot(PC_values5, pca5.explained_variance_ratio_, '*-', linewidth=2, color='red')

    PC_values7 = np.arange(pca7.n_components_) + 1
    plt.plot(PC_values7, pca7.explained_variance_ratio_, 'o-', linewidth=2, color='blue')
    plt.title('Scree Plot')
    plt.xlabel('Number of Principal Components')
    plt.ylabel('Proportion of Variance Explained')
    plt.savefig('Screeplot.png')
    
    
    
pca_plot(data,data5,data7)    

