library(tidyverse)
library(ggdendro)
library(RColorBrewer)
library(plotly)
library(readr)

#set the working directory 
setwd("/Users/chaarvibansal/Desktop/analysis-mutations/data-updated")

dendrogram_create = function(filePath,image_name)
{
  df <- read_csv(filePath)
  dat <- df %>%
    mutate(sample_name = paste('var', seq(1:nrow(df)), sep = '_')) # 
  metadata <- dat %>%
    select(sample_name, Country)
  numeric_data <- subset(dat, select = -c(Country))
  
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
  
  # Generate custom color palette for dendrogram ends based on metadata variable
  unique_vars <- levels(factor(dendrogram_ends$Country)) %>% 
    as.data.frame() %>% rownames_to_column('row_id') 
  # count number of unique variables
  color_count <- length(unique(unique_vars$.))
  # get RColorBrewer palette
  get_palette <- colorRampPalette(brewer.pal(n = 8, name = 'Set1'))
  # produce RColorBrewer palette based on number of unique variables in metadata:
  palette <- get_palette(color_count) %>% 
    as.data.frame() %>%
    rename('color' = '.') %>%
    rownames_to_column(var = 'row_id')
  color_list <- left_join(unique_vars, palette, by = 'row_id') %>%
    select(-row_id)
  var_color <- as.character(color_list$color)
  names(var_color) <- color_list$.
  
  p <- ggplot() +
    geom_segment(data = dendrogram_segments, 
                 aes(x=x, y=y, xend=xend, yend=yend)) +
    geom_segment(data = dendrogram_ends,
                 aes(x=x, y=y.x, xend=xend, yend=yend, color = Country, text = paste('sample name: ', sample_name,
                                                                                    '<br>',
                                                                                    'Country: ', Country))) + # test aes is for plotly
    scale_color_manual(values = var_color) + #scale_y_reverse() + coord_flip() + 
    theme_bw() + theme(legend.position = 'right') + ylab('Distance') + xlab('Sequence') + ggtitle(image_name)
  
  ggplotly(p)
}

#dendrogram_create('alpha.csv','Alpha country-wise cluster')
#dendrogram_create('beta.csv','Beta country-wise cluster')
#dendrogram_create('gamma.csv','Gamma country-wise cluster')
dendrogram_create('delta.csv','Delta country-wise cluster')
dendrogram_create('omicron.csv','Omicron country-wise cluster')