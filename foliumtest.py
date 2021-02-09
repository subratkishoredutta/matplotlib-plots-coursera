# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:18:48 2021

@author: Asus
"""
import folium
import matplotlib.pyplot as plt
##creating a basic world map

worldmap=folium.Map(zoom_start=104)
worldmap.save('basic.html')

##India location : 20.5937° N, 78.9629° E

indiamap=folium.Map(location=[20.5937,78.9629],zoom_start=5)
indiamap.save('India.html')

##Assam location : 26.2006° N, 92.9376° E
##tiles='stamen toner'==black and white layout
assammap=folium.Map(location=[26.2006,92.9376],zoom_start=5,tiles='Stamen Toner')
assammap.save('assam1.html')
##tiles='Stamen Terrain'
assammap=folium.Map(location=[26.2006,92.9376],zoom_start=5,tiles='Stamen Terrain')
assammap.save('assam2.html')


##adding markers

assam=folium.map.FeatureGroup()
assam.add_child(folium.features.CircleMarker(location=[26.2006,92.9376],color='blue',fill_color='blue',radius=10,weight=5))

indiamap.add_child(assam)

folium.Marker([26.2006,92.9376],popup="Assam").add_to(indiamap)

indiamap.save('marker.html')

#folium.features.CircleMarker()