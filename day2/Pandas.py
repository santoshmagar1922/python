#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:25:30 2019

@author: smq3434
"""

'''

Pandas used for : 
    Data import/ export,
    data manipulation - selction, filtering
    data cleaning
    basic statistical analysis
    data aggregation
    data visualization
    


1. Pandas Series- 1D  means 1row or 1column
2. Pandas Dataframe - 2D
3. Pandas panel - 3D

'''

########################################################
# Data import export

import pandas as pd

df = pd.read_csv(r"/Users/smq3434/desktop/Python and ML/data/datawh.csv", index_col= "Dates")

#without header
df = pd.read_csv(r"/Users/smq3434/desktop/Python and ML/data/datanh.csv", header=None)

df.columns= ["Temp", "humidity", "pressure", "air_quality"]

# load data from html sources

url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/"
dfs= pd.read_html(url)

type(dfs)

len(dfs)

df1 = dfs[0]
df2 = dfs[1]

# Export

df1.to_excel("bitcoin.xlsx")


df2.to_csv("bitcoin1.csv")


##############################################################
# Selection and Flitering of data

df = pd.read_csv("/Users/smq3434/desktop/Python and ML/data/datawh.csv", index_col= "Dates")
type(df)

print(df.columns) # see columns

print(df.head()) # see top five rows

print(df.tail()) # see bottom five rows

print(df.head(7)) # see top 7 rows

print(df.info())  # will provide overall info about data, like columns, null or non-null data etc

#selction

df.Temperature

df["Temperature"]

# access multiple columns
df[["Temperature", "Humidity"]]

type(df["Temperature"])

type(df[["Temperature", "Humidity"]])


# rowwise selection

df["05-05-2018":"09-05-2018"]


df["05-05-2018":"09-05-2018"][["Temperature","Humidity"]]


# rowwise selection using index

df.iloc[2:8, 0:4]

# Filtering

df[df["Temperature"]>2000]
df[df.Temperature>2000]

df["Temperature"][df["Temperature"]>2000]

df[df["Temperature"]>2000] ["Temperature"]

#multiple columns condition

df[df["Temperature"]>2000] [df["Humidity"]>250]


#AND
df[ (df.Temperature>2000) &  (df.Humidity>250 ) ]
df[ (df["Temperature"]>2000) &  (df["Humidity"]>250 ) ]

#OR
df[ (df.Temperature>2000) |  (df.Humidity>250 ) ]
df[ (df["Temperature"]>2000) |  (df["Humidity"]>250 ) ]


############################################

# Basic statistical analysis


# statistical overview of the data
df.describe()

# individual statistical analysis

df.mean()
df.min()

df["Temperature"].min()
df["Temperature"].max()
df["Temperature"].count()
df["Temperature"].mean()
df["Temperature"].median()
df["Temperature"].mode()
df["Temperature"].var()
df["Temperature"].std()

df["Temperature"].kurt()

df["Temperature"].skew()
df.skew()

# correlation
df.corr()

df[["Temperature","Humidity"]].corr()










