#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:14:04 2019

@author: smq3434
"""

# Data Aggegation


import pandas as pd

df = pd.read_csv(r"/Users/smq3434/desktop/Python and ML/data/regiment.csv", index_col= "index")

'''
1. which is best performing regiment after traning ?
2. which company of which regiment is best performing after training ?
3. create column to show improvement in each soldier throught traning ?
4. which regiment has made maximum improvement throughout the traning ?
5. convert the names for every soldier to cap case
6. create regiment improvemment index for every soldier = improvemt nmade by the soldier compared to
    average improvement made by soldiers of that regiment.

'''

#question 1 :
# group by method 

df.groupby(by=["regiment"])["postTestScore"].mean()

df.groupby(by=["regiment"])["postTestScore"].mean().sort_values().tail(1).index[0]

#type(df.groupby(by=["regiment"])["postTestScore"].mean().sort_values().tail(1).index)


#question 2 :
# group by method for two feature

df.groupby(by=["regiment", "company"])["postTestScore"].mean()

#question 3 :
df["improvemt"] = df["postTestScore"] - df["preTestScore"]

#question 4 :
# group by method for improvemt

df.groupby(["regiment"])["improvemt"].mean()


#question 5 :   using lambda
df["name"] = df["name"].apply(lambda x:x.upper())

#question 6 :   using lambda
df["imp_index"] = df.groupby(["regiment"])["improvemt"].apply(lambda x:x-x.mean())






