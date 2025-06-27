import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("Week_4/athlete_events_cleaned.csv")

median_age = df.groupby('Year')['Age'].median()

median_age.plot(kind='line', title='Median Athlete Age Over Time')
plt.xlabel('Olympic Year')
plt.ylabel('Median Age')
plt.grid(True)
plt.tight_layout()
plt.savefig("median_age_line.png")
plt.show()

