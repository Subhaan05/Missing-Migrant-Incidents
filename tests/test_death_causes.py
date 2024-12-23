import os
import pandas as pd
import matplotlib.pyplot as plt


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

# testing death cause visualisation
def test_death_cause_visualisation():

    data = load_cleaned_data()

    abbreviation_mapping = {
        "Mixed or unknown": "Unknown",
        "Vehicle accident / death linked to hazardous transport": "Transport Accident",
        "Sickness / lack of access to adequate healthcare": "No Healthcare",
        "Harsh environmental conditions / lack of adequate shelter, food, water": "Environmental",
        "Accidental death": "Accidental"
    }
    data['Cause of Death'] = data['Cause of Death'].replace(abbreviation_mapping)
    grouped_data = data.groupby('Cause of Death')[['Number of Females', 'Number of Males', 'Number of Children']].sum()

    # Test if grouped data is empty
    assert not grouped_data.empty, "Grouped data is empty."

    # Test if file was created
    assert os.path.exists('Visualisations/death_trends.png'), "The file was not created."