################################################################################################
#	name:	create_column_from_other_columns.py
#	desc:	Create new columns in pandas DataFrame
#	date:	2018-06-16
#	Author:	conquistadorjd
################################################################################################
import pandas as pdea
import numpy as np
# import pandas_datareader as datareader
import matplotlib.pyplot as plt
import datetime
from matplotlib.finance import candlestick_ohlc
# from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

print('*** Program Started ***')

df = pd.read_csv('15-06-2016-TO-14-06-2018HDFCBANKALLN.csv')

# ensuring only equity series is considered
df = df.loc[df['Series'] == 'EQ']

# Converting date to pandas datetime format
df['Date'] = pd.to_datetime(df['Date'])
# print(df.dtypes)
# print(df.head())

#### Normail column creation
df['range'] = df['High Price'] - df['Low Price']
df['Average'] = (df['Close Price'] + df['Open Price'])/2

#### Conditional Value
df['GT1400'] = np.where( (df['Close Price']> 1400), 1, 0)
df['DailyTrend'] = np.where( (df['Close Price']>= df['Open Price']), 'Positive', 'Negative')
df['Calculated Column'] = np.where( (df['Close Price']>= df['Open Price']), df['Close Price']- df['Open Price'], (df['Close Price'] + df['Open Price'])/2)

df.to_csv('hdfc_with_calculated_columns.csv')
print('*** Program ended ***')