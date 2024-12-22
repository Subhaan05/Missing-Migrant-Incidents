import os

def test_statistics_file_creation():
    # Check if file is created
    assert os.path.exists('Visualisations/Statistics.txt'), "The file was not created."

def test_statistics_file_not_empty():
    # Check if file is not empty
    assert os.path.getsize('Visualisations/Statistics.txt') > 0, "The file is empty."