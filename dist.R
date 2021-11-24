library(ape)
library(phangorn)
library(ggplot2)
library(reshape2)
# install.packages('TreeDist')
# install.packages("sass")
library("TreeDist")

# if (!requireNamespace("BiocManager", quietly = TRUE))
#   install.packages("BiocManager")
# BiocManager::install(c("Biostrings", "seqLogo"))


tree1 = read.tree(file = "main_trees/original_phylo_corr.tree")
tree2 = read.tree(file = "main_trees/consensus.tree")

distance1 <- RF.dist(tree1, tree2, normalize = FALSE, rooted = FALSE)
print(distance1)
VisualizeMatching(ClusteringInfoDistance, tree1, tree2)
