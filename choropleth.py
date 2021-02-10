# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:17:33 2021

@author: Asus
"""
import pandas as pd
import folium
import matplotlib.pyplot as plt

data=pd.read_excel('Canada.xlsx',sheet_name='Canada by Citizenship',skiprows=range(20),skipfooter=2)

data.drop(['AREA','DEV','REG','Type','Coverage'],axis=1,inplace=True)
data.rename(columns={'OdName':'Country'},inplace=True)
data.columns=list(map(str,data.columns))
data['total']=data.sum(axis=1)
print(data.head())

worldmap=folium.Map(zoom_start=2,tiles='Stamen Terrain')
world_geo = r'world_countries.json'
skip=np.ceil((data['total'].max()-data['total'].min())/5)
threshold=list(range(data['total'].min(),data['total'].max()+3,int(skip)))

worldmap.choropleth( geo_data=world_geo,
    data=data,
    columns=['Country', 'total'],
    key_on='feature.properties.name',
    threshold_scale=threshold,
    fill_color='YlOrRd', 
    fill_opacity=0.6, 
    line_opacity=0.5,
    legend_name='Immigration to Canada',
    reset=True)
                    
worldmap.save('choro.html')