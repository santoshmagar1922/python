#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:16:52 2019

@author: smq3434
"""
import numpy as np

import matplotlib.pyplot as plt

import theano as th


x= th.tensor.fvector('x')
y= th.tensor.fvector('y')

m = th.shared(0.5, 'm')
c = th.shared(0.8, 'c')

yhat = m*x + c

#cost function

cost = th.tensor.mean(th.tensor.sqr(y-yhat))/2   # cost is J

# gradient descent

LR = 0.05
gradm  = th.tensor.grad(cost, m) # dj/dm
gradc  = th.tensor.grad(cost, c) # dj/dc

mn = m - LR * gradm
cn = c - LR * gradc

#train funtion

train = th.function(inputs=[x,y], outputs=cost, updates=[(m,mn),(c,cn)])

area = [1.2,2.4,3.5,2.6,3.4,5.6,7.2,8.1,9.4,5.6]
price =[180,280,310,290,360,620,810,750,890,610]

area = np.array(area).astype('float32')
price = np.array(price).astype('float32')


for i in range(1000):
    cost_val = train(area, price)
    print(cost_val)


print(m.get_value())
print(c.get_value())












