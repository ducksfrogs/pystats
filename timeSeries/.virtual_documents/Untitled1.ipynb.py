import numpy as np
import pandas as pd
get_ipython().run_line_magic("matplotlib", " inline")


df = pd.read_csv("data/airline_passengers.csv", index_col='Month', parse_dates=True)


df.head()


df = df.dropna()


df.index


df.index.freq = 'MS'


df.head()


from statsmodels.tsa.holtwinters import SimpleExpSmoothing


span = 12
alpha = 2/(span+1)


df['EWMA12'] = df['Thousands of Passengers'].ewm(alpha=alpha, adjust=False).mean()


df.head()


model = SimpleExpSmoothing(df['Thousands of Passengers'])


fitted_model = model.fit(smoothing_level=alpha,optimized=False)


df['SES12'] = fitted_model.fittedvalues.shift(-1)


df.tail()



