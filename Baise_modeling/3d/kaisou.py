import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pymc3 as pm

n_samples = [30, 30, 30]
G_samples = [18,18,18]

group_idx = np.repeat(np.arange(len(n_samples)), n_samples)
data=[]
for i in range(0, len(n_samples)):
    data.extend(np.repeat([1,0],[G_samples[i],n_samples[i] - G_samples[i]]))

with pm.Model() as model_h:
    alpha = pm.HalfCauchy('alpha', beta=10)
    beta = pm.HalfCauchy('beta', beta=10)
    theta = pm.Beta('theta', alpha, beta, shape=len(n_samples))
    y = pm.Bernoulli('y', p=theta[group_idx], observed=data)

    trace_h = pm.sample(2000)
chain_h = trace_h[200:]
pm.traceplot(chain_h)
plt.savefig('img314.png')
