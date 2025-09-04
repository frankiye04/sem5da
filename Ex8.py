import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Enter File Location') 
print("Dataset Preview:")
print(df.head(10))
feature = df['Feature']
target = df['Target']
plt.scatter(feature,target)
plt.title("Scatter Plot: Feature vs Target")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.grid(True)
plt.show()
