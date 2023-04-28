import pandas as pd
import numpy as np

PATH_TO_DATASET = '../data/Swiss_food_composition_database.xlsx'

def process_dataset()->pd.DataFrame:
    """This is the driver method that will starts the processing process. It will
    return the clean and ready to use dataset.
    Args:
        None
    Returns:
        pd.Dataframe - the clean dataframe
    """
    clean_dataset = read_dataset_in_dataframe()
    drop_unnecessary_cols(clean_dataset)
    rename_columns(clean_dataset)
    replace_non_numerical_values(clean_dataset)
    replace_traces(clean_dataset)
    return clean_dataset


def read_dataset_in_dataframe():
    """Reading the dataset into a pandas dataframe.
    
        Args:
            None
        Returns:
            The dataframe holding the dataset.
    """
    dataset = pd.read_excel(PATH_TO_DATASET)
    return dataset


def drop_unnecessary_cols(dataset:pd.DataFrame)-> None:
    """The first step is to select only the columns that we want to keep. We need to remove all Source and
    Derivation of Value columns, Synonyms, ID V 4.0 from the columns. The change happens in place, so the method does not
    return anything.
    
    Args:
        dataset: is the dataset whose columns will be modified.
    
    Returns:
        None
    """
    cols = dataset.columns
    cols_names_to_drop = ['Source', 'Derivation of Value', 'Synonyms', 'ID V 4.0', 'Energy, kilojoules (kJ)']
    cols_to_drop = [col for col in cols if col in cols_names_to_drop]
    dataset = dataset.drop(columns=cols_to_drop)


def rename_columns (dataset:pd.Dataframe) -> None:
    """The second step is to rename the columns. We will use this procedure: take the first word and the unit of measure 
    and concatenate them with a prefix of f_, where f will stand for feature. 
    E.g: "Energy, kilocalories (kcal)" -> "f_energy_kcal". The changes will happen in place so the method will not 
    return anything.
    
    Args:
        dataset: is the dataset we are modifying

    Returns:
        None since the change happens in place.
    """
    prefix = 'f_'
    columns = dataset.columns[2:] # only the numerical features, Name and ID unchanged
    new_names = [prefix + (col_name[col_name.index('('):] + col_name.split(',')[0]).replace('(','' ).replace(')', '') for col_name in columns]
    new_cols = [prefix+columns[0], prefix+columns[1]]
    new_cols = new_cols.extend(new_names)
    dataset.columns = new_cols


"""

"""
def replace_non_numerical_values():
    return 0


"""

"""
def replace_traces():
    return 0