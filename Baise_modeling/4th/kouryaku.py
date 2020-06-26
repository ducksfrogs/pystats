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
x_1 = np.random.normal(size=N)
x_2 = x_1 + np.random.normal(size=N, scale=1)
y = x_1 + np.random.normal(size=N)
X = np.vstack((x_1, x_2))
#alfa_real = 2.5
#beta_real = [0.9, 1.5]
#eps_real = np.random.normal(0, 0.5, N)
#
#X = np.array([np.random.normal(i, j, N) for i, j in zip([10,2],[1,1.5])])
#
#X_mean = X.mean(axis=1, keepdims=True)
#X_centerd = X - X_mean
#y = alfa_real + np.dot(beta_real, X) + eps_real

#def scatter_plot(x, y):
#    plt.figure(figsize=(10, 10))
#    for idx, x_i, in enumerate(x):
#        plt.subplot(2,2, idx+1)
#        plt.scatter(x_i, y)
#        plt.xlabel('$x_{}$'.format(idx+1), fontsize=16)
#        plt.ylabel('$y$', rotation=0, fontsize=16)
#    plt.subplot(2,2, idx+2)
#    plt.scatter(x[0], x[1])
#    plt.xlabel('$x_{}$'.format(idx), fontsize=16)
#    plt.ylabel('$x_{}$'.format(idx+1), rotation=0)
#
#
#scatter_plot(X, y)
#plt.savefig('img427.png')

with pm.Model() as model_red:
    alpha= pm.Normal('alpha', mu=0, sd=1)
    beta = pm.Normal('beta', mu=0, sd=10, shape=2)
    epsilon = pm.HalfCauchy('epsilon', 5)

    mu = alpha+ pm.math.dot(beta, X)

    y_pred = pm.Normal('y_pred', mu=mu, sd=epsilon, observed=y)

    trace_red = pm.sample(2000, cores=1)

pm.traceplot(trace_red)
plt.savefig('img429.png')
#
#x_p = np.linspace(-6, 6)
#y_p = trace_poly['alpha'].mean() + trace_poly['beta1'].mean() * x_p + trace_poly['beta2'].mean() *x_p**2
#plt.scatter(x_2,y_2)
#plt.xlabel('$x$', fontsize=16)
#plt.ylabel('$y$', fontsize=16, rotation=0)
#plt.plot(x_p, y_p, c='r')
#plt.savefig('img424.png')
#pm.summary(trace_mlr, varnames)
