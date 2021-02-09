# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:35:26 2021

@author: Asus
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_excel('Canada.xlsx',sheet_name="Canada by Citizenship",skiprows=range(20),skipfooter=2)
newdata=pd.DataFrame(columns=['year','total'])
for i in range(1980,2014):
    newdata=newdata.append({'year':i,'total':data[i].sum(axis=0)},ignore_index=True)    
newdata.set_index('year',inplace=True)
newdata.index=map(float,newdata.index)
newdata.reset_index(inplace=True)
newdata.columns=['year','total']

fig=plt.figure(figsize=(10,7))
ax=sns.regplot(x='year',y='total',data=newdata,color="cyan",marker='+',scatter_kws={'s': 250})
sns.set(font_scale=1.5)
sns.set_style('ticks')##whitegrid
ax.set(xlabel="year",ylabel="total immigrants")
ax.set_title("total number of immigrants from 1980-2013")
plt.savefig("regplot1.png")


'''
newdata=pd.DataFrame(data[range(1980,2014)].sum(axis=0))
newdata.index=map(float,newdata.index)
newdata.reset_index(inplace=True)
newdata.columns=['year','total']
'''