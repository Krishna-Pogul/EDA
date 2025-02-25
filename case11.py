import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv(r"D:\PythonProject\cricketcase\cricket_data.csv")
sns.barplot('Batting_Strike_Rate')
plt.show()
