import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("Week_4/athlete_events_cleaned.csv")

mean_height_by_sport = df.groupby('Sport')['Height'].mean()

mean_height_by_sport.plot(kind='bar', title='Mean height by sport')
plt.xlabel('Sport')
plt.ylabel('Height')
plt.xticks(rotation=90)
plt.xticks(size=6)
plt.tight_layout()
plt.savefig("my_custom_chart.png")
plt.show()