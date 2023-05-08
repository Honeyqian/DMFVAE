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
#Supplementary data
The Supplementary documents include formulas, picture, and tables.  For Supplemental Formula 1: is the detailed process of using EASNN to obtain an enhanced association matrix; For Supplemental Formula 2: is a specific formula for each performance evaluation metric that measures the predicted performance of DMFVAE. Supplementary Figure S1: is a detailed parameter tuning experiment for the HMDD v2.0 balanced dataset. For supplementary tables S1-S2: is a single value for the evaluation metric on the HMDD v2.0 dataset; For supplementary tables S3-S4: is a single value for the evaluation metric on the HMDD v3.2 dataset; For supplementary form S5: is the top 20 candidate miRNAs associated with CN; For Supplemental Form S6:  is  the top 20 candidate miRNAs associated with EN.

# Cite
Please cite our paper if you use this code in your own work:
“Deep matrix factorization model based on variational autoencoder for miRNA-disease associations prediction”
