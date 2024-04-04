from dagster import asset
import pandas as pd

#test: chloe 
@asset
def load_data():
    data = pd.read_csv("/workspaces/314-Project-Code/314-project/data/healthcare-dataset-stroke-data.csv")
    return data

# remove N/A rows Chloe 
@asset
def drop_na(data):
    newData = data.dropna()
    return newData

# gender and ever_married columns to binary form (0,1) and remove "other" for gender column Krisha Tim-(pytest)
@asset
def make_binary(data, data_col):
    unique = data[data_col].unique().tolist()
    for index, value in data[data_col].items():
        if value in unique:
            data.at[index, data_col] = unique.index(value)
    return data

# remove id and smoking status columns Sonia
@asset
def remove_cols(data, col_list):
    data = data.drop(col_list, axis = 1)
    return data

# filter for adults (> 18) in age column jimin

# ask about to_csv? 