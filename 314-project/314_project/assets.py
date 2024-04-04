from dagster import asset
import pandas as pd

#test: chloe 
@asset
def data():
    data = pd.read_csv("/workspaces/314-Project-Code/314-project/data/healthcare-dataset-stroke-data.csv") 
    return data

# remove N/A rows - Chloe 
@asset
def drop_na(data) -> pd.DataFrame:
    newData = data.dropna()
    return newData

# gender and ever_married columns to binary form (0,1) and remove "other" for gender column Krisha Tim-(pytest)

@asset
def make_binary(drop_na):
    data_cols = ['gender', 'ever_married']
    for data_col in data_cols:
        unique = drop_na[data_col].unique().tolist()
        for index, value in drop_na[data_col].items():
            if value in unique:
                drop_na.at[index, data_col] = int(unique.index(value))
        drop_na[data_col] = drop_na[data_col].astype(int)
    return drop_na

# remove id and smoking status columns - Sonia
@asset
def remove_cols(make_binary: pd.DataFrame) -> pd.DataFrame:
    col_list = ["id", "smoking_status"]
    data = make_binary.drop(col_list, axis = 1)
    return data

# filter for adults (> 18) in age column - Jimin
@asset
def filter_adults(remove_cols : pd.DataFrame) -> pd.DataFrame:
    filter = remove_cols['age'] >= 18
    return remove_cols[filter]
