#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

import umap.umap_ as umap
import plotly.express as px

from sklearn.manifold import TSNE
import time


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
    plt.rcParams['font.size'] = 18
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1 (53.3%)')
    ax.set_ylabel('Principal Component 2 (7.7%)')
    targets = ['Alpha','Beta','Delta','Gamma','Omicron']
    colors = ['r','b','g','m','c','k']
    for target, color in zip(targets,colors):
        indicesToKeep = FDF['target'] == target
        ax.scatter(FDF.loc[indicesToKeep, 'Principal Component 1']
               , FDF.loc[indicesToKeep, 'Principal Component 2']
               , c = color
               , s = 40
                )
    ax.legend(targets, loc ='best')
    plt.savefig('PCA_covid.png')
    
    

data = pd.read_csv('covid_data.csv')
pca(data)

#ax.set_title('Principal Component Analysis')


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
    ax.set_xlabel('Principal Component 1 (16.9%)')
    ax.set_ylabel('Principal Component 2 (8.8%)')
    targets = ['Alpha','Beta','Delta','Gamma','Omicron']
    colors = ['r','b','g','m','c','k']
    for target, color in zip(targets,colors):
        indicesToKeep = FDF5['target'] == target
        ax.scatter(FDF5.loc[indicesToKeep, 'Principal Component 1']
               , FDF5.loc[indicesToKeep, 'Principal Component 2']
               , c = color
               , s = 40)
    ax.legend(targets)
    plt.savefig('PCA_COVID5.png')
    
    

data5 = pd.read_csv('covid_data5.csv')
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
    ax.set_xlabel('Principal Component 1 (6.5%)')
    ax.set_ylabel('Principal Component 2 (3.8%)')
    targets = ['Alpha','Beta','Delta','Gamma','Omicron']
    colors = ['r','b','g','m','c','k']
    for target, color in zip(targets,colors):
        indicesToKeep = FDF7['target'] == target
        ax.scatter(FDF7.loc[indicesToKeep, 'Principal Component 1']
               , FDF7.loc[indicesToKeep, 'Principal Component 2']
               , c = color
               , s = 40)
    ax.legend(targets)
    plt.savefig('PCA_COVID7.png')
    
    

data7 = pd.read_csv('covid_data7.csv')
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
    plt.xlabel('Number of Principal Components')
    plt.ylabel('Proportion of Variance Explained')
    plt.savefig('Screeplot.png')
    
    
    
pca_plot(data,data5,data7)    


# In[6]:


def umap_fn(data):
    X = data.drop(['target'], axis = 1)
    target = data['target']
    umap_reduce = umap.UMAP()
    scaled_X = StandardScaler().fit_transform(X)
    emb = umap_reduce.fit_transform(scaled_X)
    emb.shape


    X_o = emb[:,0]
    Y_o = emb[:,1]


    umap_2d = px.scatter(
        emb, x= 0, y= 1,
        color=data.target, labels={'color': 'Strain'})

    umap_2d.update_layout(
    xaxis_title="UMAP_1",
    yaxis_title="UMAP_2",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"))

    
    umap_2d.update_xaxes(showgrid=False,zeroline=False)
    umap_2d.update_yaxes(showgrid=False,zeroline=False)
    umap_2d.show()
    
    
umap_fn(data)    

#umap_2d.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})


# In[7]:


def umap_fn(data5):
    X = data5.drop(['target'], axis = 1)
    target = data5['target']
    umap_reduce = umap.UMAP()
    scaled_X = StandardScaler().fit_transform(X)
    emb = umap_reduce.fit_transform(scaled_X)
    emb.shape


    X_o = emb[:,0]
    Y_o = emb[:,1]


    umap_2d = px.scatter(
        emb, x= 0, y= 1,
        color=data5.target, labels={'color': 'Strain'})

    umap_2d.update_layout(
    xaxis_title="UMAP_1",
    yaxis_title="UMAP_2",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"))

    
    umap_2d.update_xaxes(showgrid=False,zeroline=False)
    umap_2d.update_yaxes(showgrid=False,zeroline=False)
    umap_2d.show()
    
    
umap_fn(data5) 


# In[8]:


def umap_fn(data7):
    X = data7.drop(['target'], axis = 1)
    target = data7['target']
    umap_reduce = umap.UMAP()
    scaled_X = StandardScaler().fit_transform(X)
    emb = umap_reduce.fit_transform(scaled_X)
    emb.shape


    X_o = emb[:,0]
    Y_o = emb[:,1]


    umap_2d = px.scatter(
        emb, x= 0, y= 1,
        color=data7.target, labels={'color': 'Strain'})

    umap_2d.update_layout(
    xaxis_title="UMAP_1",
    yaxis_title="UMAP_2",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"))

    
    umap_2d.update_xaxes(showgrid=False,zeroline=False)
    umap_2d.update_yaxes(showgrid=False,zeroline=False)
    umap_2d.show()
    
    
umap_fn(data7) 


# In[9]:


def tsne_fn(data):
    X = data.drop(['target'], axis = 1)
    target = data['target']
    time_start = time.time()
    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
    tsne_results_1 = tsne.fit_transform(X)
    
    
    fig = px.scatter(
    tsne_results_1, x=0, y=1,
    color=data.target, labels={'color': 'Strain'})


    fig.update_layout(
        xaxis_title="TSNE-2D-1",
        yaxis_title="TSNE-2D-2",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"))

    fig.update_xaxes(showgrid=False,zeroline=False)
    fig.update_yaxes(showgrid=False,zeroline=False)
    fig.show()
    
    

tsne_fn(data)    


# In[10]:


def tsne_fn(data5):
    X = data5.drop(['target'], axis = 1)
    target = data5['target']
    time_start = time.time()
    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
    tsne_results_1 = tsne.fit_transform(X)
    
    
    fig = px.scatter(
    tsne_results_1, x=0, y=1,
    color=data5.target, labels={'color': 'Strain'})


    fig.update_layout(
        xaxis_title="TSNE-2D-1",
        yaxis_title="TSNE-2D-2",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"))

    fig.update_xaxes(showgrid=False,zeroline=False)
    fig.update_yaxes(showgrid=False,zeroline=False)
    fig.show()
    
    

tsne_fn(data5)    


# In[11]:


def tsne_fn(data7):
    X = data7.drop(['target'], axis = 1)
    target = data7['target']
    time_start = time.time()
    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
    tsne_results_1 = tsne.fit_transform(X)
    
    
    fig = px.scatter(
    tsne_results_1, x=0, y=1,
    color=data7.target, labels={'color': 'Strain'})


    fig.update_layout(
        xaxis_title="TSNE-2D-1",
        yaxis_title="TSNE-2D-2",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"))

    fig.update_xaxes(showgrid=False,zeroline=False)
    fig.update_yaxes(showgrid=False,zeroline=False)
    fig.show()
    
    

tsne_fn(data7) 

