# ML4Food
Tutorials exposing Food Science BSc students at ETH to practical applications of Machine Learning (ML) in Food Sciences.

## Set up
To run all 3 modules and the mini-project, we recommend you set up the following conda environment:
````
conda env create -f environment.yml
conda activate ml4food
````

## Overview of tutorials
The tutorials and the mini-project aim to teach students how to apply ML methods for data exploration and analysis using datasets related to food science. They all contain theory as well as practical examples and exercises. 

The 3 tutorials each cover the following topics:
- `M1_MLIntro_DataProcessing` introduces what ML is, describes datasets used throughout all tutorials and introduces basic data processing methods for ML. 
- `M2_MLSupervisedLearning` explains what supervised ML is and introduces common models used for classification and regression.
- `M3_MLUnsupervisedLearning` introduces unsupervised ML and describes different dimensionality reduction techniques. 

We recommend working through the tutorials in the described order. 

After having completed all 3 tutorials students can move on to doing the mini-project in `Mini_Project.ipynb`. The mini-project encompasses all important concepts learned throughout the tutorials and motivates students to apply the learned material on a simple exemplary use case. 

## Solutions
The solutions to the checkpoint exercises in all 3 tutorials are available in `notes/Master_Solution_Checkpoints.ipynb`. The solution of the mini-project is in `notes/Mini_Project_Solutions.ipynb`.

## Datasets
Throughout all tutorials and the mini-project, two datasets are used, namely:
* a processed version of the [Swiss Food composition database](https://naehrwertdaten.ch/en/) containing information on the composition of different foods,
* a processed version of the [Chocolate Bar Ratings](https://www.kaggle.com/datasets/evangower/chocolate-bar-ratings) dataset containing chocolate bar ratings from all over the world. 

More information on the processing and the datasets can be found at the start of  `M1_MLIntro_DataProcessing.ipynb`.

## Acknowledgments
This project was funded by the ETH Rector’s Impulse Fund.

