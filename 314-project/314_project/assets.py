from dagster import asset
import pandas as pd

#test: chloe 
@asset
def load_data():
    data = pd.read_csv("/workspaces/314-Project-Code/314-project/data/healthcare-dataset-stroke-data.csv")
    return data

@asset
# remove N/A rows Chloe 

# gender and ever_married columns to binary form (0,1) and remove "other" for gender column Krisha Tim-(pytest)

# remove id and smoking status columns Sonia

# filter for adults (> 18) in age column jimin

# ask about to_csv? 