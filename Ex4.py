# ex4.py
import pandas as pd
df = pd.read_csv('D:\\ASP\\2025-26\\Odd Semester\\DA\\Missing_Data.csv')
print("Missing values in each column:")
print(df.isnull().sum())
for column in df.columns:
    if df[column].isnull().sum() > 0:
        if df[column].dtype == 'object':
            df[column].fillna('Unknown', inplace=True)
        else:
            df[column].fillna(df[column].mean(), inplace=True)
print("\nMissing values after filling:")
print(df.isnull().sum())
