import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymc3 as pm
from scipy import stats
import pandas as pd

tips = sns.load_dataset('tips')
tips.tail()

y = tips['tip'].values
idx = pd.Categorical(tips['day']).codes


with pm.Model() as comparing_groups:
    means = pm.Normal('means', mu=0, sd=10, shape=len(set(idx)))
    sds = pm.HalfNormal('sds', sd=10, shape=len(set(idx)))

    y = pm.Normal('y', mu=means[idx], sd =sds[idx], observed=y)
    trace_cg =pm.sample(5000)
chain_cg = trace_cg[100::]
pm.traceplot(chain_cg)
plt.savefig('img311.png')
#sns.violinplot(x='day', y='tip',data=tips)
#plt.savefig('img310.png')
dist = stats.norm()

_, ax = plt.subplot(3,2, figsize=(16,12))

comparisons = [(i,j) for i in range(4) for j in range(i+1, 4)]

pos = [(k,l) for k in range(3) for l in (0,1)]

for (i,j), (k,l) in zip(comparisons, pos):
    means_diff = chain_cg['means'][:,i]-chain_cg['means'][:,j]

    d_cohen = (means_diff/ np.sqrt(( +chain_cg['sds'][:,j]**2
