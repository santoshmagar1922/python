#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:25:17 2019

@author: smq3434
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#load data 


df = pd.read_csv(r"/Users/smq3434/desktop/Python and ML/data/Bank_churn_modelling.csv")

#  axis=0 =>row
#  axis=1 =>column

df.drop(["RowNumber", "CustomerId", "Surname"], axis=1, inplace=True)


# Creditscore v/s exited


plt.figure(figsize=(12,5))
sns.distplot(df["CreditScore"] [df["Exited"]==0])
sns.distplot(df["CreditScore"] [df["Exited"]==1])
plt.legend(['0','1'])

plt.show()

# age v/s exited

plt.figure(figsize=(12,5))
sns.distplot(df["Age"] [df["Exited"]==0])
sns.distplot(df["Age"] [df["Exited"]==1])
plt.legend(['0','1'])

plt.show()

# Geography v/s Exited
plt.figure(figsize=(6,4))
sns.countplot(df["Geography"])
plt.show()


plt.figure(figsize=(6,4))
sns.countplot(df["Geography"] [df["Exited"]==1])
plt.show()

# Gender v/s Exited

plt.figure(figsize=(6,4))
sns.countplot(df["Gender"])
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(df["Gender"] [df["Exited"]==1])
plt.show()


# HasCrCard v/s Exited

plt.figure(figsize=(6,4))
sns.countplot(df["HasCrCard"])
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(df["HasCrCard"] [df["Exited"]==1])
plt.show()

# heatmap fr correlation analysis









