# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:57:14 2021

@author: Asus
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel('Canada.xlsx',sheet_name="Canada by Citizenship",skiprows=range(20),skipfooter=2)
data.rename(columns={'OdName':'Country','AreaName':'Continent'},inplace=True)
data['total']=0
for i in range(1980,2014):
    data['total']+=data[i]

data.set_index('Country',inplace=True)

data_india=data.loc[['India'],range(1980,2014)].transpose()## transpose to bring to a format that is representable
data_india.plot(kind="box")
plt.title("immigration from India to Canada from 1980 to 2013")
plt.ylabel('number of immigrants')
plt.savefig('box.png')
plt.show()

