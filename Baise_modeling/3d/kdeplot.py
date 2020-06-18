import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.style.use('seaborn-darkgrid')

data = pd.read_csv('data.csv')
sns.kdeplot(data)
plt.savefig('img301.png')
