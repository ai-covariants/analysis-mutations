library(kmer)
library(seqinr)
library(ape)


attach(genomic)
genomic = read.FASTA('genomic.fna')
genomic


x = kcount(genomic,k =3)
x 
write.csv(x,'sample.csv')
