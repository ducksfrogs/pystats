import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
plt.style.use('seaborn-darkgrid')



def metropolis(func, steps=10000):
    

points = 15
h, n = 1, 4
grid, posterior = posterior_grid(points, h, n)
plt.plot(grid, posterior, 'o-', label='heads = {}\ntossess = {}'.format(h, n))
plt.xlabel(r'#\theta$', fontsize=14)
plt.legend(loc=0, fontsize=16)
plt.savefig('img21.png')
