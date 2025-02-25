import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv(r"D:\PythonProject\cricketcase\cricket_data.csv")
plt.figure(figsize=(10, 6))
plt.scatter(df['Stumpings'], df['Matches_Batted'], alpha=0.5, color='cyan')
plt.xlabel('Stumpings')
plt.ylabel('Matches Played')
plt.title('Stumpings vs. Matches Played')
plt.show()