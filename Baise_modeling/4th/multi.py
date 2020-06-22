import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
plt.style.use('seaborn-darkgrid')
np.set_printoptions(precision=2)
pd.set_option('display.precision', 2)

ans = sns.load_dataset('anscombe')
x_2 = ans[ans.dataset == 'II']['x'].values
y_2 = ans[ans.dataset == 'II']['y'].values
x_2 = x_2 - x_2.mean()
y_2 = y_2 - y_2.mean()

#
#plt.scatter(x_2, y_2)
#plt.xlabel('$x$', fontsize=16)
#plt.ylabel('$y$',fontsize=16, rotation=0)
#plt.savefig('img422.png')

with pm.Model() as model_poly:
    alpha = pm.Normal('alpha', mu=0, sd=10)
    beta1 = pm.Normal('beta1', mu=0, sd=1)
    beta2 = pm.Normal('beta2', mu=0, sd=1)
    epsilon = pm.HalfCauchy('epsilon', 5)

    mu = alpha + beta1 *x_2 + beta2 +x_2**2

    y_pred = pm.Normal('y_pred', mu=mu, sd=epsilon, observed=y_2)

    trace_poly = pm.sample(2000, cores=1)

pm.traceplot(trace_poly)
plt.savefig('img423.png')
