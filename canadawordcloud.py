# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 04:38:48 2021

@author: Asus
"""

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

data=pd.read_excel('Canada.xlsx',sheet_name="Canada by Citizenship",skiprows=range(20),skipfooter=2)
data.drop(['AREA','Type','Coverage','REG','DEV'],axis=1,inplace=True)
data.rename(columns={'OdName':'Country'},inplace=True)
data.columns=list(map(str,data.columns))
data.set_index('Country',inplace=True)
data['total']=data.sum(axis=1)
total=data['total'].sum()

max_words=70
mainstr=''
for name in data.index.values:
    if len(name.split(" "))==1:
        rep=int(data.loc[name,'total']/float(total)*max_words)
        mainstr=mainstr+((name+" ")*rep)    
    
WC=WordCloud(
        background_color='white',
        max_words=20,
        )

WC.generate(mainstr)
fig=plt.figure()
fig.set_figwidth(10)
fig.set_figheight(5)
plt.imshow(WC, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloudcanada.png')
plt.show()




