import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Sample dataset
data = {
    'Name': ['John', 'Mary', 'Sam', 'David'],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Age': [20, 22, 21, 23],
    'Marks': [85, None, 78, 92]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])

df['Age_Marks_Ratio'] = df['Marks'] / df['Age']
scaler = MinMaxScaler()
df[['Marks', 'Age_Marks_Ratio']] = scaler.fit_transform(
    df[['Marks', 'Age_Marks_Ratio']]
)

print("\nFeature Engineered Dataset:")
print(df)