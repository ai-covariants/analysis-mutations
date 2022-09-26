# analysis-mutations
Analysis of mutations during COVID-19 using unsupervised machine learning 

## Data 

Data for different variants (250 sequences in total) was downloaded from GISAID (global initiative on sharing Avian influenza data). Please contact the authors for the dataset. 

## Code

1. kmer-analysis-using-R.R: This R script is used to generate kmers of a specified length from the given FASTA file. Change the value of k as per requirement. This script accepts as input a FASTA file and outputs a csv file with kmer count for all possible kmers. 

2. PCA Analysis.ipynb: This notebook contains the code for analysing the variance explained by different PCA components. We have analysed 10 components. 

3. dimensionality-reduction-comparison.ipynb: In this notebook, Principal Component Analysis,t-SNE and UMAP are used to reduce the dimensions while retaining most information of the datasets. Subsequently, the visualization is produced to examine the relationship between various isolates.

4. clustering-country.R & clustering-variant.R: These scripts have been used to plot dendrograms after applying hierarchial clustering on the processed kmer data for k=3. (Reference - https://towardsdatascience.com/custom-coloring-dendrogram-ends-in-r-f1fa45e5077a)

## Results

1. results-PCA: This folder includes Principal Component Analysis i.e.,dimensional reduction results using dataset from GISAID.

2. results-T-SNE: This folder comprises of t-SNE dimensional reduction approach using dataset from GISAID.

3. results-UMAP: This folder contains UMAP, a novel dimensional reduction method, using dataset from GISAID.

4. results-Clustering: This folder contains clustering results, variant-wise and country-wise. 
