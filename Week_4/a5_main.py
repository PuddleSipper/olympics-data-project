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

# Fill missing ages with median age
median_age = df_cleaned['Age'].median()
df_cleaned.loc[:, 'Age'] = df_cleaned['Age'].fillna(avg_age)

print(df_cleaned.head())
print(avg_age)
print(median_age)

# Unique values in 'Sex' and 'Medal'
print(df_cleaned['Sex'].unique())
print(df_cleaned['Medal'].unique())

# Check again for missing values
print(df_cleaned.isnull().sum())

# Get stats after cleaning
print(df_cleaned.describe())

# Save your cleaned version
df_cleaned.to_csv("athlete_events_cleaned.csv", index=False)