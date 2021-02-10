# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 01:35:04 2021

@author: Asus
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("Canada.xlsx",skiprows=range(20),skipfooter=2,sheet_name='Canada by Citizenship')

data.rename(columns={'OdName':'Country'},inplace=True)
data.set_index('Country',inplace=True)

data['total']=0
for i in range(1980,2014):
    data['total']+=data[i]
    
print(data.head())
data.rename(columns={'AreaName':'Continent'},inplace=True)

color=['cyan','gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen']

explode_list=[0.2,0,0,0.1,0.3,0.4]

newdata=data.groupby('Continent',axis=0).sum()
#newdata['total'].plot(kind='pie')
newdata['total'].plot(kind="pie",figsize=(15,10),labels=None,autopct='%1.1f%%',pctdistance=1.09,  explode=explode_list, startangle=90, shadow=True,colors=color)

plt.legend(labels=newdata.index,loc="upper right")
plt.title('percentage of immigrants from 1980 to 2013 from various continents')
plt.axis('equal') 
plt.savefig('piechart.png')
plt.show()