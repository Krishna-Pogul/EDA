import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv(r"D:\PythonProject\cricketcase\cricket_data.csv")
player_appearances = df.groupby('Player_Name')['Year'].count().sort_values(ascending=False)
top_ten_players = player_appearances.head(10)
plt.figure(figsize=(12, 6))
plt.bar(top_ten_players.index, top_ten_players.values, color='skyblue')
plt.xlabel('Player Name')
plt.ylabel('Number of Appearances')
plt.title('Top Ten Players with Most Appearances')
plt.xticks(rotation=45, ha='right')
plt.show()