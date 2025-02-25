import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "D:\PythonProject\cricketcase\cricket_data.csv"  # Update with your file path if needed
df = pd.read_csv(file_path)

# Convert numerical columns to appropriate data types
df_numeric = df.drop(columns=['Year', 'Player_Name', 'Matches_Batted', 'Not_Outs','Catches_Taken', 'Stumpings', 'Matches_Bowled', 'Balls_Bowled',
       'Runs_Conceded', 'Wickets_Taken', 'Best_Bowling_Match',
       'Bowling_Average', 'Economy_Rate', 'Bowling_Strike_Rate',
       'Four_Wicket_Hauls', 'Five_Wicket_Hauls'])  # Remove non-numeric column
df_numeric = df_numeric.apply(pd.to_numeric, errors='coerce')  # Convert to numeric

# Drop columns with excessive zeros or NaN values (keep at least 10% non-zero values)
df_cleaned = df_numeric.loc[:, (df_numeric != 0).mean() > 0.1]

# Compute correlation matrix
corr_matrix = df_cleaned.corr()

# Filter out weak correlations (absolute value below 0.4)
filtered_corr = corr_matrix.where(abs(corr_matrix) > 0.4)

# Generate a heatmap with reduced entries
plt.figure(figsize=(12, 6))
sns.heatmap(filtered_corr, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")
plt.title("Filtered Correlation Heatmap (Only Strong Correlations)")
plt.show()
