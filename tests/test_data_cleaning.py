import pandas as pd

def load_cleaned_data():
    
    # Load and clean the dataset
    
    data = pd.read_csv('Missing_Migrants_Global_Figures_allData.csv')

    # Drop unwanted columns
    unwanted_columns = ['Main ID', 'Incident ID', 'UNSD Geographical Grouping', 'URL', 'Source Quality', 'Information Source']
    data = data.drop(columns=unwanted_columns)

    # Rename columns
    columns_names = {
        'Region of Incident': 'Incident Region',
        'Date of Incident': 'Incident Date',
        'Year of Incident': 'Incident Year',
        'Number of Dead': 'Death Toll',
        'Minimum Estimated Number of Missing': 'Estimated Missing Count',
        'Total Number of Dead and Missing': 'Total Missing and Dead',
        'Number of Survivors': 'Survivors Count',
        'Number of Females': 'Females Count',
        'Number of Males': 'Males Count',
        'Number of Children': 'Children Count',
        'Country of Origin': 'Origin Country',
        'Region of Origin': 'Origin Region',
        'Country of Incident': 'Incident Country',
        'Location of Death': 'Incident Location',
    }
    data.rename(columns=columns_names, inplace=True)

    # Set Null to 0 for death count
    data['Death Toll'] = data['Death Toll'].fillna(0)

    print(list(data.columns))  # Add this line to inspect the actual column names

    return data


def test_unwanted_columns_removed():
    # Test if unwanted columns are removed
    data = load_cleaned_data()
    unwanted_columns = ['Main ID', 'Incident ID', 'UNSD Geographical Grouping', 'URL', 'Source Quality', 'Information Source']
    assert all(col not in data.columns for col in unwanted_columns), "Unwanted columns were not removed."

def test_columns_renamed():
    # Test if columns are renamed correctly
    data = load_cleaned_data()
    expected_columns = [
        'Incident Type', 'Incident Region', 'Incident Date', 'Incident Year', 'Month',
        'Death Toll', 'Estimated Missing Count', 'Total Missing and Dead',
        'Survivors Count', 'Females Count', 'Males Count', 'Children Count',
        'Origin Country', 'Origin Region', 'Cause of Death', 'Incident Country',
        'Migration Route', 'Location of Incident', 'Coordinates'
    ]
    assert list(data.columns) == expected_columns, "Columns were not renamed correctly."
    
def test_death_toll_nulls_filled():
    # Test if null values in death count are set to 0
    data = load_cleaned_data()
    assert data['Death Toll'].isnull().sum() == 0, "Null values in Death Toll were not replaced with 0."