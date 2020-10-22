import numpy as np
import pandas as pd
get_ipython().run_line_magic("matplotlib", " inline")


df = pd.read_csv('data/df1.csv',index_col=0)


df.head()


df['A'].plot.hist()


df2 = pd.read_csv('data/df2.csv')


df2.head()


df['A'].plot.hist(edgecolor='k')





df['A'].plot.hist(edgecolor='k').autoscale(enable=True,axis='both',tight=True)


df['A'].plot.hist(bins=100, edgecolor='k').autoscale(enable=True,axis='both',tight=True)


df['A'].plot.hist(bins=20, edgecolor='k').autoscale(enable=True,axis='both',tight=True)


df['A'].plot.hist(grid=True)


df2.plot.bar(stacked=True)


df2.plot.barh(stacked=True)


df2.plot.line(y='a')


df2.plot.line(y=['a','b','c'],figsize=(12,5))



