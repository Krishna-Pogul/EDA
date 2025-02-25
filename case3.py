import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv(r"D:\PythonProject\cricketcase\cricket_data.csv")
plt.figure(figsize=(10, 6))
plt.scatter(df['Batting_Average'], df['Runs_Scored'], alpha=0.5, color='red')
plt.xlabel('Batting Average')
plt.ylabel('Runs Scored')
plt.title('Batting Average vs. Runs Scored')
plt.show()