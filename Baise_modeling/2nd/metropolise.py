import numpy as np
import matplotlib.pyplot as plt

from scipy import stats

def metropolise(func, steps=10000):
    """A very simple Metropolise implementation"""
    samples = np.zeros(steps)
    old_x = func.mean()
    old_prob = func.pdf(old_x)

    for i in range(steps):
        new_x = old_x + np.random.normal(0,0.5)
        new_prob = func.pdf(new_x)
        accptance = new_prob/old_prob
        if accptance >= np.random.random():
            samples[i] = new_x
            old_x = new_x
            old_prob = new_prob
        else:
            samples[i] = old_x

    return samples

func = stats.beta(0.4,2)
samples = metropolise(func=func)
x = np.linspace(0.01, 0.99, 100)
y = func.pdf(x)
plt.xlim(0,1)
plt.plot(x, y, 'r-', lw=3, label='True distoribution')
plt.hist(samples, bins=30, normed=True, label='Estimated distoribution')
plt.ylabel('$pdf(x)$', fontsize=14)
plt.legend()
plt.savefig('img023.png')
