import pandas as pd


df = pd.read_csv('data/starbucks.csv',index_col='Date', parse_dates=True)


df.head()


df.info()


df.index


df.resample(rule='A').mean()


df.resample(rule='A').sum()


def first_day(entry):
    if len(entry) get_ipython().getoutput("= 0:")
        return entry[0]


df.resample(rule='A').apply(first_day)


df.head()


df['Close'].resample('A').mean().plot.bar()


df['Close'].resample(rule='A').mean()


df['Close'].resample('A').mean().plot.bar(title="Yearly Mean closing Price for Starbucks")


title = "Monthly Max closing Price for Starbucks"
df['Close'].resample('M').max().plot.bar(figsize=(16,6),title=title,color='red')



