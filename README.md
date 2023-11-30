# ML4Food
An introduction to Machine Learning (ML) for food scientists. These tutorials explore practical applications of ML in the Food Sciences. These tutorials assume at least a foundational knowledge of Python programming.

## Set up
To run all 3 modules and the mini-project, we recommend you set up the following `conda` environment (make sure you have [`conda`](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) installed first):
````
conda env create -f environment.yml
conda activate ml4food
````

## Overview of tutorials
The tutorials and the mini-project aim to teach students how to apply ML methods for data exploration and analysis using datasets related to food science. They all contain theory as well as practical examples and exercises. 

The 3 tutorials cover the following topics:
- `M1_MLIntro_DataProcessing` provides an introduction to ML, describes datasets used throughout these tutorials, and introduces basic data processing methods for ML. 
- `M2_MLSupervisedLearning` explains what supervised ML is and introduces common models used for classification and regression.
- `M3_MLUnsupervisedLearning` introduces unsupervised ML and describes different dimensionality reduction techniques. 

We recommend working through the tutorials in the described order. 

After having completed all 3 tutorials, students can test their knowledge with the mini-project in `Mini_Project.ipynb`. The mini-project encompasses all important concepts learned throughout the tutorials and motivates students to apply the learned material on a simple exemplary use case. 

## Solutions
The solutions to the checkpoint exercises in all 3 tutorials are available in `solutions/Master_Solution_Checkpoints.ipynb`. The solution of the mini-project is in `solutions/Mini_Project_Solutions.ipynb`.

## Datasets
The tutorials and mini-project use the following datasets:
* a processed version of the [Swiss Food composition database](https://naehrwertdaten.ch/en/) containing information on the composition of different foods,
* a processed version of the [Chocolate Bar Ratings](https://www.kaggle.com/datasets/evangower/chocolate-bar-ratings) dataset containing chocolate bar ratings from all over the world. 

More information on the processing and the datasets can be found at the start of  `M1_MLIntro_DataProcessing.ipynb`.

## Images
All images of the tutorials can be found in the `images` folder. To change or modify any of them, see `Graphics Of ML4Food.pptx`.

## Acknowledgments
This project was supported by funding from the ETH Rector’s Impulse Fund. We thank Adrian Weiss for his kind donation in support of this initiative.

