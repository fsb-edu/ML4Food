# ML4Food
Develop tutorials that expose Food Science BSc students at ETH to practical applications of machine learning in food sciences. Students will learn to apply ML methods for data exploration and analysis using datasets related to food science.

## Tutorial sections
Three tutorial sections are planned (each written in a Jupyter notebooks). Each tutorial should include an interactive teaching section and a short exercise.

### 1) Overview of ML for food sciences
* Brief textual overview on where ML is used in food sciences
* Brief overview of unsupervised vs. supervised learning
* Introduction to 2-3 datasets that will be used throughout the tutorials (see [datasets section](#datasets))
* Overview and application of basic data processing methods for ML methods (simple code excerpts using scikit-learn and pandas) including:
    * train-test split
    * standardization
    * outlier detection
    * data quality control

### 2) Unsupervised clustering
* Brief overview of unsupervised learning and its main applications (clustering, dimensionality reduction)
* Display of interactive plots of different clustering methods in which students can play with different parameters and observe the behavior of the resulting clustering, e.g.:
    * PCA
    * k-means (inspiration [here](https://k-means-explorable.vercel.app/))
    * UMAP (inspiration [here](https://pair-code.github.io/understanding-umap/))
    * t-SNE


### 3) Supervised learning: classification and regression
* Introduction of training setup, e.g. role of train-test set, notion of reduction of loss metric
* Brief overview of some common models for classification and regression
* Introduction of role of evaluation metrics and overview of a few commonly used metrics
* Introduction of role of hyperparameters & display of interactive plots where students can play with hyperparameters of a model and observe the changing decision boundaries and evaluation metrics of the resulting models


## Datasets
Choosing 2-3 datasets from a dataset list, we want to display the above [tutorial sections](#tutorial-sections) using these food science datasets as examples. Criteria for selecting datasets are: easily downloadable, some interesting insight can be gained in dataset by using the methods introduced in these tutorials.


## Setting up the environment
In order to be able to set up the environment you first need to have conda installed in your system. Assuming conda is installed run the following steps:
1. Go inside ML4Food folder where the `environment.yml` file is located.
2. There run `conda env create -f environment.yml`.
3. After it has finished running, execute `conda activate ml4food`. This will activate the environment.

To run the notebooks, in the IDE of your choice choose *ml4food* as your Python kernel.

## Future considerations:
 - Automatic graded exercises.
 - Check applications of ML in Food Science from Overview chapter.
 - Clustering for the Swiss Food Composition Dataset.
 - Example where dimensionality reduction and supervised learning
 are used as part of the same pipeline. This will help in visualizing
 the models.
 - Recreation of M2-Figure 5 GIF.
 - Selection of multiple categories in the unsupervised plots.