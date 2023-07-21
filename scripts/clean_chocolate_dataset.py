import os
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split


def read_dataset_in_dataframe(path2data)->pd.DataFrame:
    """Reading the dataset into a pandas dataframe.
    
        Args:
            The path where the raw dataset is saved.
        Returns:
            The dataframe holding the dataset.
    """
    dataset = pd.read_csv(path2data)
    columns_to_keep = ['id', 'bean_origin', 'year_reviewed', 'cocoa_percent',\
                        'num_ingredients', 'rating']
    return dataset[columns_to_keep]

def train_test_split_dataset(dataset:pd.DataFrame):
    train_set, test_set = \
        train_test_split(dataset, test_size=0.2, random_state=0)
    return train_set, test_set

def impute_missing_values(train_set:pd.DataFrame, test_set:pd.DataFrame):
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
    print('Standardizing the data...')
    standard_scaler = StandardScaler()
    train_data_st = train_data.copy()
    test_data_st = test_data.copy()
    train_data_st[feature_cols] = standard_scaler.fit_transform(train_data[feature_cols])
    test_data_st[feature_cols] = standard_scaler.transform(test_data[feature_cols])
    print('Standardization done!')
    return train_data_st, test_data_st

def process_dataset(path2data:str):
    dataset = read_dataset_in_dataframe(path2data)
    train, test = train_test_split_dataset(dataset)
    train, test = impute_missing_values(train, test)
    feature_columns = ['cocoa_percent', 'num_ingredients']
    train_st, test_st = standardize_the_dataset(train, test, feature_columns)
    train_st['split'] = 'train'
    test_st['split'] = 'test'
    dataset_preprocessed = pd.concat([train_st, test_st]).sort_index()
    return dataset_preprocessed