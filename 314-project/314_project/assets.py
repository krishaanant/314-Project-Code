from dagster import asset
import pandas as pd

@asset
def load_data():
    data = pd.read_csv("/workspaces/314-Project-Code/314-project/data/healthcare-dataset-stroke-data.csv")

load_data()