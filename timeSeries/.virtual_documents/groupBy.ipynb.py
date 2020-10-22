import pandas as pd


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


df = pd.DataFrame(data)


df


df.groupby('Company').mean()


df.groupby('Company').sum()


df.groupby('Company').describe()


df.groupby('Company').describe().transpose()


df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})


df['col2'].unique()


len(df['col2'].unique())


df['col2'].nunique()


df['col2'].value_counts()


new_df = df[(df['col1'] > 2) & (df['col2'] == 444)]


new_df


df


def times_to(nubmer):
    return nubmer *2


times_to(3)


df.apply(times_to)


df['New'] = df['col1'].apply(times_to)


df


del df['New']


df


df.columns


df.index


df.info()


df.describe()


df.sort_values(by='col2',ascending=False)



