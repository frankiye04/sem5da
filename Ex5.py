# ex5.py
import pandas as pd
df = pd.read_csv('D:\\ASP\\2025-26\\Odd Semester\\DA\\Duplicate_Data.csv')
print("Original DataFrame:")
print(df)
duplicate_rows = df[df.duplicated()]
print("\nDuplicate rows:")
print(duplicate_rows)
df = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df)
df.rename(columns={'old_column_name1': 'new_column_name1', 'old_column_name2': 'new_column_name2'}, inplace=True)
print("\nDataFrame after renaming columns:")
print(df)
