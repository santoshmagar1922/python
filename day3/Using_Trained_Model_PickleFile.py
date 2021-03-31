#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:41:22 2019

@author: smq3434
"""

from sklearn.externals import joblib
model = joblib.load("ccpp_model.pkl")


model.predict([[13.97,	39.16,	1016.05,	84.6]])