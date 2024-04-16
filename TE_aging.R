### Loop for storing age estimations for TEs in wyeomyia

### set working directory
setwd("~/Documents/CooperLab/ltr_aging")

### import phangorn
library(ape)
library(phangorn)
library(tidyverse)
library(ggplot2)

### create lists of files to loop through
my.files = list.files(path="./aligned", pattern="*.stdout", full.names=TRUE)

### create table to store data in
### columns: species, name, distance, age
df <- data.frame(matrix(ncol = 5, nrow = length(my.files)))
x <- c("Species","TE", "Distance", "Age", "Age In Millions")
colnames(df) <- x

### create loop to find distance and age estimation for each aaeg TE file
count=0
for (file in my.files){
  count<-count+1
  
  dna <- read.dna(file, format = "fasta")
  distance<-dist.dna(dna)
  age<-(distance/(2*(1*10^-9)))/10
  age_in_millions<-age/1000000
  
  header<-labels(dna)[1]
  
  species_split<-strsplit(header, split = "_")[[1]][1]
  if (species_split == "Aaeg"){
    species<-"Aedes aegypti"
  } else if (species_split == "Aalb"){
    species<-"Aedes albopictus"
  } else if (species_split == "Acol"){
    species<-"Anopheles coluzzii"
  } else if (species_split == "Cqui"){
    species<-"Culex quinquefasciatus"
  } else if (species_split == "Ctar"){
    species<-"Culex tarsalis"
  } else if (species_split == "Wsmi"){
    species<-"Wyeomyia smithii"
  }
  
  position_split<-strsplit(header, split = "#")
  position<-position_split[[1]][2]
  
  family_split<-strsplit(position, split = ":")
  family<-family_split[[1]][1]
  
  df[count,1]<-species
  df[count,2]<-family
  df[count,3]<-distance
  df[count,4]<-age
  df[count,5]<-age_in_millions
}

ggplot(df, aes(Species,`Age In Millions`)) + geom_boxplot() + geom_jitter(alpha = 0.3, color = "#9933FF") + theme_classic()

ggplot(df, aes(TE,`Age In Millions`)) + geom_boxplot() + geom_jitter(alpha = 0.3, color = "#9933FF") + theme_classic()

ggplot(df, aes(Species,`Age In Millions`)) + geom_violin(trim = TRUE, fill = "#CCCCFF", color = "#9933FF") + geom_boxplot(width = 0.15) + geom_jitter(alpha = 0.3, color = "#330066") + theme_classic()

ggplot(df, aes(TE,`Age In Millions`)) + geom_violin(trim = TRUE, fill = "#CCCCFF", color = "#9933FF") + geom_boxplot(width = 0.15) + geom_jitter(alpha = 0.3, color = "#330066") + theme_classic()
