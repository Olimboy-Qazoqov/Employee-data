import pandas as pd
import numpy as np
import random
from faker import Faker

# Set random seed for reproducibility
np.random.seed(42)

#Set fake data for generating fake datas
fake = Faker()

# Number of rows
n_rows = 5000

# Generate synthetic dataset
departments = ["Sales", "HR", "IT", "Finance", "Marketing"]
regions = ["North", "South", "East", "West"]
genders = ["Male", "Female"]

data = {
    "EmployeeID": np.arange(1, n_rows + 1),
    "Name": [fake.name() for i in range(n_rows)],
    "Department": np.random.choice(departments, n_rows),
    "Region": np.random.choice(regions, n_rows),
    "Gender": np.random.choice(genders, n_rows),
    "Age": np.random.randint(20, 60, n_rows),
    "Salary": np.random.randint(30000, 120000, n_rows),
    "JoiningDate": pd.date_range(
        '2015-01-01', periods = n_rows, freq = 'D'
    ),
    "PerformanceScore": np.random.randint(1, 6, n_rows),  # 1-5 scale
    "Sales": np.random.randint(0, 50000, n_rows),
}

df = pd.DataFrame(data)

# Introduce some NaN values
for col in ["Age", "Salary", "PerformanceScore", "Sales"]:
    df.loc[df.sample(frac=0.02, random_state=random.randint(0, 100)).index, col] = np.nan

# Introduce some duplicate rows
duplicates = df.sample(50, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

#See which columns has Nan values for understanding what to fill with
df.isna().sum()

#Fill Nan values
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Age'] = df['Age'].fillna(df['Age'].median())
df['PerformanceScore'] = df['PerformanceScore'].ffill()
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

#Drop all duplicated data
df = df.drop_duplicates()

Tenure = 2025 - (df['JoiningDate'].dt.year).astype('int16')
df['Salary_per_year_experience'] = df['Salary'] / Tenure

#Categorizing Salaries
df['Category_salary'] = pd.cut(df['Salary'], bins = [30000, 50000, 100000, 120000], labels = ['Low', 'Medium', 'High']).astype('category')

#Converting datatypes accordingly 
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])
df['Department'] = df['Department'].astype('category')
df['EmployeeID'] = df['EmployeeID'].astype('str')

#Outlier values
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower_bounder = Q1 - 1.5 * IQR
higher_bounder = Q3 + 1.5 * IQR
df['is_outlier'] = (df['Salary'] < lower_bounder) | (df['Salary'] > higher_bounder)

#If below shows 0 that means there is no outliers in Salary column
df['is_outlier'].sum()

#Exporting cleaned dataset to csv file
df.to_csv('Cleaned_employee_dataset.csv', index=False)
