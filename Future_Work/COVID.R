library(ape)
library(kmer)

alpha_df = function(alpha){
  alpha = read.FASTA('alpha.fasta')
  alpha3 = kcount(alpha, k = 3)
  target = rep(('alpha'),length(alpha))
  alpha_df1 = data.frame(alpha3, target)
  return(alpha_df1)
}

alpha = alpha_df(alpha)




beta_df = function(beta){
  beta = read.FASTA('beta.fasta')
  beta3 = kcount(beta, k = 3)
  target = rep(('beta'),length(beta))
  beta_df1 = data.frame(beta3, target)
  return(beta_df1)
}

beta = beta_df(beta)




gamma_df = function(gamma){
  gamma = read.FASTA('gamma.fasta')
  gamma3 = kcount(gamma, k = 3)
  target = rep(('gamma'),length(gamma))
  gamma_df1 = data.frame(gamma3, target)
  return(gamma_df1)
}
gamma = gamma_df(gamma)


delta_df = function(delta){
  delta = read.FASTA('delta.fasta')
  delta3 = kcount(delta, k = 3)
  target = rep(('delta'),length(delta))
  delta_df1 = data.frame(delta3, target)
  return(delta_df1)
}
delta = delta_df(delta)



omicron_df = function(omicron){
  omicron = read.FASTA('omicron.fasta')
  omicron3 = kcount(omicron, k = 3)
  target = rep(('omicron'),length(omicron))
  omicron_df1 = data.frame(omicron3, target)
  return(omicron_df1)
}
omicron = omicron_df(omicron)



