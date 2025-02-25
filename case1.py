import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv(r"D:\PythonProject\cricketcase\cricket_data.csv")
print(df.columns)
plt.hist(df['Runs_Scored'], bins=20)
plt.xlabel('Runs')
plt.ylabel('Frequency')
plt.title('Histogram of Runs Scored')
plt.show()