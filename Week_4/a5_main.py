import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Count missing values in each column
print(df.isnull().sum())

# Drop rows missing both height and weight
df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)

# Fill missing medals with 'None'
df_cleaned.loc[:, 'Medal'] = df_cleaned['Medal'].fillna('None')

# Fill missing ages with average age
avg_age = df_cleaned['Age'].mean()
df_cleaned.loc[:, 'Age'] = df_cleaned['Age'].fillna(avg_age)

print(df_cleaned.head())
