import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df = pd.read_csv('Enter File Location')
X = df[['Feature']]   
y = df['Target']       
model = LinearRegression()
model.fit(X,y)
predictions = model.predict(X)
print("Predicted Target Values:")
print(predictions)
plt.scatter(X,y,color='blue',label='Actual')
plt.plot(X,predictions,color='red',label='Predicted')
plt.title("Linear Regression Fit")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.legend()
plt.grid(True)
plt.show()
