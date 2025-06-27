import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("Week_4/athlete_events_cleaned.csv")

sport_counts = df['Sport'].value_counts().head(10)

sport_counts.plot(kind='bar', title='Top 10 Sports by Athlete Count')
plt.xlabel('Sport')
plt.ylabel('Number of Athletes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_10_sports.png")
plt.show()