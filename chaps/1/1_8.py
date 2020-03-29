
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
plt.style.use('seaborn-darkgrid')

def naive_hpd(post):
    sns.kdeplot(post)
    HPD = np.percentile(post, [2.5, 97.5])
    plt.plot(HPD, [0, 0], label='HPD {:.2f} {:.2f}'.format(*HPD), linewidth=8, color='k')
    plt.legend(fontsize=16)
    plt.xlabel(r'$\theta$', fontsize=14)
    plt.gca().axes.get_yaxis().set_ticks([])

np.random.seed(1)
gausee_a = stats.norm.rvs(loc=4, scale=0.9, size=3000)
gausee_b = stats.norm.rvs(loc=-2, scale=1, size=2000)
mix_norm = np.concatenate((gausee_a, gausee_b))

from plot_post import plot_post
plot_post(mix_norm, rountto=2, alpha=0.05)
plt.xlabel(r"$\theta$", fontsize=14)
plt.savefig('img_09.png')
