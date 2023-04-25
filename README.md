# DMFVAE
Deep matrix factorization model based on variational autoencoder for miRNA-disease associations prediction

# Requirements
* TensorFlow 1.9.0
* python 3.6
* numpy 1.19.5
* pandas 0.20.0
* scikit-learn 0.24.0
* scipy 1.5.4

# Data
We provide two kinds of database includes HMDD v2.0 and HMDD v3.2, our model experiments on balanced and unbalanced datasets in two databases

# Take HMDD v2.0 as an example：
1. modifing the path address of each required file before running
2. running example.py to obtain embedding features of miRNAs and disease network structures 
1. running dataprocess.py to obtain samples
2. running vae.py to train and prediction

# Cite
Please cite our paper if you use this code in your own work:
“Deep matrix factorization model based on variational autoencoder for miRNA-disease associations prediction”
