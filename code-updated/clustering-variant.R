library(tidyverse)
library(ggdendro)
library(RColorBrewer)
library(plotly)
library(readr)

#set the working directory 
setwd("/Users/chaarvibansal/Desktop/analysis-mutations/data-updated")

dendrogram_create = function(filePath)
{
  data <- read_csv(filePath)
  df = subset(data, select = -c(...1))
  dat <- df %>%
    mutate(sample_name = paste('var', seq(1:nrow(data)), sep = '_')) # 
  metadata <- dat %>%
    select(sample_name, target)
  numeric_data <- subset(dat, select = -c(target))
  
  # normalize data to values from 0 to 1 
  numeric_data_norm <- numeric_data %>%
    select(sample_name, everything()) %>%
    pivot_longer(cols = 2:ncol(.), values_to = 'value', names_to = 'type') %>%
    group_by(type) %>%
    mutate(value_norm = (value-min(value))/(max(value)-min(value))) %>% # normalize data to values 0–1
    select(sample_name, value_norm) %>%
    pivot_wider(names_from = 'type', values_from = 'value_norm') %>%
    column_to_rownames('sample_name')
  
  # create dendrogram from distance matrix of normalized data
  dist_matrix <- dist(numeric_data_norm, method = 'euclidean')
  dendrogram <- as.dendrogram(hclust(dist_matrix, method = 'complete'))
  
  # extract dendrogram segment data
  dendrogram_data <- dendro_data(dendrogram)
  dendrogram_segments <- dendrogram_data$segments # contains all dendrogram segment data
  head(dendrogram_segments)
  
  # get terminal dendrogram segments
  dendrogram_ends <- dendrogram_segments %>%
    filter(yend == 0) %>% # filter for terminal dendrogram ends
    left_join(dendrogram_data$labels, by = 'x') %>% # .$labels contains the row names from dist_matrix (i.e., sample_name)
    rename(sample_name = label) %>%
    left_join(metadata, by = 'sample_name') 
  
  variant_color <- c('Alpha' = '#AA00AA', 'Beta' = '#0000AA', 'Gamma' = '#00AA00','Delta'='#00AAAA','Omicron'='#FFFF55')
  
  p <- ggplot() +
    geom_segment(data = dendrogram_segments, 
                 aes(x=x, y=y, xend=xend, yend=yend)) +
    geom_segment(data = dendrogram_ends,
                 aes(x=x, y=y.x, xend=xend, yend=yend, color = target, text = paste('sample name: ', sample_name,
                                                                                      '<br>',
                                                                                      'Target: ', target))) + # test aes is for plotly
    scale_color_manual(values = variant_color) + #scale_y_reverse() + coord_flip()  
    theme_bw() + theme(legend.position = 'right') + ylab('Distance') + xlab('Sequence') + ggtitle('COVID dendrogram')
  
  ggplotly(p)
}

dendrogram_create('covid_kmer_new_3.csv')
