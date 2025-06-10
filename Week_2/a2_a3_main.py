import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Show the first 5 rows
print(df.head())

# Show the column names
print(df.columns)

# Lists the Top 5 Sports
print(df['Sport'].value_counts().head())

# Lists how many player of each sex there were
print(df['Sex'].value_counts())

# Shows statistics about Age, ID, Height, Weight and Year with means, minimum and maximum values
print(df.describe())

# Shows country codes
print(df['NOC'].nunique())
print(df['NOC'].unique())