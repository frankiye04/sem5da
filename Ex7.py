# ex7.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    'rooms': [3, 4, 2, 5, 3],
    'area': [1000, 1500, 800, 2000, 1200],
    'age': [10, 5, 20, 2, 15],
    'price': [300000, 400000, 250000, 500000, 320000]
}
df = pd.DataFrame(data)
correlation_matrix = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='YlGnBu', fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()
target_feature = 'price'
cor_target = correlation_matrix[target_feature].drop(target_feature)
high_correlation = cor_target[abs(cor_target) > 0.5]
print("Highly correlated features with target (price):")
print(high_correlation)
