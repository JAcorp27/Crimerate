#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 23:03:53 2020

@author: junghan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics

data=pd.read_csv("popdata.csv")
print(data)

data1=pd.read_csv("MCI.csv")
data1_count=data1.groupby('reportedyear').size()
data1_count2=data1_count.to_frame().reset_index()
finaldata=data1_count2.rename(columns= {0: 'Crime Count','reportedyear':'Year'})
print(finaldata)

mergedata=pd.merge(data,finaldata)
print(mergedata)

x=mergedata['Population']
y=mergedata['Crime Count']

m, b = np.polyfit(x, y, 1)

print(m)
print(b)

plt.scatter(x,y)
plt.plot(x, m*x + b)
plt.xlabel("Population")
plt.ylabel("Crime Count")
plt.title('A Relationship between Population and Crime Count')
plt.show()

