################################################################################################
#	name:	convert_daily_to_monthly.py
#	desc:	takes inout as daily prices and convert into monthly data
#	date:	2018-06-15
#	Author:	conquistadorjd
################################################################################################
import pandas as pd
import numpy as np

print('*** Program Started ***')

df = pd.read_csv('15-06-2016-TO-14-06-2018HDFCBANKALLN.csv')

# ensuring only equity series is considered
df = df.loc[df['Series'] == 'EQ']

# Converting date to pandas datetime format
df['Date'] = pd.to_datetime(df['Date'])
# Getting month number
df['Month_Number'] = df['Date'].dt.month
# Getting year. month is common across years (as if you dont know :) )to we need to create unique index by using year and month
df['Year'] = df['Date'].dt.year

# Grouping based on required values
df2 = df.groupby(['Year','Month_Number']).agg({'Open Price':'first', 'High Price':'max', 'Low Price':'min', 'Close Price':'last','Total Traded Quantity':'sum'})
# df3 = df.groupby(['Year','Week_Number']).agg({'Open Price':'first', 'High Price':'max', 'Low Price':'min', 'Close Price':'last','Total Traded Quantity':'sum','Average Price':'avg'})
df2.to_csv('Monthly_OHLC.csv')
print('*** Program ended ***')