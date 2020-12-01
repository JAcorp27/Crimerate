#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 17:46:56 2020

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

x=mergedata.drop(['Crime Count','Year'],axis='columns')
y=mergedata['Crime Count']

X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=10)

poly=PolynomialFeatures(degree=2)
xpoly=poly.fit_transform(X_train)

linreg=LinearRegression()
linreg.fit(X_train,y_train)

y_predict1=linreg.predict(X_test)
r_square1=metrics.r2_score(y_test,y_predict1)
print(r_square1)
prd1=linreg.predict([[3025027]])
print('2020 Crime Count assuming population will grow by 2%:',prd1)
prd2=linreg.predict([[3085528]])
print('2021 Crime Count assuming population will grow by 2%:',prd2)


plt.scatter(X_train,y_train, color='green')
plt.plot(X_train,linreg.predict(X_train),color='blue')
plt.title('A Predictive Model of Crime Count')
plt.ylabel('Crime Count')
plt.xlabel('Population')
plt.show()





