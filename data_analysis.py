# Importing Modules
import pandas as pd
import matplotlib.pyplot as plt

# Function to clean the data
def cleaning_data():    
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

data = cleaning_data()


# Visualisations

# 1. Global Yearly Trends in Migrant Deaths and Missing Cases through Travel Incidents
yearly = data.groupby('Incident Year')[['Number of Dead', 'Minimum Estimated Number of Missing']].sum()
yearly.plot(kind='bar', figsize=(12, 8), stacked=True, edgecolor='black')
plt.title('Global Yearly Trends in Migrant Deaths and Missing Cases through Travel Incidents')
plt.ylabel('Count')
plt.xlabel('Year')
plt.xticks(rotation=0)

missing_dead_yearly = yearly['Number of Dead'] + yearly['Minimum Estimated Number of Missing']
mean_value = missing_dead_yearly.mean()
min_value = missing_dead_yearly.min()
max_value = missing_dead_yearly.max()

plt.axhline(y=mean_value, color='orange', linestyle='-', linewidth=1.5, label="Mean: " + str(round(mean_value, 2)))
plt.axhline(y=min_value, color='red', linestyle='-', linewidth=1.5, label="Min: " + str(min_value))
plt.axhline(y=max_value, color='green', linestyle='-', linewidth=1.5, label="Max: " + str(max_value))

plt.legend(loc="upper center")
plt.savefig('Visualisations/yearly_trends.png')
plt.clf()


# 2. Global Count of Migrant Travel incidents by Month
monthly = data['Month'].value_counts(sort=False)
monthly.plot(kind='line', marker='o', figsize=(12, 8), color='darkblue')
plt.title('Global Count of Migrant Travel Incidents by Month')
plt.ylabel('Number of Incidents')
plt.xlabel('Month')
plt.xticks(range(len(monthly)), labels=monthly.index, rotation=0)  
plt.grid(alpha=0.5)
plt.tight_layout()

mean_value = monthly.mean()
min_value = monthly.min()
max_value = monthly.max()

plt.axhline(y=mean_value, color='orange', linestyle='-', linewidth=1.5, label="Mean: " + str(round(mean_value, 2)))
plt.axhline(y=min_value, color='red', linestyle='-', linewidth=1.5, label="Min: " + str(min_value))
plt.axhline(y=max_value, color='green', linestyle='-', linewidth=1.5, label="Max: " + str(max_value))

plt.legend(loc="upper left")
plt.savefig('Visualisations/monthly_trends.png')
plt.clf()


# 3. Global cause of death from incidents by Gender / Age

death_cause = data.copy()
# Abbreviating long causes of death
abbreviation_mapping = {
    "Mixed or unknown": "Unknown",
    "Vehicle accident / death linked to hazardous transport": "Transport Accident",
    "Sickness / lack of access to adequate healthcare": "No Healthcare",
    "Harsh environmental conditions / lack of adequate shelter, food, water": "Environmental",
    "Accidental death": "Accidental"
}
death_cause['Cause of Death'] = death_cause['Cause of Death'].replace(abbreviation_mapping)
death_cause_gender = death_cause.groupby('Cause of Death')[['Number of Females', 'Number of Males', 'Number of Children']].sum()

# stacked bar chart
death_cause_gender.plot(kind='bar', stacked=True, figsize=(12, 8), edgecolor='black', color=['orange', 'lightblue', 'lightgreen'])
plt.title('Global Causes of Migrant Deaths during Travel Incidents by Gender / Age')
plt.ylabel('Total Count')
plt.xlabel('Cause of Death')
plt.xticks(rotation=0)  
plt.legend(title='Number by Gender / Age', loc='upper right')
plt.grid(axis='y',alpha=0.5)
plt.tight_layout()
plt.savefig('Visualisations/death_trends.png')
plt.clf()



# Text file containing .describe() for each visualization
with open('Visualisations/Statistics.txt', 'w') as file:
    
    file.write("Visualisation 1: Global Yearly Trends in Migrant Deaths and Missing Cases through Travel Incidents\n")
    file.write(yearly.describe().to_string())
    file.write("\n\n")

    file.write("Visualisation 2: Global Count of Migrant Travel incidents by Month\n")
    file.write(monthly.describe().to_string())
    file.write("\n\n")

    file.write("Visualisation 3: Gender and Age Distribution Stacked by Causes of Death\n")
    file.write("Summary Statistics for Causes of Death:\n")
    file.write(death_cause['Cause of Death'].value_counts().to_string())
    file.write("\n\n")

    file.write("Summary of Gender and Age Counts by Cause of Death:\n")
    file.write(death_cause_gender.describe().to_string())
    file.write("\n\n")