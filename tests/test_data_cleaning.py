import pandas as pd

def load_cleaned_data():
    # Function to clean the data
    
    # Reading the dataset
    data = pd.read_csv('Missing_Migrants_Global_Figures_allData.csv')

    # Keep only required columns
    required_columns = [
        'Incident Type', 'Incident Year', 'Month', 'Region of Origin', 'Region of Incident',
        'Country of Origin', 'Number of Dead', 'Minimum Estimated Number of Missing',
        'Total Number of Dead and Missing', 'Number of Survivors', 'Number of Females',
        'Number of Males', 'Number of Children', 'Cause of Death', 'Migration Route',
        'Location of Incident', 'Coordinates', 'UNSD Geographical Grouping'
    ]

    data = data[required_columns]


    # Handle missing values
    
    data['Number of Dead'] = data['Number of Dead'].fillna(0)
    data['Minimum Estimated Number of Missing'] = data['Minimum Estimated Number of Missing'].fillna(0)
    data['Total Number of Dead and Missing'] = data['Total Number of Dead and Missing'].fillna(0)
    data['Number of Survivors'] = data['Number of Survivors'].fillna(0)
    data['Number of Females'] = data['Number of Females'].fillna(0)
    data['Number of Males'] = data['Number of Males'].fillna(0)
    data['Number of Children'] = data['Number of Children'].fillna(0)

    data['Region of Origin'] = data['Region of Origin'].fillna('Unknown')
    data['Country of Origin'] = data['Country of Origin'].fillna('Unknown')
    data['Migration Route'] = data['Migration Route'].fillna('Unknown')
    data['Cause of Death'] = data['Cause of Death'].fillna('Unknown')

    data = data.dropna()

    print("Shape of the data:", data.shape)    
    print("Number of missing values in each column:\n", data.isnull().sum())
    
    return data



def test_required_columns():
    # Test if the required columns are present
    data = load_cleaned_data()
    required_columns = [
        'Incident Type', 'Incident Year', 'Month', 'Region of Origin', 'Region of Incident',
        'Country of Origin', 'Number of Dead', 'Minimum Estimated Number of Missing',
        'Total Number of Dead and Missing', 'Number of Survivors', 'Number of Females',
        'Number of Males', 'Number of Children', 'Cause of Death', 'Migration Route',
        'Location of Incident', 'Coordinates', 'UNSD Geographical Grouping'
    ]
    for col in required_columns:
        assert col in data.columns, "Required column '" + col + "' is missing."
    for col in data.columns:
        assert col in required_columns, "Unexpected column '" + col + "' is present."
        
def test_no_nulls():
    # Test that no null values exist in the dataset
    data = load_cleaned_data()
    assert data.isnull().sum().sum() == 0, "Null values are present in the dataset."
