#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:38:37 2019

@author: smq3434
"""

# Data Cleaning


import pandas as pd

#Load the file 

df = pd.read_csv(r"/Users/smq3434/desktop/Python and ML/data/datawh_missing.csv")

'''
    Data Cleaning :
        1. Handling duplicate entries
        2. Handling missing entries

'''

# check for duplicates
df.duplicated().sum()

# dropping duplicates
df.drop_duplicates(inplace=True)   # commit in dataframe

# check for missing values
df.isnull().sum()

# load data with mentioned token representating missing values
df = pd.read_csv(r"/Users/smq3434/desktop/Python and ML/data/datawh_missing.csv",
                 na_values=[".","?"])
df.isnull().sum()

#s = "12345.55"
#print(s.isdecimal()) 
#print(s.isdigit()) 


df.skew()

# using mean to impute the missing entries in temp

df["Temperature"].fillna(df["Temperature"].mean(), inplace=True)


# replace missing values by median

df.fillna(df.median(), inplace=True)











































