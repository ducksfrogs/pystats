import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pymc3 as pm


data = np.array([51.06, 55.12, 53.73, 50.24, 52.05, 56.40, 48.45, 52.34, 55.65, 51.49, 51.86, 63.43, 53.00, 56.09, 51.93, 52.31, 52.33, 57.48, 57.44, 55.14, 53.93, 54.62, 56.09, 68.58, 51.36, 55.47, 50.73, 51.94, 54.95, 50.39, 52.91, 51.5, 52.68, 47.72, 49.73, 51.82, 54.99, 52.84, 53.19, 54.52, 51.46, 53.73, 51.61, 49.81, 52.42, 54.3, 53.84, 53.16
])


data


sns.kdeplot(data)


np.mean(stats.t(loc=0, scale=1, df=1).rvs(100))


np.mean(stats.t(loc=0, scale=1, df=100).rvs(100))


x_values = np.linspace(-10, 10, 200)


for df in [1,2,5,20]:
    distri = stats.t(df)
    x_pdf = distri.pdf(x_values)
    plt.plot(x_values, x_pdf, label=r'$\nu$ = {}'.format(df))
x_pdf = stats.norm.pdf(x_values)
plt.plot(x_values, x_pdf, label=r'$\nu = \infty$')
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
plt.legend(loc=0, fontsize=10)
plt.xlim(-7,7)


with pm.Model() as model_g:
    mu = pm.Uniform('mu', 40, 70)
    sigma = pm.HalfNormal('sigma', sd=10)
    y = pm.Normal('y', mu=mu, sigma=sigma, observed=data)
    trace_g = pm.sample(1100)

chain_g = trace_g[100:]
pm.traceplot(chain_g)



df = pm.summary(chain_g)


df


y_pred = pm.sample_posterior_predictive(chain_g, 100, model_g, size=len(data))
sns.kdeplot(data, c='b')
for i in y_pred['y']:
    sns.kdeplot(i, color='r', alpha=0.1)
plt.xlim(35, 75)
plt.title("Gaussian Model", fontsize=16)
plt.xlabel('$x$', fontsize=16)



y_pred


with pm.Model() as model_t:
    mu = pm.Uniform('mu', 40,75)
    sigma = pm.HalfNormal('sigma', sd=10)
    nu = pm.Exponential('nu', 1/30)
    y = pm.StudentT('y', mu=mu, sigma=sigma, nu=nu, observed=data)
    trace_t = pm.sample(1100)

chain_t = trace_t[100:]
pm.traceplot(chain_t)



df = pm.summary(chain_t)
print(df)



y_pred = pm.sample_pos(chain_t, 100, model_t, size=len(data))
sns.kdeplot(data, c='b')
for i in y_pred['y']:
    sns.kdeplot(i, c='r', alpha=0.1)




