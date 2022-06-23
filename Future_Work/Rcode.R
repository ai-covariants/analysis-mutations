library("dplyr")
library(kmer)
library(ape)

d614_df = function(d614){
  d614 = read.FASTA('sample_updated.fasta')
  d614 = head(d614, 50)
  d6143 = kcount(d614, k = 3)
  target = rep(('D614'), length(d614))
  d614_df1 = data.frame(d6143, target)
  return(d614_df1)
}

d614 = d614_df(d614)

omicron_df = function(omicron){
  omicron = read.FASTA('omicron.fasta')
  omicron = head(omicron,50)
  omicron3 = kcount(omicron, k = 3)
  target = rep(('Omicron'), length(omicron))
  omicron_df1 = data.frame(omicron3, target)
  return(omicron_df1)
}

omicron = omicron_df(omicron)


data = bind_rows(d614, omicron)
write.csv(data, 'selected_covid_data.csv')


