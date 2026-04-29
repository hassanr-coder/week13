'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 13 Assignment 2
'''

import pandas as pd

# Task 1: Load the Dataset
df = pd.read_csv("employees.csv")
print("--- Task 1: First 5 Rows ---")
print(df.head())

# Task 2: Check for Missing Values
print("\n--- Task 2: Missing Values Count ---")
print(df.isnull().sum())

# Task 3: Handle Missing Values (Option A: Fill with Average)
# We calculate the mean and fill the empty spots in the salary column
avg_salary = df['salary'].mean()
df['salary'] = df['salary'].fillna(avg_salary)
print("\n--- Task 3: DataFrame after filling missing salaries ---")
print(df)

# Task 4: Filter Data Based on a Condition
# IT Department AND Salary > 65000
filtered_df = df[(df['department'] == 'IT') & (df['salary'] > 65000)]
print("\n--- Task 4: Filtered Results (IT & Salary > 65000) ---")
print(filtered_df)

# Task 5: Sort Data
# Sorting the filtered results by salary in descending order
sorted_df = filtered_df.sort_values(by='salary', ascending=False)
print("\n--- Task 5: Sorted Results (Salary Descending) ---")
print(sorted_df)

# Task 6: Calculate an Average
final_avg = df['salary'].mean()
print(f"\n--- Task 6: Final Average Salary ---")
print(f"The average salary for the dataset is: {final_avg:.2f}")