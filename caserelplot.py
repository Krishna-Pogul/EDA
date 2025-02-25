import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv(r"D:\PythonProject\casestady\company.csv")
print(sns.relplot(data=df,x='average_montly_hours',y='satisfaction_level',col='Department',hue='salary',style='salary'))
plt.show()
