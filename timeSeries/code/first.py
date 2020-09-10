import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path_to_csv = 'https://www.mizuhobank.co.jp/rate/market/historical.html'

df_historical = pd.read_csv('{path_to_csv}/m_quote.csv')
df_historical
