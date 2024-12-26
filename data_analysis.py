# Importing Modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal


# Function to clean the data
def cleaning_data():    
    # Reading the dataset
    data = pd.read_csv('Missing_Migrants_Global_Figures_allData.csv')

    print("Shape of the data before pre-processing:", data.shape)
    
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

    print("Shape of the data after pre-processing:", data.shape)
    print("Number of missing values in each column:\n", data.isnull().sum())
    
    return data


data = cleaning_data()
print(data.head(5))

# Visualisations

# 1. Global Count of Migrant Travel incidents by Month
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
plt.figtext(0.5, -0.05, "Figure 2: Global Count of Migrant Travel Incidents by Month\nThis figure shows the monthly count of travel incidents, highlighting seasonal trends.\nThe trend reveals peak incidents occur frime June to October, then dip significantly below the mean.", ha="center")
plt.savefig('Visualisations/monthly_trends.png', bbox_inches='tight')
plt.clf()

# 2. Global Yearly Trends in Migrant Deaths and Missing Cases through Travel Incidents
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
plt.figtext(0.5, -0.002, "Figure 3: Global Yearly Trends in Migrant Deaths and Missing Cases through Travel Incidents\nThis figure displays yearly totals of migrant deaths and missing cases stacked together.\nThe trend shows 2016 and 2023 far above the rest, pulling the mean up as there are only 4 years above the mean.", ha="center")
plt.savefig('Visualisations/yearly_trends.png', bbox_inches='tight')
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
plt.figtext(0.5, -0.05, "Figure 4: Global Causes of Migrant Deaths during Travel Incidents by Gender / Age\nThis figure shows causes of migrant deaths, categorised by gender and age group.\nDrowning emerges as the leading cause of death, affecting all age groups. Males are the largest demographic group by number of deaths.", ha="center")
plt.savefig('Visualisations/death_trends.png', bbox_inches='tight')
plt.clf()


# 4. Count of Travel Incidents by Migration Route and Year
heatmap = data.groupby(['Migration Route', 'Incident Year']).size().unstack(fill_value=0)
plt.figure(figsize=(16, 8))
sns.heatmap(heatmap, cmap="YlGnBu", annot=True, fmt='d', linewidths=0.5)
plt.title('Count of Travel Incidents by Migration Route and Year')
plt.xlabel('Year',)
plt.ylabel('Migration Route')
plt.tight_layout()
plt.figtext(0.5, -0.05, "Figure 5: Count of Travel Incidents by Migration Route and Year\nThis heatmap summarises the count of travel incidents across migration routes over time, highlighting high-risk routes.\nThere are 3 routes that have caused a large number of deaths, Afganisatan to Iran, the Sahara Desert crossing and the US-Mexico border crossing.", ha="center")
plt.savefig('Visualisations/migration_trends.png', bbox_inches='tight')
plt.clf()

# 5. Count of Travel Incidents by Region of Incident and Year
region_year = data.groupby(['Region of Incident', 'Incident Year']).size().unstack(fill_value=0)
region_year.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='viridis', edgecolor='black')
plt.title('Count of Travel Incidents by Region of Incident')
plt.ylabel('Number of Incidents')
plt.xlabel('Region')
plt.legend(title='Year', loc='upper right')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.figtext(0.5, -0.05, "Figure 6: Count of Travel Incidents by Region of Incident\nThis stacked bar chart displays the number of travel incidents across regions, broken down by year.\nNorth America and Southern Asia regions report the highest number of incidents.", ha="center")
plt.savefig('Visualisations/region_trends.png', bbox_inches='tight')
plt.clf()

    # Kruskal-Wallis test calculation
    
region_incidents = [region_year.loc[region].values for region in region_year.index]
h_stat, p_value = kruskal(*region_incidents)



    
# Text file containing .describe() for each visualization
with open('Visualisations/Statistics.txt', 'w') as file:
    
    file.write("Visualisation 1: Global Count of Migrant Travel incidents by Month\n")
    file.write(monthly.describe().to_string())
    file.write("\n\n")
    
    file.write("Visualisation 2: Global Yearly Trends in Migrant Deaths and Missing Cases through Travel Incidents\n")
    file.write(yearly.describe().to_string())
    file.write("\n\n")

    file.write("Visualisation 3: Gender and Age Distribution Stacked by Causes of Death\n")
    file.write(death_cause['Cause of Death'].value_counts().to_string())
    file.write("\n\n")

    file.write("Summary of Gender and Age Counts by Cause of Death:\n")
    file.write(death_cause_gender.describe().to_string())
    file.write("\n\n")
    
    file.write("Visualisation 4: Count of Travel Incidents by Migration Route and Year\n")
    file.write(heatmap.describe().to_string())
    file.write("\n\n")
    
    file.write("Visualisation 5: Count of Travel Incidents by Region of Incident\n")
    file.write(region_year.describe().to_string())
    file.write("\n\n")
    file.write("Kruskal-Wallis Test Results for Visualisation 5:\n")
    file.write(f"H-Statistic: {h_stat:.5f}\n")
    file.write(f"P-Value: {p_value:.5f}\n")
    file.write("\n\n")