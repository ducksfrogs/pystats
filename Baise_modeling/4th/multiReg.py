import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
plt.style.use('seaborn-darkgrid')
np.set_printoptions(precision=2)
pd.set_option('display.precision', 2)


np.random.seed(314)
N = 100
alfa_real = 2.5
beta_real = [0.9, 1.5]
eps_real = np.random.normal(0, 0.5, N)

X = np.array([np.random.normal(i, j, N) for i, j in zip([10,2],[1,1.5])])

X_mean = X.mean(axis=1, keepdims=True)
X_centerd = X - X_mean
y = alfa_real + np.dot(beta_real, X) + eps_real

def scatter_plot(x, y):
    plt.figure(figsize=(10, 10))
    for idx, x_i, in enumerate(x):
        plt.subplot(2,2, idx+1)
        plt.scatter(x_i, y)
        plt.xlabel('$x_{}$'.format(idx+1), fontsize=16)
        plt.ylabel('$y$', rotation=0, fontsize=16)
    plt.subplot(2,2, idx+2)
    plt.scatter(x[0], x[1])
    plt.xlabel('$x_{}$'.format(idx), fontsize=16)
    plt.ylabel('$x_{}$'.format(idx+1), rotation=0)


scatter_plot(X_centerd, y)
plt.savefig('img425.png')

#plt.scatter(x_2, y_2)
#plt.xlabel('$x$', fontsize=16)
#plt.ylabel('$y$',fontsize=16, rotation=0)
#plt.savefig('img422.png')

#with pm.Model() as model_poly:
#    alpha = pm.Normal('alpha', mu=0, sd=10)
#    beta1 = pm.Normal('beta1', mu=0, sd=1)
#    beta2 = pm.Normal('beta2', mu=0, sd=1)
#    epsilon = pm.HalfCauchy('epsilon', 5)
#
#    mu = alpha + beta1 *x_2 + beta2 *x_2**2
#
#    y_pred = pm.Normal('y_pred', mu=mu, sd=epsilon, observed=y_2)
#
#    trace_poly = pm.sample(2000, cores=1)
#
##pm.traceplot(trace_poly)
##plt.savefig('img423.png')
#
#x_p = np.linspace(-6, 6)
#y_p = trace_poly['alpha'].mean() + trace_poly['beta1'].mean() * x_p + trace_poly['beta2'].mean() *x_p**2
#plt.scatter(x_2,y_2)
#plt.xlabel('$x$', fontsize=16)
#plt.ylabel('$y$', fontsize=16, rotation=0)
#plt.plot(x_p, y_p, c='r')
#plt.savefig('img424.png')
