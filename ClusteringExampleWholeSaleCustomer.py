#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:53:08 2019

@author: smq3434
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# load the data

df = pd.read_csv(r"/Users/smq3434/desktop/Python and ML/data/Wholesale customers data.csv")

df2 = df[["Fresh", "Milk"]]

#appy clustering

from sklearn.cluster import KMeans
model = KMeans(n_clusters=3, random_state=5)


# train the model
model.fit(df2)

#cluster analysis
model.cluster_centers_

plt.hist(model.labels_)
plt.show()

sns.countplot(model.labels_)
plt.show()



# cost mean intertia_
# x axis is cluster vs y axis is cost
# we can calculate the value of K, 
# always better to calculate value of K first so that we have less cost.


cost = []
k = []

for i in range(1,10):
    model = KMeans(n_clusters=i)
    model.fit(df2)
    cost.append(model.inertia_)
    k.append(i)
    
   
plt.plot(k, cost)
plt.grid(True)
plt.show() 
    

############################

df3 = df[["Fresh", "Milk", "Frozen", "Grocery"]]

from sklearn.cluster import KMeans
model1 = KMeans(n_clusters=3, random_state=5)

# train the model
model1.fit(df3)

#cluster analysis
model1.cluster_centers_

plt.hist(model1.labels_)
plt.show()



############################
























