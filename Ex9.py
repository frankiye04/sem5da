import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Enter File Location')
print("Original Dataset:")
print(df)
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Value'])
plt.title("Boxplot to Detect Outliers")
plt.show()
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
filtered_df = df[(df['Value'] >= lower_bound) & (df['Value'] <= upper_bound)]
print("\nFiltered Dataset (Outliers Removed):")
print(filtered_df)
plt.figure(figsize=(6, 4))
sns.boxplot(x=filtered_df['Value'])
plt.title("Boxplot After Removing Outliers")
plt.show()
