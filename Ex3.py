# ex3.py
import pandas as pd
df = pd.read_csv('D:\\ASP\\2025-26\\Odd Semester\\DA\\Data.csv')
print("First five rows of the dataset:")
print(df.head())
print("\nShape of the dataset (rows, columns):")
print(df.shape)
print("\nColumn names and data types:")
print(df.dtypes)
