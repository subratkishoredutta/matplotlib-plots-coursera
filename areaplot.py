# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:20:22 2021

@author: Asus
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel(r"Canada.xlsx",skiprows=range(20),skipfooter=2,sheet_name="Canada by Citizenship")

data.rename(columns={'OdName':'Country'},inplace=True)
data.set_index('Country',inplace=True)
data['total']=0
for i in range(1980,2014):
    data['total']+=data[i]
    
data.sort_values(['total'],ascending=False,axis=0,inplace=True)
new=data.head()
years=range(1980,2014)
new=new[years].transpose()
new.plot(kind="area")
plt.xlabel("years")
plt.ylabel("immigrant's country")
plt.savefig("areaplot.png")
plt.show()