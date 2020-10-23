import numpy as np
import pandas as pd
get_ipython().run_line_magic("matplotlib", " inline")


df = pd.read_csv("data/macrodata.csv", index_col=0, parse_dates=True)


df.head()


df['realgdp'].plot(figsize=(12,5))


from statsmodels.tsa.filters.hp_filter import hpfilter


gdp_cycle, gdp_trend = hpfilter(df['realgdp'], lamb=1600)


type(gdp_cycle)


gdp_cycle


gdp_trend


gdp_trend.plot()


df['trend'] = gdp_trend


df.head()


df[['trend','realgdp']]['2005-01-01':].plot(figsize=(12,5))


airline = pd.read_csv('data/airline_passengers.csv',index_col='Month', parse_dates=True)


airline.head()


airline.isna().count()


airline.describe()


airline.info()


airline = airline.dropna()


airline.plot()


from statsmodels.tsa.seasonal import seasonal_decompose


result = seasonal_decompose(airline['Thousands of Passengers'],
                            model='multiplicative')


result.trend


result.seasonal


from pylab import rcParams
rcParams['figure.figsize'] = 12,5

result.plot();


airline.index


airline.index = pd.to_datetime(airline.index)


airline.index


airline.head()


airline['6-month-SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()


airline['12-month-SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()


airline.plot()


airline['EWMA-12'] = airline['Thousands of Passengers'].ewm(span=12).mean()


airline[['Thousands of Passengers', 'EWMA-12']].plot()



