# Iris Flower Species Prediction

Predicting the species of Iris flowers using Machine Learning in Python. This project demonstrates the end-to-end workflow of a supervised learning problem with exploration, modeling, and evaluation.


## Project Overview

This project predicts the species of Iris flowers based on sepal and petal measurements. The main objectives are: 
- Understand and visualize the Iris dataset 
- Preprocess data for Machine Learning 
- Train and evaluate classifiers 
- Interpret results using confusion matrices and accuracy metrics

It’s built using Python and Jupyter Notebook, making it easy to follow for anyone learning ML.


## Dataset

The project uses the classic Iris dataset￼, which contains 150 samples of three Iris species: 
- Iris setosa 
- Iris versicolor 
- Iris virginica

Each sample has four features: 
- Sepal length 
- Sepal width 
- Petal length 
- Petal width


## Features 
- End-to-end ML pipeline in a single notebook 
- Data visualization with Matplotlib and Seaborn 
- Model training using scikit-learn classifiers (Logistic Regression, Decision Tree, Random Forest) 
- Evaluation metrics including accuracy and confusion matrices



## Installation

Clone this repository:

```bash
git clone https://github.com/AaryaaDahal/Iris-Flower-Species-Prediction.git 
cd Iris-Flower-Species-Prediction
```

Install required packages:
```bash
 pip install -r requirements.txt
```

## Usage

```python
jupyter notebook
```
Open iris_species_prediction.ipynb and run the cells step by step.

## Modeling

The notebook demonstrates training using multiple classifiers: 
- Logistic Regression – simple linear classifier 
- Decision Tree – interpretable tree-based model 
- Random Forest – ensemble method for better accuracy

You can modify the notebook to try other models or tune hyperparameters.


## Evaluation 
- Accuracy scores for each model 
- Confusion matrices for detailed classification performance 
- Visualizations of feature distributions

## Results

The models achieve high accuracy on the Iris dataset (typically >95%), showing that even simple classifiers can effectively separate the three species.
## License

[MIT](https://choosealicense.com/licenses/mit/)
