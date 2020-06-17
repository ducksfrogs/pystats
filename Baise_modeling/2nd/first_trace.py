import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pymc3 as pm

np.random.seed(123)
n_experiments = 4
theta_real = 0.35
data = stats.bernoulli.rvs(p=theta_real,size=n_experiments)
print(data)

with pm.Model() as our_first_model:
    theta = pm.Beta('theta', alpha=1, beta=1)
    y = pm.Bernoulli('y', p=theta, observed=data)

    start = pm.find_MAP()
    step = pm.Metropolis()
    trace = pm.sample(1000, step=step, start=start)

burnin =100
chain = trace[burnin:]
pm.traceplot(chain, lines={'theta': theta_real})
plt.savefig('img204.png')
