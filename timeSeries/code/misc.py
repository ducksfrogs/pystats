import pandas as pd
import numpy as np

labels = ['a','b','c']
mylist = [10,20,30]
arr = np.array(mylist)

d = {'a':10, 'b':20, 'c':30}

pd.Series(data=mylist, index=labels)

pd.Series(arr)

pd.Series(data=[10,'a','b',4])

ser1 = pd.Series([1,2,3,4],index=['USA','Germany','USSR','Japan'])
