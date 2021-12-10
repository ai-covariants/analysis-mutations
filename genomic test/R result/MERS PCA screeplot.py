#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
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


data = pd.read_csv('sample.csv')
data5 = pd.read_csv('sample5.csv')
data7 = pd.read_csv('sample7.csv')


# In[2]:


from sklearn.decomposition import PCA
pca = PCA(n_components=10)
##2 D PCA
y = data['Unnamed: 0']
X = data.drop(['Unnamed: 0'], axis = 1)
principalComponents = pca.fit_transform(X)


principal_df = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4',
                         'principal component 5','principal component 6','principal component 7','principal component 8',
                         'principal component 9','principal component 10'])



print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))


# In[3]:


n_components = 10
total_var = pca.explained_variance_ratio_.sum() * 100

fig = px.scatter_matrix(principalComponents,dimensions=range(n_components), labels=data,title=f'Total Explained Variance: {total_var:.2f}%')
fig.update_traces(diagonal_visible=False)
fig.show()




plt.figure(figsize=(50,50))
sns.scatterplot(
    x="principal component 1", y="principal component 2",
    hue= data['Unnamed: 0'],
    palette=sns.color_palette("hls", principal_df.shape[0]),
    data=principal_df,
    legend= 'full',
    alpha=1)
plt.savefig('PCA.png')
plt.show()


# In[4]:



pca5 = PCA(n_components=10)
##2 D PCA
y = data5['Unnamed: 0']
X5 = data5.drop(['Unnamed: 0'], axis = 1)
principalComponents5 = pca5.fit_transform(X5)


principal_df5 = pd.DataFrame(data = principalComponents5
             , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4',
                         'principal component 5','principal component 6','principal component 7','principal component 8',
                         'principal component 9','principal component 10'])



print('Explained variation per principal component: {}'.format(pca5.explained_variance_ratio_))


# In[5]:


n_components5 = 10
total_var5 = pca5.explained_variance_ratio_.sum() * 100

fig = px.scatter_matrix(principalComponents5,dimensions=range(n_components5), labels=data5,title=f'Total Explained Variance: {total_var:.2f}%')
fig.update_traces(diagonal_visible=False)
fig.show()




plt.figure(figsize=(50,50))
sns.scatterplot(
    x="principal component 1", y="principal component 2",
    hue= data5['Unnamed: 0'],
    palette=sns.color_palette("hls", principal_df5.shape[0]),
    data=principal_df5,
    legend= 'full',
    alpha=1)
plt.savefig('PCA7.png')
plt.show()


# In[6]:



pca7 = PCA(n_components=10)
##2 D PCA
y = data7['Unnamed: 0']
X7 = data7.drop(['Unnamed: 0'], axis = 1)
principalComponents7 = pca7.fit_transform(X7)


principal_df7 = pd.DataFrame(data = principalComponents7
             , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4',
                         'principal component 5','principal component 6','principal component 7','principal component 8',
                         'principal component 9','principal component 10'])



print('Explained variation per principal component: {}'.format(pca7.explained_variance_ratio_))


# In[7]:


n_components7 = 10
total_var7 = pca7.explained_variance_ratio_.sum() * 100

fig = px.scatter_matrix(principalComponents7,dimensions=range(n_components7), labels=data7,title=f'Total Explained Variance: {total_var:.2f}%')
fig.update_traces(diagonal_visible=False)
fig.show()




plt.figure(figsize=(50,50))
sns.scatterplot(
    x="principal component 1", y="principal component 2",
    hue= data7['Unnamed: 0'],
    palette=sns.color_palette("hls", principal_df7.shape[0]),
    data=principal_df7,
    legend= 'full',
    alpha=1)
plt.savefig('PCA7.png')
plt.show()


# In[8]:


##screeplot
##screeplot

PC_values = np.arange(pca.n_components_) + 1
plt.plot(PC_values, pca.explained_variance_ratio_, 'ro-', linewidth=2, label = "k = 3")

PC_values5 = np.arange(pca5.n_components_) + 1
plt.plot(PC_values5, pca5.explained_variance_ratio_, 'go-', linewidth=2, label = "k = 5")




PC_values7 = np.arange(pca7.n_components_) + 1
plt.plot(PC_values7, pca7.explained_variance_ratio_, 'b*-', linewidth=2, label = "k = 7")


plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Proportion of Variance Explained')
plt.legend()
plt.savefig('Screeplot.png')
plt.show()

