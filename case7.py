import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv(r"D:\PythonProject\cricketcase\cricket_data.csv")

# Display dataset info and first few rows
print(df.info())
print(df.head())

# Identify and clean non-numeric columns
df.replace('No stats', None, inplace=True)  # Replace problematic strings with NaN
df.drop(columns=['Player_Name', 'Best_Bowling_Match', 'Bowling_Average',
                 'Economy_Rate', 'Bowling_Strike_Rate',
                 'Four_Wicket_Hauls', 'Five_Wicket_Hauls'], axis=1, inplace=True)

# Convert categorical column to dummy variables
if 'Half_Centuries' in df.columns:
    df = pd.concat([df, pd.get_dummies(df["Half_Centuries"], drop_first=True)], axis=1)
    df.drop(columns=["Half_Centuries"], inplace=True)

# Convert all remaining non-numeric columns to numeric if possible
df = df.apply(pd.to_numeric, errors='coerce')

# Generate and display correlation heatmap
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.show()
