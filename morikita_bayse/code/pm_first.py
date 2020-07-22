
mport numpy as np
import matplotlib.pyplot as plt


count_data = np.loadtxt("data/txtdata.csv")
n_count_data = len(count_data)

import pymc3 as pm
alpha = 1.0 / count_data.mean()

lambda_1 = pm.Exponential("lambda_1", alpha)
lambda_2 = pm.Exponential("lambda_2", alpha)

tau = pm.DiscreteUniform("tau", lower=0, upper=n_count_data)
