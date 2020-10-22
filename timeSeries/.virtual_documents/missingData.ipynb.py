import numpy as np
import pandas as pd


df = pd.DataFrame({'A':[1,2,np.nan],'B':[5, np.nan,np.nan],'C':[1,2,3]})


df


df.dropna()


df.dropna(axis=1)


df


df.dropna(thresh=2)


df.dropna(thresh=3)


df.fillna(value=0)


df.fillna(df.mean())


df['A'].fillna(value=df['A'].mean())



