# ex6.py
import pandas as pd
import numpy as np
df = pd.read_csv('D:\\ASP\\2025-26\\Odd Semester\\DA\\Data.csv')
numeric_df = df.select_dtypes(include=[np.number])
print("Basic Statistical Analysis of Numeric Columns:\n")
print(numeric_df.describe())
