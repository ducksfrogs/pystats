import matplotlib.pyplot as pljt
import numpy as np
import seaborn as sns

n_samples = [30, 30, 30]
G_samples = [18,18,18]

group_idx = np.repeat(np.arange(len(n_samples)), n_samples)
data=[]
for i in range(0, len(n_samples)):
    data.extend(np.repeat([1,0],[G_samples[i],n_samples[i] - G_samples[i]]))


data



