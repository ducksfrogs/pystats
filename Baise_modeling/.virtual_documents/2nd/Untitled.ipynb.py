import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


N = 1000000
x,y = np.random.uniform(-1, 1, size=(2,N))


x


y


plt.scatter(x, y)


inside = (x**2 + y **2) <= 1


inside


outside = np.invert(inside)


plt.plot(x[inside],y[inside],'b.')
plt.plot(x[outside],y[outside], 'r.')


pi = inside.sum()*4/N


pi


inside.sum()


outside.sum()


err = abs((pi - np.pi)/pi)*100


err

















N = 100
x, y = np.random.uniform(-1, 1, size=(2,N))


x


plt.hist(x)


x, y = np.random.uniform(-1,1,size=(2,1000))


x


y


plt.hist(x)


plt.hist(y)



