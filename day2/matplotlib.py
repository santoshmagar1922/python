#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:13:47 2019

@author: smq3434
"""

import numpy as np
import matplotlib.pyplot as plt

#lin plot
x=np.arange(0,20,1)
y=np.sin(x)
z=0.8*np.cos(1.5*x)

plt.plot(x,y)
plt.show

plt.plot(x,y,c='g')
plt.show

plt.figure(figsize=(12,5))
plt.plot(x,y,c='r', label="x v/s y")
plt.plot(x,z,c='g', label="x v/s z")

plt.title("graph of x, y and z")
plt.xlabel("value of x")
plt.ylabel("value of y and z")

plt.legend()
plt.show()

plt.figure(figsize=(12,5))
plt.scatter(x,y)
plt.show()

# pie chart

vals = [25,45,56,75,12]
labs= ["DEL", "BOM", "PUN", "BAN", "HYD"]
plt.pie(vals, labels=labs)
plt.show()

# bar chart
vals = [25,45,56,75,12]
labs= ["DEL", "BOM", "PUN", "BAN", "HYD"]
plt.bar(labs, vals)
plt.show()


# histogram

temp = [25,26,25,24,26,23,26,30,23,26,28]
plt.hist(temp)
plt.show()




