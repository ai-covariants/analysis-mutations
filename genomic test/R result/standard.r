library(kmer)


genomic = read.FASTA('genomic.fna')
genomic


x3 = kcount(genomic,k =3)
x3 
write.csv(x3,'sample.csv')
x5 = kcount(genomic, k =5)
write.csv(x5, 'sample5.csv')

x7 = kcount(genomic, k = 7)
write.csv(x7, 'sample7.csv')
