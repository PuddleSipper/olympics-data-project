import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("Week_4/athlete_events_cleaned.csv")

medal_counts = df[df['Medal'] != 'None']['Medal'].value_counts()

medal_counts.plot(kind='pie', autopct='%1.1f%%', title='Distribution of Medal Types')
plt.ylabel('')  # Removes default y-axis label
plt.tight_layout()
plt.savefig("medal_pie_chart.png")
plt.show()