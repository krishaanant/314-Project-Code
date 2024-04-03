from 314_project import assets
import pandas as pd

def test_remove_cols():
    data = pd.DataFrame({"id" : [10], "smoking": ["yes"], "age" : [18], "gender" : [1]})
    list = ["age", "smoking"]
    pd.testing.assert_frame_equal(remove_cols(data, list), pd.DataFrame({"id": [10], "gender": [1]}))


