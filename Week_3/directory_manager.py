import pandas as pd

# Demo: Reading CSV files using different relative paths

# 1. Reading a file in the same directory as this script
# df_same_dir = pd.read_csv('somefile.csv')

# 2. Reading a file in a sub-directory (e.g., Week_3/innie.csv)
df_innie = pd.read_csv('Week_3/gold_medalists.csv')
print("Reading from sub-directory (Week_3/innie.csv):")
print(df_innie.head())

# 3. Reading a file in the parent directory (e.g., ../outtie.csv)
df_outtie = pd.read_csv('../athlete_events.csv')
print("\nReading from parent directory (../athlete_events.csv):")
print(df_outtie.head())