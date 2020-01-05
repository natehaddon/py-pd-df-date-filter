# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 13:11:45 2020

@author: nate_

"""

#Use this to get the latest records from the web properties data.

from pandas import DataFrame
import pandas as pd
import numpy as np

def find_recent_date(df, date_col):
    
    recent_date = df[date_col].max()
    return recent_date

def append_time(timestamp):
    
    pass

def filter_date(df, start:str, end:str, date_col):
    
    mask = (df[date_col] > start) & (df[date_col] <= end)
    df = df.loc[mask]
    return df

# Create the test data
np.random.seed(0)
# create an array of 5 dates starting at '2015-02-24', one per minute
rng = pd.date_range('2015-02-24', periods=48, freq='H')
df = pd.DataFrame({ 'Date': rng, 'Val': np.random.randn(len(rng)) }) 

print(find_recent_date(df, 'Date'))
print(type(find_recent_date(df, 'Date')))
# Returns just the date, we can use this to query the latest records
print(str(find_recent_date(df, 'Date').date()))
# Append 00:00:00 and 23:59:59 to start and end timestamps
start = str(find_recent_date(df, 'Date').date()) + ' 00:00:00'
end = str(find_recent_date(df, 'Date').date()) + ' 23:59:59'

print(start, end)
#check_date_col(df, 'Date')
df = filter_date(df, start, end, 'Date')
#print(df['Date'].dtypes)