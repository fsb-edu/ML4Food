import os
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

'''
This module performs the preprocessing steps of the chocolate_bar_ratings.csv
dataset found in the /data folder. The steps are as follows:
1. Read the dataset in a pandas dataframe.
2. Split the dataset into train and test set.
3. Impute missing values for the 'num_ingredients' feature using mean.
4. Standardize the dataset only the 'num_ingredients' and 'cocoa_percent'
because the other features are either categorical, or will not be needed 
in the regression task.
5. Transform 'year_reviewed' to binary. 
6. Transform 'bean_origin' to have only 3 categories.
7. One hot encode the new categorical features of 'year_reviewed' and 'bean_origin'.
'''

def read_dataset_in_dataframe(path2data)->pd.DataFrame:
    """Reading the dataset into a pandas dataframe.
    
        Args:
            The path where the raw dataset is saved.
        Returns:
            The dataframe holding the dataset.
    """
    dataset = pd.read_csv(path2data)
    columns_to_keep = ['bean_origin', 'year_reviewed', 'cocoa_percent',\
                        'num_ingredients', 'rating']
    return dataset[columns_to_keep]

def train_test_split_dataset(dataset:pd.DataFrame):
    """
    This  function performs the train-test split of the dataset.

    Args:
        The dataset as a pandas dataframe
    Returns:
        Two sets of data: train and test set.
    """
    train_set, test_set = \
        train_test_split(dataset, test_size=0.2, random_state=0)
    return train_set, test_set

def impute_missing_values(train_set:pd.DataFrame, test_set:pd.DataFrame):
    """
    This  function performs the imputation of the missing values for the 
    'num_ingredients' feature. This is the only feature with missing values.

    Args:
        The train and test sets as pandas dataframes.
    Returns:
        Two sets of data: train and test set without  missing values.
    """
    print("Before imputation:")
    print("Train set missing values: ")
    print(train_set.isnull().sum())
    print("Test set missing values: ")
    print(test_set.isnull().sum())
    
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    train_col_to_impute = train_set[['num_ingredients']]
    test_col_to_impute = test_set[['num_ingredients']]
    train_set['num_ingredients'] = imputer.fit_transform(train_col_to_impute)
    test_set['num_ingredients'] = imputer.transform(test_col_to_impute)
    
    print("After imputation:")
    print("Train set missing values: ")
    print(train_set.isnull().sum())
    print("Test set missing values: ")
    print(test_set.isnull().sum())

    return train_set, test_set


def standardize_the_dataset(train_data:pd.DataFrame, test_data:pd.DataFrame, feature_cols:list):
    """
    This  function performs the standardization of the dataset.

    Args:
        The train and test sets as pandas dataframes as well as the 
        features that will be standardized.
    Returns:
        Two sets of data: train and test set standardized.
    """
    print('Standardizing the data...')
    standard_scaler = StandardScaler()
    train_data_st = train_data.copy()
    test_data_st = test_data.copy()
    train_data_st[feature_cols] = standard_scaler.fit_transform(train_data[feature_cols])
    test_data_st[feature_cols] = standard_scaler.transform(test_data[feature_cols])
    print('Standardization done!')
    return train_data_st, test_data_st

def map_year_label(year):
    """
    This  function refines the 'year_reviewed' feature.

    Args:
        The year that determines the labeling.
    Returns:
        The corresponding string.
    """
    if year >= 2015:
        return f'>=2015'
    else:
        return f'<2015'

def refine_bean_origin(country:str, countries_to_keep:list):
    """
    This  function refines the 'bean_origin' feature.

    Args:
        - country - that determines the labeling.
        - countries_to_keep - determines whether a country should be changed
        to 'others' or preserved.
    Returns:
        The corresponding string.
    """
    if country in countries_to_keep:
        return country
    else:
        return 'Other'

def one_hot_encode_years_bean_origin(dataset:pd.DataFrame):
    """
    This  function performs the one hot encoding of the 'year_reviewed'
    and 'bean_origin' refined features.

    Args:
        - dataset - the original dataset where the changes will take place.
    Returns:
        - the modified dataset.
    """
    one_hot_encoded_bo = pd.get_dummies(dataset['bean_origin'])
    year_mapping = {'>=2015':1, '<2015':0}
    dataset['year_binary'] = dataset['year_reviewed'].map(year_mapping)
    print(dataset['year_binary'])
    df = pd.concat([dataset, one_hot_encoded_bo], axis=1)
    return df


def process_dataset(path2data:str):
    """
    This is the driver function for the whole pre-processing step.

    Args:
        -path2data -  the path to the dataset.
    Returns:
        The pre-processed, ready to be used dataset.
    """
    dataset = read_dataset_in_dataframe(path2data)

    train, test = train_test_split_dataset(dataset)
    
    train, test = impute_missing_values(train, test)
    
    feature_columns = ['cocoa_percent', 'num_ingredients']
    train_st, test_st = standardize_the_dataset(train, test, feature_columns)
    
    train_st['split'] = 'train'
    test_st['split'] = 'test'
    dataset_preprocessed = pd.concat([train_st, test_st]).sort_index()
    
    dataset_preprocessed['year_reviewed'] = dataset_preprocessed['year_reviewed']\
        .apply(map_year_label)
    
    countries_to_keep = ['Venezuela', 'Peru']
    dataset_preprocessed['bean_origin'] = dataset_preprocessed['bean_origin']\
        .apply(refine_bean_origin, args=(countries_to_keep, ))
    
    dataset_preprocessed = one_hot_encode_years_bean_origin(dataset_preprocessed)
    dataset_preprocessed = dataset_preprocessed.drop(columns=['year_reviewed', 'bean_origin', 'Other'])
    dataset_preprocessed.rename(columns={'Peru':'country_peru', 'Venezuela':'country_venezuela'}, inplace=True)

    dataset_preprocessed['id'] = range(1, len(dataset_preprocessed)+1)
    dataset_preprocessed = dataset_preprocessed.set_index('id')

    return dataset_preprocessed