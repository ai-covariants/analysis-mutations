library(kmer)
library(ape)



##D614
d614 = read.FASTA('sample.fasta')
d614 = d614[-1]
d614
##wuhan-hu-1 original sequence
wuhan_hu_1 = d614$`BetaCoV/Wuhan-Hu-1/2019|EPI_ISL_402125`
#kmer frequency
wuhan_kmer = kcount(wuhan_hu_1, k =3)
wuhan_kmer

write.csv(wuhan_kmer, 'wuhan_kmer.csv')



##mers
mers = read.FASTA('genomic.fna')
mers
#first
mers1 = mers$`JX869059.2 Human betacoronavirus 2c EMC/2012, complete genome`
mers1_kmer = kcount(mers1, k = 3)
mers1_kmer

#second mers
mers2 = mers$`KF600612.1 Middle East respiratory syndrome coronavirus isolate Riyadh_1_2012, complete genome`
mers2_kmer = kcount(mers2, k = 3)
mers2_kmer

#third mers
mers3 = mers$`KC776174.1 Human betacoronavirus 2c Jordan-N3/2012, complete genome`
mers3_kmer = kcount(mers3, k = 3)
mers3_kmer

##fourth mers
mers4 = mers$`KP209307.1 Middle East respiratory syndrome coronavirus strain Abu Dhabi_UAE_18_2014, complete genome`
mers4_kmer = kcount(mers4, k = 3)
mers4_kmer

#fifth_mers
mers5 = mers$`KY673148.1 Middle East respiratory syndrome-related coronavirus strain Hu/Oman_50_2015, complete genome`
mers5_kmer = kcount(mers5, k = 3)
mers5_kmer

##sixth mers
mers6 = mers$`KF600630.1 Middle East respiratory syndrome coronavirus isolate Buraidah_1_2013, complete genome`
mers6_kmer = kcount(mers6, k = 3)
mers6_kmer

##seventh mers
mers7 = mers$`MN723542.1 Middle East respiratory syndrome-related coronavirus isolate Hu/Jeddah-KSA-173RS1101/2017, complete genome`
mers7_kmer = kcount(mers7, k = 3)
mers7_kmer

##eighth mers
mers8 = mers$`KF186564.1 Middle East respiratory syndrome coronavirus isolate Al-Hasa_4_2013, complete genome`
mers8_kmer = kcount(mers8, k = 3)
mers8_kmer

#join them
mers_total = rbind(mers1_kmer, mers2_kmer, mers3_kmer, mers4_kmer, mers5_kmer,
                   mers6_kmer, mers7_kmer, mers8_kmer)
mers_total
#reset index
row.names(mers_total) = 1:nrow(mers_total)
mers_total


##save as csv
write.csv(mers_total, 'mers_kmer.csv')

##omicron
omicron = read.FASTA('omicron.fasta')
omicron

##first omicron
omicron1 = omicron$`hCoV-19/USA/UT-UPHL-211211887190/2021|EPI_ISL_7741717|2021-11-29`
omicron1_kmer = kcount(omicron1, k = 3)
omicron1_kmer

##second omicron
omicron2 = omicron$`hCoV-19/Switzerland/BL-ETHZ-35009242/2021|EPI_ISL_7620538|2021-11-29`
omicron2
omicron2_kmer = kcount(omicron2, k = 3)
omicron2_kmer

#third omicron
omicron3 = omicron$`hCoV-19/Israel/ICH-760598216/2021|EPI_ISL_7552186|2021-12-03`
omicron3_kmer = kcount(omicron3, k = 3)
omicron3_kmer

#fourth omicron
omicron4 = omicron$`hCoV-19/India/DL-GSLLNH/2021|EPI_ISL_7623676|2021-12-06`
omicron4_kmer = kcount(omicron4, k = 3)
omicron4_kmer

#fifth omicron
omicron5 = omicron$`hCoV-19/Botswana/R44B19_BHP_000844008/2021|EPI_ISL_7121205|2021-11-23`
omicron5_kmer = kcount(omicron5, k = 3)
omicron5_kmer

##sixth omicron
omicron6 = omicron$`hCoV-19/Germany/HE-RKI-I-385980/2021|EPI_ISL_8219450|2021-12-03`
omicron6_kmer = kcount(omicron6, k = 3)
omicron6_kmer

##seventh omicron
omicron7 = omicron$`hCoV-19/Spain/IB-HUSE-03236/2021|EPI_ISL_7624232|2021-12-03`
omicron7_kmer = kcount(omicron7, k = 3)
omicron7_kmer


##eighth omicron
omicron8 = omicron$`hCoV-19/France/IDF-HMN-21122210612/2021|EPI_ISL_8256019|2021-12-15`
omicron8_kmer = kcount(omicron8, k = 3)
omicron8_kmer

#join them
omicron_total = rbind(omicron1_kmer, omicron2_kmer, omicron3_kmer, omicron4_kmer, omicron5_kmer,
                      omicron6_kmer, omicron7_kmer, omicron8_kmer)
omicron_total
#reset index
row.names(omicron_total) = 1:nrow(omicron_total)
omicron_total


##save as csv
write.csv(omicron_total, 'omicron_kmer.csv')



##gamma
gamma = read.FASTA('beta_gamma.fasta')
gamma1 = gamma$`P.1/EPI_ISL_3842262/North America / USA / Colorado/2021-07-07`
gamma1_kmer = kcount(gamma1, k = 3)
gamma1_kmer

gamma2 = gamma$`P.1/EPI_ISL_5645882/South America / Brazil / Sao Paulo/2021-05-31`
gamma2_kmer = kcount(gamma2, k = 3)
gamma2_kmer

gamma3 = gamma$`P.1/EPI_ISL_3983576/North America / USA / Wisconsin / Ozaukee County/2021-07-26`
gamma3_kmer = kcount(gamma3, k = 3)
gamma3_kmer


gamma4 = gamma$`P.1/EPI_ISL_4415922/South America / Brazil / Sao Paulo/2021-06-04`
gamma4_kmer = kcount(gamma4, k = 3)
gamma4_kmer

gamma5 = gamma$`P.1/EPI_ISL_2756234/South America / Chile / O'Higgins / San Vicente/2021-06-07`
gamma5_kmer = kcount(gamma5,k = 3)
gamma5_kmer


gamma6 = gamma$`P.1/EPI_ISL_4422674/South America / Brazil / Bahia/2021-06-08`
gamma6_kmer = kcount(gamma6, k = 3)
gamma6_kmer

gamma7 = gamma$`P.1/EPI_ISL_4417797/South America / Brazil / Bahia/2021-08-05`
gamma7_kmer = kcount(gamma7,k = 3)
gamma7_kmer


gamma8 = gamma$`P.1/EPI_ISL_2344540/South America / Brazil / Sao Paulo/2021-03-30`
gamma8_kmer = kcount(gamma8,k = 3)
gamma8_kmer



#join them
gamma_total = rbind(gamma1_kmer, gamma2_kmer,gamma3_kmer,gamma4_kmer,
                    gamma5_kmer, gamma6_kmer, gamma7_kmer, gamma8_kmer)
gamma_total
#reset index
row.names(gamma_total) = 1:nrow(gamma_total)
gamma_total


##save as csv
write.csv(gamma_total, 'gamma_kmer.csv')
