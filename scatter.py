# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:19:47 2021

@author: Asus
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('Canada.xlsx',sheet_name="Canada by Citizenship",skiprows=range(20),skipfooter=2)
data.rename(columns={'OdName':'Country','AreaName':'Continent'},inplace=True)
data['total']=0
for i in range(1980,2014):
    data['total']+=data[i]
newdata=pd.DataFrame(columns=['year','total'])

for i in range(1980,2014):
    newdata=newdata.append({'year':i,'total':data[i].sum()},ignore_index=True)
standard = (newdata['total']-newdata['total'].min())/(newdata['total'].max()-newdata['total'].min())

plt.scatter(newdata['year'],newdata['total'],alpha=0.5,color='cyan',s=5)
plt.title('total number of immigration to Canada from 1980 to 2013')
plt.xlabel('year')
plt.ylabel('immigrants')
plt.savefig('scatternew.png')
plt.show()
