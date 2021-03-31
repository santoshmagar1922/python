#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:06:12 2019

@author: smq3434
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# load the bank_churn data

df = pd.read_csv(r"/Users/smq3434/desktop/Python and ML/data/Bank_churn_modelling.csv")

# cleaning of data
df.info()

#check unique values in object columns to see if any token is present or not like . or @ or # or ?
df["Geography"].unique() 
df["Gender"].unique()

# check for duplicates
df.duplicated().sum()

#check for missing values
df.isnull().sum()

# drop unnecessary columns
df.drop(["RowNumber", "CustomerId", "Surname"], axis=1, inplace=True)

#check shape of data
print(df.shape)

##########################
#correlation analysis

cor = df.corr()
plt.figure(figsize=(12,10))

sns.heatmap(cor, annot=True, cmap="coolwarm")

plt.show()

# f test ANOVA => f test can be only applicable on numeric data

xcont = df[["CreditScore", "Age", "Tenure", "Balance", "EstimatedSalary"]]
y = df[["Exited"]]



from sklearn.feature_selection import f_classif
fvalue, pvalue = f_classif(xcont,y)

print(xcont.columns)
print(pvalue)

# Chi square => THis is applied on categoricla features

xcat = df[["HasCrCard", "IsActiveMember"]]
y=df["Exited"]


from sklearn.feature_selection import chi2
cvalue, pvalue = chi2(xcat,y)

print(xcat.columns)
print(pvalue)


####################################################
# separate feature and labels

xd = df.drop(["Exited"], axis=1)
y = df["Exited"]

# dropping unnecessary features
#xd.drop(["Tenure", "EstimatedSalary", "HasCrCard"], axis=1, inplace=True)

# encoding geography and gender using labelencoder

from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
xd["Geography"] = le1.fit_transform(xd["Geography"])

le2 = LabelEncoder()
xd["Gender"] = le2.fit_transform(xd["Gender"])

# onehot encoding  geography column

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(categorical_features=[1])   # groGraphy is first column so its 1
x = ohe.fit_transform(xd).toarray()

####################################################
#scale the deatures using standadization

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x = sc.fit_transform(x)

# split data into train and test sets

from sklearn.model_selection import train_test_split

xtr,xts,ytr,yts = train_test_split(x,y,test_size = 0.2)

# logistic regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# train the model
model.fit(xtr,ytr)

#making a prediction for single customer
'''
creditscore = 452, from France, Male with Age 75, tenure 3 yrs, balance of 45645,
number of products 3, hasCC is yes, isActive is No, and salary is 45621
'''
ip = np.array([1,0,0,452,1,75,3,45645,3,1,0,45621]).reshape(1,12)
model.predict(ip)

# Performance analysis

ypread = model.predict(xts)
from sklearn import metrics

# for classification we use accuracy_score
metrics.accuracy_score(yts, ypread)

# RECALL
metrics.recall_score(yts, ypread)

# confusion matrix
metrics.confusion_matrix(yts, ypread)

# Precesion
metrics.precision_score(yts, ypread)

# F1 score
metrics.f1_score(yts, ypread)

# AUC for 
metrics.roc_auc_score(yts, ypread)

#metrics.roc_curve(yts, ypread)



####################################################
####################################################
#K Nearest Neighbour

from sklearn.neighbors import KNeighborsClassifier

model2= KNeighborsClassifier(n_neighbors=3)

model2.fit(xtr, ytr)

ypread2=model2.predict(xts)

metrics.accuracy_score(yts, ypread2)

#recall

metrics.recall_score(yts, ypread2)
metrics.roc_auc_score(yts, ypread2)



##############################################

from sklearn.neural_network import MLPClassifier
model2 = MLPClassifier(learning_rate_init=0.001,max_iter=5000,
                       hidden_layer_sizes=(200,100),verbose=True)
model2.fit(xtr,ytr)
ypred2=model2.predict(xts)

metrics.recall_score(yts,ypred2)

#recall in train data
metrics.recall_score(ytr,model2.predict(xtr))

#metrics.accuracy_score(yts,ypred2)

##############################################

from sklearn.neural_network import MLPClassifier
model3 = MLPClassifier(learning_rate_init=0.001,max_iter=5000,
                        hidden_layer_sizes=(20,10),verbose=True)

model3.fit(xtr,ytr)
ypred3=model3.predict(xts)

metrics.recall_score(yts,ypred3)

#metrics.accuracy_score(yts,ypred3)

##############################################

from sklearn.neural_network import MLPClassifier
model4 = MLPClassifier(learning_rate_init=0.001,max_iter=5000,
                        hidden_layer_sizes=(100),verbose=True)

model4.fit(xtr,ytr)
ypred4=model4.predict(xts)


#recall in test data
metrics.recall_score(yts,ypred4)

#recall in train data
metrics.recall_score(ytr,model4.predict(xtr))

#metrics.accuracy_score(yts,ypred4)






















