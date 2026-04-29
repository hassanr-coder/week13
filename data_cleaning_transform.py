'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 13 Assignment 3
Code Helper - Gemini Google AI
'''

import pandas as pd

# Task 1: Load the Dataset
df = pd.read_csv("sales_data.csv")
print("--- Task 1: Initial Data ---")
print(df.head())

# Task 2: Check for Missing Values
print("\n--- Task 2: Missing Values Count ---")
print(df.isnull().sum())

# Task 3: Handle Missing Values
# Median for units_sold, Mean for unit_price
df['units_sold'] = df['units_sold'].fillna(df['units_sold'].median())
df['unit_price'] = df['unit_price'].fillna(df['unit_price'].mean())
print("\n--- Task 3: Data After Filling Missing Values ---")
print(df)

# Task 4: Remove Duplicate Rows
print(f"\n--- Task 4: Duplicates ---")
print(f"Rows before: {len(df)}")
df = df.drop_duplicates()
print(f"Rows after: {len(df)}")

# Keep a copy for Task 7 before we do One-Hot Encoding
df_cleaned = df.copy()

# Task 5: Convert Categorical Data into Numerical (One-Hot Encoding)
# This creates new columns for each Region and Product
df_encoded = pd.get_dummies(df, columns=['region', 'product'])
print("\n--- Task 5: Columns after One-Hot Encoding ---")
print(df_encoded.columns.tolist())

# Task 6: Normalize Numerical Values (Min-Max Normalization)
# Formula: (x - min) / (max - min)
for col in ['units_sold', 'unit_price']:
    df_encoded[col] = (df_encoded[col] - df_encoded[col].min()) / (df_encoded[col].max() - df_encoded[col].min())

print("\n--- Task 6: Normalized Columns (0-1 Range) ---")
print(df_encoded[['units_sold', 'unit_price']].head())

# Task 7: Group Data and Calculate Summary Statistics
# We use the copy we made before encoding so 'region' still exists
summary = df_cleaned.groupby('region').agg({
    'units_sold': 'sum',
    'unit_price': 'mean'
})
print("\n--- Task 7: Grouped Summary by Region ---")
print(summary)