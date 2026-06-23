import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv('data.csv')
X = df[['hours']]
y = df['score']
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[6]])
print("Predicted Score for 6 hours:", prediction[0])