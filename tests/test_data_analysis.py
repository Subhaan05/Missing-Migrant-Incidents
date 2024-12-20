import os
import pandas as pd

def test_file_exists():
    #Test if the dataset file exists
    assert os.path.exists('Missing_Migrants_Global_Figures_allData.csv'), "The dataset file is missing."

def test_file_readable():
    #Test if the dataset can be read without errors
    data = pd.read_csv('Missing_Migrants_Global_Figures_allData.csv')
    assert data is not None, "The dataset could not be read."

def test_data_not_empty():
    # if the dataset is not empty
    data = pd.read_csv('Missing_Migrants_Global_Figures_allData.csv')
    assert len(data) > 0, "The dataset is empty."