# Exploring Missing Migrant Incidents
## An Analysis of Trends and Patterns

---
## 1. Overview
This repository contains the analysis and visualisations of a dataset aimed at migrant incidents occuring as a result of a migrants journey. The dataset contains various aspects of migrants and their journey. With this, I have examined the routes, causes of death, regionality and temporal aspects that migrants have delt with globally to shed light on patterns on insights that can help to understand the challenges faced, and what can be done about it.

The tragic loss of life among migrants inspired this analysis. The goal of this project is to identify trends in migrant incidents and provide insights for policy creation.

The hypothesis investigated was:
> "The number and severity of migrant travel incidents vary across regions, migration routes, and causes of death, influenced by time, geographical hazards, migration policies, and socioeconomic conditions."

---

## 2. Project Structure
- **`.circleci/`**: Configuration files for CircleCI integration for testing every commit.
- **`Visualisations/`**: Stores all visualisations related to the analysis.
- **`tests/`**: Includes all test files ran by CircleCI for every commit.
- **`.gitignore`**: Specifies files and folders to be ignored by Git.
- **`Missing_Migrants_Global_Figures_allData.csv`**: The dataset used for the analysis.
- **`README.md`**: Project documentation.
- **`data_analysis.py`**: Python script for data cleaning, data analysis, and creating visualisations.
- **`requirements.txt`**: Lists Python dependencies needed to run the analysis.

---

## 3. Dataset
The dataset was sourced from the Missing Migrants Project, by the International Organization For Migration:
- **Size**: 17,474 rows and 25 columns before preprocessing.
- **Pre-processing**: Removed unnecessary columns, handled null values, and filtered data for analysis.

The dataset provides information on:
- Incident date, migration routes, and causes of death.
- Demographic details such as gender and age.
- Total number of dead and missing.

---

## 4. How to Run
To run the analysis locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/Subhaan05/Missing-Migrant-Incidents.git
   cd Missing-Migrant-Incidents
 2. Install the required dependencies from 'requrements.txt':
    ```bash
    pip install -r requirements.txt

4. Run the data anlysis script - 'data_analysis.py':
   ```bash
   python data_analysis.py

6. To execute the test suite:
    ```bash
    pytest tests/

7. View the visualisations:

   Navigate inside the 'Visualisations/' folder to do so.
