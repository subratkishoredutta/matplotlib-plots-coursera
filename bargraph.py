# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 01:08:25 2021

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
new=data.loc['Iceland',range(1980,2014)]
new.plot(kind="bar")
plt.xlabel("year")
plt.ylabel('number of immigrants ')
plt.title('immigrants from Iceland from 1980 to 2013')
plt.savefig('barplot.png')
plt.show()