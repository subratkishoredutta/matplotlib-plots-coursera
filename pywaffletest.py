# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:15:39 2021

@author: Asus
"""

import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle

data=pd.read_excel('Canada.xlsx',sheet_name="Canada by Citizenship",skiprows=range(20),skipfooter=2)
data.drop(['REG','DEV','Coverage','Type','AREA'],axis=1,inplace=True)
data.columns=list(map(str,data.columns))
data.rename(columns={'OdName':'Country','RegName':'Region','AreaName':'Continent'},inplace=True)
data['total']=data.sum(axis=1)
data.set_index('Country',inplace=True)

newdata=data.loc[['India','Pakistan','China']]
newdata.head()

fig = plt.figure(
    FigureClass=Waffle, 
    rows=25, 
    columns=50, 
    values=newdata['total'],
    figsize=(25, 50),
    labels=[name+"("+str(newdata.loc[name,'total'])+")" for name in newdata.index],
    colors=["#232066", "#983D3D", "#DCB732"],
    #icons='child', 
    legend={'loc': 'lower center', 'bbox_to_anchor': (.5, -0.06),'ncol':len(newdata.index)},

)
plt.savefig('test.png')
plt.show()