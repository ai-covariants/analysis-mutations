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


data = pd.read_csv('k-mer-lau9.csv')
data


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


# In[3]:


# In[5]:


plt.figure(figsize=(16,12))
sns.scatterplot(
    x="principal component 1", y="principal component 2",
    hue= data['Unnamed: 0'],
    palette=sns.color_palette("hls", 177),
    data=principal_df,
    legend= 'full',
    alpha=0.4)
plt.show()


# In[6]:


##screeplot

PC_values = np.arange(pca.n_components_) + 1
plt.plot(PC_values, pca.explained_variance_ratio_, 'ro-', linewidth=2, label = "k = 9")


plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Proportion of Variance Explained')
plt.legend()
plt.savefig('Screeplot.png')
plt.show()


# In[ ]:




