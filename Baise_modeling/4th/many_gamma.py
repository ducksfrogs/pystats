import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
plt.style.use('seaborn-darkgrid')
np.set_printoptions(precision=2)
pd.set_option('display.precision', 2)

rates = [1,2,5]
scales = [1, 2, 3]

#x = np.linspace(0,20, 100)
#f, ax = plt.subplots(len(rates), len(scales), sharex=True, sharey=True)
#for i in range(len(rates)):
#    for j in range(len(scales)):
#        rate = rates[i]
#        scale = scales[j]
#        rv = stats.gamma(a=rate, scale=scale)
#        ax[i, j].plot(x, rv.pdf(x))
#        ax[i, j].plot(0,0, label="$\\alpha$ = {:3.2f}\n$\\theta$ = {:3.2f}".format(rate,
#            scale), alpha=0)
#        ax[i, j].legend()
#ax[2,1].set_xlabel('$x$')
#ax[1,0].set_ylabel('$pdf(x)')
#plt.savefig('img401.png')
np.random.seed(314)
N = 100
alpha_real = 2.5
beta_real = 0.9
eps_real = np.random.normal(0, 0.5, size=N)

x = np.random.normal(10, 1, N)
y_real = alpha_real + beta_real * x
y = y_real + eps_real

#plt.figure(figsize=(10,5))
#plt.subplot(1,2,1)
#plt.plot(x, y, 'b.')
#plt.xlabel('$x$', fontsize=16)
#plt.ylabel('$y$', fontsize=16, rotation=0)
#plt.plot(x, y_real, 'k')
#plt.subplot(1,2,2)
#sns.kdeplot(y)
#plt.xlabel('$x$', fontsize=10)
#plt.savefig('img403.png')

with pm.Model() as model:
    alpha = pm.Normal('alpha', mu=0, sd=10)
    beta = pm.Normal('beta', mu=0, sd=1)
    epsilon = pm.HalfCauchy('epsilon', 5)

    mu = pm.Deterministic('mu', alpha + beta * x)
    y_pred = pm.Normal('y_pred', mu=mu, sd=epsilon, observed=y)

    start = pm.find_MAP()
    step = pm.Metropolis()
    trace = pm.sample(11000, step, start, cores=1)

trace_n = trace[1000:]
pm.traceplot(trace_n)
plt.savefig('img404-2.png')
