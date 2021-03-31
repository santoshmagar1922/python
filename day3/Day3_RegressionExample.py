#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:33:23 2019

@author: smq3434
"""

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# load the data
# https://archive.ics.uci.edu/ml/machine-learning-databases/00294/   file taken from this link

df = pd.read_excel(r"/Users/smq3434/desktop/Python and ML/data/CCPP/Folds5x2_pp.xlsx")

# check for data info
df.info()

# check duplicates
df.duplicated().sum()

# 41 duplciates present but not dropping because duplicate data naturally can occur in this problem
# check for missing values

df.isnull().sum()

#correlation anaylsis
cor = df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(cor, annot=True, cmap="coolwarm")
plt.show()

'''

Note:  Z test is used to compare population mean vs sample mean where popu mean and pop std is known.
 Example of dairy milks

One sample test :
    
Independent test :
    
chi square test - this is to compare distributoin of the categorical attribute among the 
multiple groups

Null hypothesis = means of multiple groups are same

Alternate Hypothesis = means are different

if pvaue < 0.05 -> Reject null hypothesis = > if feature has different distribution/behavior in groups
so its important 

if pvaue > 0.05 -> Accept null hypothesis = > if feature has same distribution/ behavior in groups
so its NOT imp 

'''

# Below is example of F test -> ANOVA  analysis of variance
# separating x and y => x is features, y is label which is power produced (PE)
# F test works on sample sets only. like high temp is one set and low temp is another set and then
#it see its impact on PE

x= df.drop(["PE"], axis=1)
y = df["PE"]

from sklearn.feature_selection import f_regression
fvalue, pvalue = f_regression(x,y)
print(x.columns)

print(pvalue)
# if pvalue is lesser than 0.05 feature is important. Because of 95%
# p is probability. how close they are with each other.  0 means they are not closer means 
# features are important.
# f is statistical value 

####################################################

# spliting data into train and test sets

from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts = train_test_split(x,y,test_size=0.2)


print(x.shape)
print(xtr.shape)
print(xts.shape)

#building a linear regression predictor

from sklearn.linear_model import LinearRegression
model = LinearRegression()

# train the model

model.fit(xtr,ytr)

#making a prediction

ip = np.array([19.07,49.69,1007.22,76.79]).reshape(1,4)

model.predict(ip)

# need to calculate r sqaure which is error.
# PERFORMANCE ANALYSIS

ypred = model.predict(xts)

from sklearn.metrics import r2_score

# for Regression we use accuracy_score

r2_score(yts, ypred)

################################
# Exporting the model for deployment

from sklearn.externals import joblib

joblib.dump(model, "ccpp_model.pkl")

































