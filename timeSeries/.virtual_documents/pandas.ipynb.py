import pandas as pd


get_ipython().getoutput("ls")



df1 = pd.read_csv('data/df1.csv',index_col=0)


df1


df2 = pd.read_csv('data/df2.csv')


df2


df1['A'].plot.hist()


df1['B'].plot.hist(edgecolor='k').autoscale(enable=True, axis='both')



