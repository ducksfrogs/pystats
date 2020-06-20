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
