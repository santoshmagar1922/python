#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:45:07 2019

@author: smq3434
"""

#Numpy
'''
Two popular data types in numpy : 
    1. Ndarray->n dimentinal array
    2. Matrix -> 
    
'''
import numpy as np

x=[4,5,6]
y=[1,2,3]

x+y

#################

x=np.array([4,5,6])
y=np.array([1,2,3])

print(x+y)

print(x.shape)


x= np.array([[4,5,2], [3,2,7], [6,8,1]])

print(x)
print(x.shape)


print(x.min())

print(x.max())

print(x.mean())

###### row wise operation

x.max(axis=1)

###### column wise operation

x.min(axis=0)


####################################################

#funtions in numpy for mathematical computation

np.log10(100)
np.log(1000)

np.sqrt(625)

np.sin(np.deg2rad(90))   # degree to radient

np.cos(np.deg2rad(90))

####################################################

np.ones(5)

x= np.ones(5)

print(x.dtype)

np.ones((4,3))

np.zeros(6)

np.zeros((2,3))

np.zeros((2,3), dtype='int32')

np.arange(start=2,stop=20,step=1.5)    #np.arange.__doc__

np.arange(2,30,3)

np.linspace(start=5, stop=20, num=10)   #np.linspace.__doc__

#np.linspace.__doc__

##############################################

m = np.matrix([[4,5,2],[3,7,5],[6,1,8]])

print(m.dtype)
print(type(m))

# linear algebra

np.linalg.inv(m)   # inverse of matrix
np.linalg.det(m)   # determinant of matrix
np.linalg.eig(m)   # eigen values and vectors

##############################################
'''

Solve the below equation

3x-6y = 3

4x+y = 31

'''

a = [[3,-6], [4,1]]
b =[3,31]

np.linalg.solve(a,b)





































