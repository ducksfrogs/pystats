import pymc3 as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import theano.tensor as tt
plt.style.use('seaborn-darkgrid')
np.set_printoptions(precision=2)
pd.set_option('display.precision', 2)

z = np.linspace(-10, 10, 100)
logistic = 1/(1 + np.exp(-z))
plt.plot(z, logistic)
plt.xlabel('$z$', fontsize=16)
plt.ylabel('$logistic(z)$', fontsize=16)
plt.savefig('img501.png')

iris = sns.load_dataset('iris')
iris.head()

sns.stripplot(x='species', y= 'sepal_length', data=iris, jitter=True)
