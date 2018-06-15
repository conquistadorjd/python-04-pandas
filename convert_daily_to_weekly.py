################################################################################################
#	name:	convert_daily_to_weekly.py
#	desc:	takes inout as daily prices and convert into weekly data
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
# Getting week number
df['Week_Number'] = df['Date'].dt.week
# Getting year. Weeknum is common across years to we need to create unique index by using year and weeknum
df['Year'] = df['Date'].dt.year

# Grouping based on required values
df2 = df.groupby(['Year','Week_Number']).agg({'Open Price':'first', 'High Price':'max', 'Low Price':'min', 'Close Price':'last','Total Traded Quantity':'sum'})
# df3 = df.groupby(['Year','Week_Number']).agg({'Open Price':'first', 'High Price':'max', 'Low Price':'min', 'Close Price':'last','Total Traded Quantity':'sum','Average Price':'avg'})
df2.to_csv('Weekly_OHLC.csv')
print('*** Program ended ***')