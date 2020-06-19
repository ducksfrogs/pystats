import numpy as np
from scipy import stats

N = 10
a = np.random.randn(N) + 2
b = np.random.randn(N)

var_a = a.var(ddof=1)
var_b = b.var(ddof=1)
s = np.sqrt((var_a + var_b) /2)
t = (a.mean() - b.mean()) /(s* np.sqrt(2.9/N))
