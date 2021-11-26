#!/usr/bin/env python
# coding: utf-8

# In[1]:

from matplotlib import pyplot as plt
from itertools import product
from Bio import SeqIO
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plot
import numpy as np
import plotly.express as px

# create all possible kmers
def createKmers(string, k):
    kmers = [''.join(c) for c in product(string, repeat=k)]
    return(kmers)

# count kmers in string
def countKmers(string, kmers):
    kcount = list()
    for k in kmers:
        kcount = kcount + [string.count(k)]
    return(kcount)

# normalize kmer counts by total number of kmers
def normKmers(kdict):
    norm = dict()
    for key in kdict.keys():
        l = list()
        for i in kdict[key]:
            l = l + [i/sum(kdict[key])]
        norm[key] = l
    return(norm)

# create all possible kmers for a given length of k
k = 3
kmers = createKmers('ACGT', k)

# input fasta containing all sequences to be analysed
inputFasta = 'sample.fasta'

# this dictionary will contain the kmer counts for each sequence
kmerCounts = dict()

ffile = SeqIO.parse(inputFasta, 'fasta')
# iterate through each sequence in the fasta file
for seq_record in ffile:
    # extract just the accession number to use as ID
    id = str(seq_record.id)[1:]
    
    # count the occurance of each kmer and store in the dictionary
    kmerCounts[id] = countKmers(str(seq_record.seq), kmers)

kmerNorm = normKmers(kmerCounts)
kmerNorm

# create a dataframe from the dictionary
#df = pd.DataFrame.from_dict(kmerCounts, orient='index', columns=kmers)
#dfnorm = pd.DataFrame.from_dict(kmerNorm, orient='index', columns=kmers)
dfnorm = pd.DataFrame.from_dict(kmerNorm, orient = 'index',columns = kmers)
dfnorm


# In[ ]:


from sklearn.decomposition import PCA
pca = PCA(n_components=10)
principalComponents = pca.fit_transform(dfnorm)


principal_df = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4',
                         'principal component 5','principal component 6','principal component 7','principal component 8',
                         'principal component 9','principal component 10'])



print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))

n_components = 10
total_var = pca.explained_variance_ratio_.sum() * 100

fig = px.scatter_matrix(principalComponents,dimensions=range(n_components), labels=dfnorm,title=f'Total Explained Variance: {total_var:.2f}%')
fig.update_traces(diagonal_visible=False)
fig.show()


# In[2]:


# create all possible kmers for a given length of k
k = 5
kmers5 = createKmers('ACGT', k)

# input fasta containing all sequences to be analysed
inputFasta = 'sample.fasta'

# this dictionary will contain the kmer counts for each sequence
kmerCounts5 = dict()

ffile = SeqIO.parse(inputFasta, 'fasta')
# iterate through each sequence in the fasta file
for seq_record in ffile:
    # extract just the accession number to use as ID
    id = str(seq_record.id)[1:]
    
    # count the occurance of each kmer and store in the dictionary
    kmerCounts5[id] = countKmers(str(seq_record.seq), kmers5)

kmerNorm5 = normKmers(kmerCounts5)
kmerNorm5

# create a dataframe from the dictionary
#df = pd.DataFrame.from_dict(kmerCounts, orient='index', columns=kmers)
#dfnorm = pd.DataFrame.from_dict(kmerNorm, orient='index', columns=kmers)
dfnorm5 = pd.DataFrame.from_dict(kmerNorm5, orient = 'index',columns = kmers5)
dfnorm5


# In[ ]:


pca5 = PCA(n_components=10)
principalComponents5 = pca5.fit_transform(dfnorm5)


principal_df5 = pd.DataFrame(data = principalComponents5
             , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4',
                         'principal component 5','principal component 6','principal component 7','principal component 8',
                         'principal component 9','principal component 10'])



print('Explained variation per principal component: {}'.format(pca5.explained_variance_ratio_))

n_components5 = 10
total_var5 = pca5.explained_variance_ratio_.sum() * 100

fig = px.scatter_matrix(principalComponents5,dimensions=range(n_components5), labels=dfnorm5,title=f'Total Explained Variance: {total_var5:.2f}%')
fig.update_traces(diagonal_visible=False)
fig.show()


# In[3]:


# create all possible kmers for a given length of k
k = 7
kmers7 = createKmers('ACGT', k)

# input fasta containing all sequences to be analysed
inputFasta = 'sample.fasta'

# this dictionary will contain the kmer counts for each sequence
kmerCounts7 = dict()

ffile = SeqIO.parse(inputFasta, 'fasta')
# iterate through each sequence in the fasta file
for seq_record in ffile:
    # extract just the accession number to use as ID
    id = str(seq_record.id)[1:]
    
    # count the occurance of each kmer and store in the dictionary
    kmerCounts7[id] = countKmers(str(seq_record.seq), kmers7)

kmerNorm7 = normKmers(kmerCounts7)
kmerNorm7

# create a dataframe from the dictionary
#df = pd.DataFrame.from_dict(kmerCounts, orient='index', columns=kmers)
#dfnorm = pd.DataFrame.from_dict(kmerNorm, orient='index', columns=kmers)
dfnorm7 = pd.DataFrame.from_dict(kmerNorm7, orient = 'index',columns = kmers7)
dfnorm7


# In[ ]:


pca7 = PCA(n_components=10)
principalComponents7 = pca7.fit_transform(dfnorm7)


principal_df7 = pd.DataFrame(data = principalComponents7
             , columns = ['principal component 1', 'principal component 2','principal component 3','principal component 4',
                         'principal component 5','principal component 6','principal component 7','principal component 8',
                         'principal component 9','principal component 10'])



print('Explained variation per principal component: {}'.format(pca7.explained_variance_ratio_))

n_components7 = 10
total_var7 = pca7.explained_variance_ratio_.sum() * 100

fig = px.scatter_matrix(principalComponents7,dimensions=range(n_components7), labels=dfnorm7,title=f'Total Explained Variance: {total_var7:.2f}%')
fig.update_traces(diagonal_visible=False)
fig.show()


# In[4]:


PC_values = np.arange(pca.n_components_) + 1
plt.plot(PC_values, pca.explained_variance_ratio_, 'ro-', linewidth=2, label = "k = 3")

PC_values5 = np.arange(pca5.n_components_) + 1
plt.plot(PC_values5, pca5.explained_variance_ratio_, 'b*-', linewidth=2, label = "k = 5")

PC_values7 = np.arange(pca7.n_components_) + 1
plt.plot(PC_values7, pca7.explained_variance_ratio_, 'yo-', linewidth=2, label = "k = 7")





plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Proportion of Variance Explained')
plt.legend()
plt.savefig('Screeplot.png')
plt.show()

##kink at 6

##sigma of the variance by the first 6 principal components
##bare minimum should be 66%
## first two PCA should be 40%

