from 314_project import assets
import pandas as pd

def test_remove_cols():
    data = pd.DataFrame({"id" : [10], "smoking": ["yes"], "age" : [18], "gender" : [1]})
    list = ["age", "smoking"]
    pd.testing.assert_frame_equal(remove_cols(data, list), pd.DataFrame({"id": [10], "gender": [1]}))

def test_load_data():
# test the assertion of the correct shape of the data

def test_drop_na():
# make a sample data frame with some null values and assert after running drop_na it is correct

