#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:45:18 2019

@author: smq3434
"""

import numpy as np

from sklearn.linear_model import LinearRegression


area = [1.2,2.4,3.5,2.6,3.4,5.6,7.2,8.1,9.4,5.6]
price =[180,280,310,290,360,620,810,750,890,610]


area = np.array(area).reshape(10,1)   # inputs are needed in 2D
price = np.array(price)             # labels are not required        

# creating model instance
#normal equation approach
model = LinearRegression()

# train the model

model.fit(area, price)

print("value of m : ", model.coef_)
print("value of c : ", model.intercept_)



# sklearn from ML
#Gradient descent approach

from sklearn.linear_model import SGDRegressor

model2 = SGDRegressor(verbose=True)

model2.fit(area, price)
