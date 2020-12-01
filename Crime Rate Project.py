#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 08:44:03 2020

@author: junghan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

pop_data=pd.read_csv("Thesixpop.csv")
thesixpop=pop_data.head (1) #you only need for all ages#
print(thesixpop)
print(thesixpop.columns)
new_pop=thesixpop.drop(['Ages'],axis = 'columns')
print(new_pop)
change_pop=new_pop.transpose()
print(change_pop)
change_pop.columns=['total population']#changing column name#
print(change_pop)
print(change_pop.columns)                    

#importing crime data and cleaning up#                    
crime_rate=pd.read_csv("MCI.csv")
crime_rate1=crime_rate.drop(['X', 'Y','Index_','event_unique_id','ucr_code','ucr_ext','Long','Lat'], 
                           axis = 'columns')
print(crime_rate1.columns)

crime_count=crime_rate1.groupby('reportedyear').size()
crime_counttotal=crime_count.to_frame().reset_index()
total_crime=crime_counttotal.rename(columns= {0: 'Crime Count'})
print(total_crime)
print(total_crime.columns)
total_crime1=total_crime.drop(['reportedyear'], 
                           axis = 'columns')

#checking relationship between total crime rate and population growth
plt.scatter(total_crime1,change_pop)
plt.xlabel("Population")
plt.ylabel("Crime Count")
plt.show()


#checking relationship between total crime rate and months
crime_month=crime_rate1.groupby('reportedmonth').size()
crime_montht=crime_month.to_frame().reset_index()
total_crimemonth=crime_montht.rename(columns= {0: 'Crime Count'})
print (total_crimemonth)
total_crimemonth.plot(x='reportedmonth',y='Crime Count')




