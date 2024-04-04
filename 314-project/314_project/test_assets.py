import assets 
import os
import pandas as pd

def test_load_data():
# test the assertion of the correct shape of the data
    data = assets.data()
    assert list(data.shape) == [5110,12]

test_load_data()

def test_drop_na():
# make a sample data frame with some null values and assert after running drop_na it is correct
    data = assets.data()
    NewData = assets.drop_na(data)
    sum_na = NewData.isna()
    assert all(~sum_na)
    
test_drop_na()

def test_make_binary():
# make a sample data frame with gender and ever_married columns and 
# assert after running make_binary that the columns are in fact binary 
    data = pd.DataFrame({"gender" : ['Male', 'Female', 'Other'], 
                         "ever_married": ["Yes", "No", "Yes"], 
                         "stroke" : [0, 1, 1]})
    data_op = assets.make_binary(data)
    data_bin = pd.DataFrame({"gender" : [0, 1, 2], 
                         "ever_married": [0, 1, 0], 
                         "stroke" : [0, 1, 1]})
    pd.testing.assert_frame_equal(data_op, data_bin)
test_make_binary()

def test_remove_cols():
    data = pd.DataFrame({"id" : [10], "smoking_status": ["yes"], "age" : [18], "gender" : [1]})
    pd.testing.assert_frame_equal(assets.remove_cols(data), pd.DataFrame({"age": [18], "gender": [1]}))
test_remove_cols()

def test_filter_adults():
    example_data =pd.DataFrame({'age' : [10, 9, 18, 40, 87, 32, 24], 
                                              'stroke' : [0, 0, 1, 0, 1, 1, 0],
                                              'heart_disease' : [0, 0, 0, 1, 1, 0, 0]})
    example_data
    data = assets.filter_adults(example_data)

    assert all(data['age'] >= 18)
    assert list(data.columns) == ['age', 'stroke', 'heart_disease']
    assert len(data) != 0
    assert all(~data.isna())
test_filter_adults()