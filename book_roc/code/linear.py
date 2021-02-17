import cvxpy as cp

x1, x2 = cp.Variable(), cp.Variable()

obj = cp.Maximize(20*x1  60*x2)

cons = [5*x1 + 4*x2 <= 80,
        2*x1 + 4*x2 <= 40,
        2*x1 + 8*x2 <= 64,
        x1 >= 0,
        x2 >=0]

p = cp.Problem(obj, cons)
p.solve(verbose=True)

#Second plogram


import numpy as np
import cvxpy as cp

x = cp.Variable(2)

c = np.array([-20.0, -60.0, ]).T

G = np.array([
    [5.0, 4.0 ],
    [2.0, 4.0],
    [2.0, 8.0],
    [-1.0, 0],
    [0, -1.0]
])

h = [80.0, 40.0, 64.0, 0.0, 0.0]

obj = cp.Minimize(c.T * x)
cons = [G*x <= h]

p = cp.Problem(obj, cons)
p.solve(verbose=True)


#Solution for Third Problem

import cvxpy as cp
import numpy as np

r = 20
np.random.seed(1)

A = np.hstack((np.random.randn(r, 1), np.ones([r,1])))

c = np.array(A[:,0]).T

b = (10.0*np.random.randn() *c) + (0.5+np.random.randn(r,1))

b = b.T.tolist()

x = cp.Variable(2)
obj = cp.Minimize( sum(cp.square(A*x-b)))
