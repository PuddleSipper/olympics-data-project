import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("Week_4/athlete_events_cleaned.csv")

df['Weight'].plot(kind='hist', bins=10, title='Distribution of Athlete Weights')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("weight_distribution.png")
plt.show()

