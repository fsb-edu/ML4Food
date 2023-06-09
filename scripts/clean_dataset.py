import pandas as pd
import numpy as np

def read_dataset_in_dataframe(path2data)->pd.DataFrame:
    """Reading the dataset into a pandas dataframe.
    
        Args:
            None
        Returns:
            The dataframe holding the dataset.
    """
    # header is 3 since the header is the third row in the Excel file
    dataset = pd.read_excel(path2data, header=2)
    return dataset


def drop_unnecessary_cols(dataset:pd.DataFrame)-> pd.DataFrame:
    """
    The first step is to select only the columns that we want to
    keep. We need to remove all Source and Derivation of Value columns,
    Synonyms, ID V 4.0 from the columns. The change happens in place,
    so the method does not return anything.
    
    Args:
        dataset: is the dataset whose columns will be modified.
    
    Returns:
        the dataframe after the columns are dropped.
    """
    df = dataset.copy(deep=True)
    sources_to_drop = ["Source."+str(i) for i in range(1,40)]
    derivations_to_drop = ["Derivation of value." + str(i) for i in range(1,40)]
    # additional columns to drop
    cols_to_drop = [
        "Source", "Derivation of value", "Density", "Synonyms", "ID V 4.0", 
        "Matrix unit", "ID SwissFIR","Energy, kilojoules (kJ)", "Record has changed"]
    cols_to_drop.extend(sources_to_drop)
    cols_to_drop.extend(derivations_to_drop)
    df = dataset.drop(columns=cols_to_drop, axis=1)
    return df


def rename_columns (dataset:pd.DataFrame) -> pd.DataFrame:
    """
    The second step is to rename the columns. We will use this procedure:
    take the first word and the unit of measure and concatenate them with
    a prefix of f_, where f will stand for feature. 
    E.g: "Energy, kilocalories (kcal)" -> "f_energy_kcal". 
    The changes will happen in place so the method will not return anything.
    
    Args:
        dataset: is the dataset we are modifying

    Returns:
        the modified dataframe after renaming the columns.
    """
    df = dataset.copy(deep=True)
    prefix = ""
    new_cols_mapping = {"ID":"ID", 
                    "Name":"name", 
                    "Category":"category", 
                    "Energy, kilocalories (kcal)": "energy_kcal",
                    "Fat, total (g)":"fat_g", 
                    "Fatty acids, saturated (g)": 
                    "fatty_acids_sat_g",
                    "Fatty acids, monounsaturated (g)":"fatty_acids_monounsat_g", 
                    "Fatty acids, polyunsaturated (g)":"fatty_acids_polyunsat_g",
                    "Cholesterol (mg)":"cholesterol_mg", 
                    "Carbohydrates, available (g)":"carbohydrates_g", 
                    "Sugars (g)":"sugars_g", 
                    "Starch (g)":"starch_g",
                    "Dietary fibres (g)":"fibres_g", 
                    "Protein (g)":"protein_g", 
                    "Salt (NaCl) (g)":"salt_g", 
                    "Alcohol (g)":"alcohol_g", 
                    "Water (g)":"water_g", 
                    "Vitamin A activity, RE (µg-RE)":"vit_A_activity_re_µg", 
                    "Vitamin A activity, RAE (µg-RE)":"vit_A_activity_rae_µg", 
                    "Retinol (µg)":"retinol_µg", 
                    "Beta- carotene activity (µg-BCE)":"beta_carotene_activity_µg", 
                    "Beta-carotene (µg)":"beta_carotene_µg", 
                    "Vitamin B1 (thiamine) (mg)":"vit_B1_mg", 
                    "Vitamin B2 (riboflavin) (mg)":"vit_B2_mg", 
                    "Vitamin B6 (pyridoxine) (mg)":"vit_B6_mg", 
                    "Vitamin B12 (cobalamin) (µg)":"vit_B12_µg", 
                    "Niacin (mg)":"niacin_mg", 
                    "Folate (µg)":"folate_µg", 
                    "Panthotenic acid (mg)":"panthotenic_acid_mg",
                    "Vitamin C (ascorbic acid) (mg)":"vit_c_mg", 
                    "Vitamin D (calciferol) (µg)":"vit_d_µg", 
                    "Vitamin E activity (mg-ATE)":"vit_e_activity_mg", 
                    "Potassium (K) (mg)":"potassium_mg", 
                    "Sodium (Na) (mg)":"sodium_mg",
                    "Chloride (Cl) (mg)":"chloride_mg", 
                    "Calcium (Ca) (mg)":"calcium_mg", 
                    "Magnesium (Mg) (mg)":"magnesium_mg", 
                    "Phosphorus (P) (mg)":"phosphorus_mg", 
                    "Iron (Fe) (mg)":"iron_mg", 
                    "Iodide (I) (µg)":"iodide_µg",
                    "Zinc (Zn) (mg)":"zinc_mg", 
                    "Selenium (Se) (µg)":"selenium_µg"}
    df.columns = [prefix + value for value in new_cols_mapping.values()]
    return df


def replace_non_numerical_values(dataset:pd.DataFrame)->pd.DataFrame:
    """
    This method is used to clear values of the form "<0.4" from the dataset.
    In this case we subsitute them with the numerical value. E.g: "<0.4" becomes "0.4".

    Args:
        dataset: is the dataset we are modifying

    Returns:
        the dataframe without the non-numerical values    
    """
    df = dataset.copy(deep=True)
    count = df.astype(str).applymap(lambda x: x.count("<")).sum().sum()
    print(f"There are {count} cells containing non-numerical values. Stripping "<".")
    print("Done.")
    def extract_value(value):
        if "<" in str(value):
            return float(value.split("<")[1])
        else:
            return value
    # remove < only from numerical columns, starting from index 3
    df.iloc[:, 3:] = df.iloc[:, 3:].applymap(extract_value)
    return df


def add_new_category(dataset:pd.DataFrame)->pd.DataFrame:
    """ 
    This method will add a new category column to the dataset. This new 
    category will be a more generalized version of the existing column of the dataset. 
    In total, there will be 13 new categories.

    Args:
        dataset: is the dataset that we are modifying
    
    Returns:
        the modified dataframe with the category_new column
    """
    new_categories_dict = {
        "dairy":"dairy", 
        "non-alcoholic beverages":"non_alcoholic_beverages", 
        "alcoholic beverages":"alcoholic_beverages",
        "sweet":"sweets",
        "fruit":"fruits",
        "herbs":"herbs", 
        "vegetable":"vegetables",
        "cereal":"cereals",
        "bread":"bread",
        "sauces":"sauce",
        "meat":"meat",
        "nut":"nuts"
    }
    keys = new_categories_dict.keys()
    n_cols = len(dataset.columns)
    dataset["category_new"] = np.zeros((dataset.shape[0], 1))

    for i, value in enumerate(dataset["category"]):
        for word in keys:
            if word in value.lower():
                dataset.iloc[i, n_cols] = new_categories_dict[word]
                break
            else:
                dataset.iloc[i, n_cols] = "other"
    dataset["category"] = dataset["category_new"] 
    dataset = dataset.drop(columns=["category_new"])
    return dataset

def replace_traces(dataset:pd.DataFrame)->pd.DataFrame:
    """
    This method is used to remove all "tr." values, that stand for traces from the 
    database. We substitute them with a small value defined in the value variable.

    Args:
        dataset: is the dataset we are modifying

    Returns:
        the dataframe without the "t.r." values    
    """
    df = dataset.copy(deep=True)
    tr_count = df.apply(lambda x: x.value_counts().get("tr.", 0))
    value = 0.0001
    print("In total found " + str(sum(tr_count))+ " traces. Replacing them with 0.0001")
    df = df.replace("tr.", value)
    return df

def replace_nd_values(dataset:pd.DataFrame)->pd.DataFrame:
    """
    This method is used to remove all "n.d." values, that stand for missing values from
    the dataset. We substitute them with np.nan.

    Args:
        dataset: is the dataset we are modifying

    Returns:
        the dataframe without the "n.d." values    
    """
    
    df = dataset.copy(deep=True)
    df = df.replace("n.d.", np.nan)
    return df



def process_dataset(path2data)->pd.DataFrame:
    """This is the driver method that will starts the processing process. It will
    return the clean and ready to use dataset.
    Args:
        None
    Returns:
        pd.Dataframe - the clean dataframe
    """
    clean_dataset = read_dataset_in_dataframe(path2data)
    clean_dataset = drop_unnecessary_cols(clean_dataset)
    clean_dataset = rename_columns(clean_dataset)
    clean_dataset = replace_non_numerical_values(clean_dataset)
    clean_dataset = replace_traces(clean_dataset)
    clean_dataset = replace_nd_values(clean_dataset)
    clean_dataset = clean_dataset.drop(columns=["ID"])
    clean_dataset = add_new_category(clean_dataset)
    clean_dataset["energy_kcal"] = clean_dataset["energy_kcal"].astype("float64")
    print("Done. Clean dataset ready.")
    return clean_dataset