import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv(r"D:\PythonProject\cricketcase\cricket_data.csv")
plt.figure(figsize=(10, 6))
plt.scatter(df['Bowling_Average'], df['Wickets_Taken'], alpha=0.5, color='blue')
plt.xlabel('Bowling Average')
plt.ylabel('Wickets Taken')
plt.title('Bowling Average vs. Wickets Taken')
plt.show()
