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
    print('Done. Clean dataset ready.')
    return clean_dataset


def read_dataset_in_dataframe():
    """Reading the dataset into a pandas dataframe.
    
        Args:
            None
        Returns:
            The dataframe holding the dataset.
    """
    # header is 3 since the header is the third row in the Excel file
    dataset = pd.read_excel(PATH_TO_DATASET, header=2)
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
    sources_to_drop = ['Source.'+str(i) for i in range(1,40)]
    derivations_to_drop = ['Derivation of value.' + str(i) for i in range(1,40)]
    # additional columns to drop
    cols_to_drop = ['Source', 'Derivation of value', 'Density', 'Synonyms', 'ID V 4.0', 
                    'Matrix unit', 'ID SwissFIR','Energy, kilojoules (kJ)', 'Record has changed']
    cols_to_drop.extend(sources_to_drop)
    cols_to_drop.extend(derivations_to_drop)
    dataset = dataset.drop(columns=cols_to_drop, axis=1, inplace=True)


def rename_columns (dataset:pd.DataFrame) -> None:
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
    new_cols_mapping = {'ID':'ID', 
                    'Name':'name', 
                    'Category':'category', 
                    'Energy, kilocalories (kcal)': 'energy_kcal',
                    'Fat, total (g)':'fat_g', 
                    'Fatty acids, saturated (g)': 
                    'fatty_acids_sat_g',
                    'Fatty acids, monounsaturated (g)':'fatty_acids_monounsat_g', 
                    'Fatty acids, polyunsaturated (g)':'fatty_acids_polyunsat_g',
                    'Cholesterol (mg)':'cholesterol_mg', 
                    'Carbohydrates, available (g)':'carbohydrates_g', 
                    'Sugars (g)':'sugars_g', 
                    'Starch (g)':'starch_g',
                    'Dietary fibres (g)':'fibres_g', 
                    'Protein (g)':'protein_g', 
                    'Salt (NaCl) (g)':'salt_g', 
                    'Alcohol (g)':'alcohol_g', 
                    'Water (g)':'water_g', 
                    'Vitamin A activity, RE (µg-RE)':'vit_A_activity_re_µg', 
                    'Vitamin A activity, RAE (µg-RE)':'vit_A_activity_rae_µg', 
                    'Retinol (µg)':'retinol_µg', 
                    'Beta- carotene activity (µg-BCE)':'beta_carotene_activity_µg', 
                    'Beta-carotene (µg)':'beta_carotene_µg', 
                    'Vitamin B1 (thiamine) (mg)':'vit_B1_mg', 
                    'Vitamin B2 (riboflavin) (mg)':'vit_B2_mg', 
                    'Vitamin B6 (pyridoxine) (mg)':'vit_B6_mg', 
                    'Vitamin B12 (cobalamin) (µg)':'vit_B12_µg', 
                    'Niacin (mg)':'niacin_mg', 
                    'Folate (µg)':'folate_µg', 
                    'Panthotenic acid (mg)':'panthotenic_acid_mg',
                    'Vitamin C (ascorbic acid) (mg)':'vit_c_mg', 
                    'Vitamin D (calciferol) (µg)':'vit_d_µg', 
                    'Vitamin E activity (mg-ATE)':'vit_e_activity_mg', 
                    'Potassium (K) (mg)':'potassium_mg', 
                    'Sodium (Na) (mg)':'sodium_mg',
                    'Chloride (Cl) (mg)':'chloride_mg', 
                    'Calcium (Ca) (mg)':'calcium_mg', 
                    'Magnesium (Mg) (mg)':'magnesium_mg', 
                    'Phosphorus (P) (mg)':'phosphorus_mg', 
                    'Iron (Fe) (mg)':'iron_mg', 
                    'Iodide (I) (µg)':'iodide_µg',
                    'Zinc (Zn) (mg)':'zinc_mg', 
                    'Selenium (Se) (µg)':'selenium_µg'}
    dataset.columns = [prefix + value for value in new_cols_mapping.values()]


def replace_non_numerical_values(dataset:pd.DataFrame)->None:
    """
    This method is used to clear values of the form '<0.4' from the dataset. In this case we subsitute them 
    with the numerical value. E.g: '<0.4' becomes '0.4'.

    Args:
        dataset: is the dataset we are modifying

    Returns:
        None since the change happens in place.    
    """
    count = dataset.astype(str).applymap(lambda x: x.count('<')).sum().sum()
    print("There are " + str(count) + " cells containing non-numerical values. Stripping '<'.")
    print("Done.")
    def extract_value(value):
        if '<' in str(value):
            return float(value.split('<')[1])
        else:
            return value
    # remove < only from numerical columns, starting from index 3
    dataset.iloc[:, 3:] = dataset.iloc[:, 3:].applymap(extract_value)


def replace_traces(dataset:pd.DataFrame)->None:
    """
    This method is used to remove all 'tr.' values, that stand for traces from the datase. We substitute them 
    with a small value defined in the value variable.

    Args:
        dataset: is the dataset we are modifying

    Returns:
        None since the change happens in place.    
    """
    tr_count = dataset.apply(lambda x: x.value_counts().get('tr.', 0))
    value = 0.0001
    print("In total found " + str(sum(tr_count))+ " traces. Replacing them with 0.0001")
    dataset = dataset.replace('tr.', value, inplace=True)