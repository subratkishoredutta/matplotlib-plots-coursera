# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:51:42 2021

@author: Asus
"""
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("Canada.xlsx",skiprows=range(20),skipfooter=2,sheet_name='Canada by Citizenship')

data.head()##display by default 5 rows from the dataset

data=data.rename(columns={'OdName':'Country'})
data=data.set_index('Country')
data['total']=0
for i in range(1980,2014):
    data['total']+=data[i]


years=range(1980,2014)

data.loc['Haiti',years].plot(kind='line')
plt.xlabel('years')
plt.ylabel('population')
plt.title('immigration from Haiti')
plt.savefig('Haiti_Canada_immi.jpg')
plt.show()
