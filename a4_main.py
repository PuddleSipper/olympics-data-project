import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())
print("Rows:", len(female_athletes))

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(older_athletes[['Name', 'Age', 'Sport']].head())
print("Rows:", len(older_athletes))

# Testing combined filter

# Female athletes over 30
combo_filter = df[(df['Sex'] == 'F') & (df['Age'] > 30)]
print(combo_filter[['Name', 'Age', 'Sport']].head())
print("Rows:", len(combo_filter))

# Male athletes in Basketball
basketball_males = df[(df['Sex'] == 'M') & (df['Sport'] == 'Basketball')]
print(basketball_males.head())
print("Rows:", len(basketball_males))

# My own filter for Australian Swimmers

australian_swimmers = df[(df['NOC'] == 'AUS') & (df['Sport'] == 'Swimming')]
print(australian_swimmers.head())
print("Rows", len(australian_swimmers))

# Testing sorting

# Sort by age
sorted_by_age = df.sort_values(by='Age', ascending=False)
print(sorted_by_age[['Name', 'Age', 'Sport']].head())

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head())

# My own sorting code for "height then weight"
