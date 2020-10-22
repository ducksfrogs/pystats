import numpy as np
import pandas as pd



labels = ['a', 'b', 'c']


mylist = [10,20,30]


arr = np.array(mylist)


d = {'a':10, 'b':20, 'c':30}



arr


pd.Series(data=mylist, index=labels)



pd.Series(arr, index=labels)



pd.Series(data=[10,'a','b',4])



ser1 = pd.Series([1,2,3,4],index=['USA','Germany','USSR','Japan'])



ser1['USA']


ser2 = pd.Series([1,4,5,6],index=['USA','Germany','Italy','Japan'])



ser1 + ser2


#data Frames


from numpy.random import randn
np.random.seed(101)


rand_mat = randn(5,4)


rand_mat


df = pd.DataFrame(data=rand_mat, index='A B C D E'.split(), columns='W X Y Z'.split())


df


df['W']


mylist = ['W','Y']

df[mylist]


df[['X','Z']]


df.W


df['NEW'] = df['W'] + df['Y']


df


df.drop('NEW',axis=1)


df


df.drop('NEW', axis=1, inplace=True)


df


df.drop('A')


df.drop('C')


df.loc['A']


df.iloc[0]


df.iloc[2]


df.loc[['A','E']]


df.iloc[[0,3]]


df.loc[['A','B']]


df.loc[['A','B'],['Y','Z']]


df


df > 0


df_bool = df >0


df[df_bool]


df[df>0]


df['W'] >0


df[df['W'] > 0]


df[df['W'] >0]['Y'].loc['A']


df[df['W'] >0]['Y']



cond1 = df['W'] > 0
cond2 = df['Y'] > 1


df[(cond1) & (cond2)]


df.reset_index()


df


new_ind = 'CA NY WY OR CO'.split()


df['States'] = new_ind


df


df.set_index('States',inplace=True)


df.info()



df.dtypes


df.describe()


df['W'] > 0


df


ser_w = df['W'] > 0


ser_w.value_counts()


sum(ser_w)


len(ser_w)



