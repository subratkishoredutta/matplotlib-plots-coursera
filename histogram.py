# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:52:21 2021

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

counts,bin_edge=np.histogram(data[2013])

data[2013].plot(kind="hist",xticks=bin_edge)
plt.title("histogram of the population coming from various countries")
plt.xlabel("no of immigrants")
plt.ylabel("no of countries")
plt.savefig("histogram")
plt.show()

