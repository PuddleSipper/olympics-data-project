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
sorted_by_height = df.sort_values(by=['Height', 'Weight'], ascending=False)
print(sorted_by_weight[['Name', 'Height', 'Weight', 'Sport']].head())

# Count participants in each sport
sport_counts = df['Sport'].value_counts()
print(sport_counts.head())

# Count medals per team
medals_by_team = df[df['Medal'].notnull()].groupby('Team')['Medal'].count()
print(medals_by_team.sort_values(ascending=False).head())

# My code for female participants
female_athletes_by_sport = df[df['Sport'].notnull()].groupby('Sex')['Sport'].value_counts()
print(female_athletes_by_sport.sort_values(ascending=False).head())

# Average height per sport
avg_height = df.groupby('Sport')['Height'].mean().sort_values(ascending=False)
print(avg_height.head())

# Median age by year
median_age_by_year = df.groupby('Year')['Age'].median()
print(median_age_by_year.tail())

# My code for average weight by sex and sport
avg_weight_by_sex_and_sport = df.groupby(['Sex', 'Sport'])['Weight'].mean().sort_values(ascending=False)
print(avg_weight_by_sex_and_sport)

# Filter gymnasts and save to new CSV
gymnasts = df[df['Sport'] == 'Gymnastics']
gymnasts.to_csv('gymnastics_athletes.csv', index=False)

# My code for athletes under 18 and gold medalists
under_18s = df[df['Age'] < 18]
under_18s.to_csv('under_18_athletes.csv', index=False)
gold_medalists = df[df['Medal'] == 'Gold']
gold_medalists.to_csv('gold_medalists.csv', index=False)
