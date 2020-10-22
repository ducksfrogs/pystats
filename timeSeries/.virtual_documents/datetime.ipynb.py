from datetime import datetime


my_year = 2020
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15


my_date = datetime(my_year, my_month, my_day)


my_date_time = datetime(my_year,my_month, my_day, my_hour, my_minute, my_second)


my_date_time


my_date_time.day


my_date_time.hour


import numpy as np


np.array(['2020-03-15','2020-03-16','2020-03-17'], dtype='datetime64[Y]')


np.array(['2020-03-15','2020-03-16','2020-03-17'], dtype='datetime64[h]')





np.array(['2020-03-15','2020-03-16','2020-03-17'], dtype='datetime64')


np.arange('2018-06-01','2018-06-23', 7, dtype='datetime64[D]')


np.arange('1968','1976', dtype='datetime64[Y]')


import pandas as pd


pd.date_range('2020-01-01', periods=7, freq='D')


pd.date_range('Jan 01, 2018', periods=7, freq='D')


pd.to_datetime(['1/2/2018', 'Jan 3, 2018'])


pd.to_datetime(['1/2/2018', '1/3/2018'],format='get_ipython().run_line_magic("d/%m/%Y')", "")


pd.to_datetime(['1--2--2018', '1--3--2018'],format='get_ipython().run_line_magic("d--%m--%Y')", "")


data = np.random.randn(3,2)
cols = ['A','B']



idx = pd.date_range('2020-01-01',periods=3, freq='D')
df = pd.DataFrame(data, index=idx, columns=cols)


df


df.index


df.index.max()


df.index.argmax()



