# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:19:48 2021

@author: Asus
"""
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_excel("Canada.xlsx",skiprows=range(20),skipfooter=2,sheet_name="Canada by Citizenship")
#cleaning the data

data.drop(['AREA','REG','DEV','Coverage','Type'],axis=1,inplace=True)
data.rename(columns={'OdName':'Country','AreaName':'Continent'},inplace=True)
data.set_index('Country',inplace=True)
data.columns=list(map(str,data.columns))
data['total']=data.sum(axis=1)
##India,China,Pakistan
newdata=data.loc[['India','Pakistan','China']]

total=newdata['total'].sum(axis=0)

proportions=[float(value)/float(total) for value in newdata['total']]

width = 50##width of the waffle plot
height = 20##height of the waffle plot

N = width*height##total number of tile

M=[round(proportion*N)for proportion in proportions]

canvas=np.zeros((height,width),dtype=np.uint8)

CI=0
Ccount=0

for i in range(width):
    for j in range(height):
        Ccount+=1
        if Ccount>sum(M[0:CI]):
            CI+=1
        canvas[j][i]=CI
        
fig=plt.figure()
colormap = plt.cm.coolwarm#gist_ncar
plt.matshow(canvas, cmap=colormap)

#plt.colorbar()

ax = plt.gca()
ax.set_xticks(np.arange(-0.5,width,1),minor=True)
ax.set_yticks(np.arange(-0.6,height,1),minor=True)
ax.grid(which="minor",color='w',linestyle='-',linewidth=1)
plt.xticks([])
plt.yticks([])

labels=[]

cumuvals=np.cumsum(newdata['total'])

for i,name in enumerate(newdata.index):
    label=name+"("+str(newdata.loc[name,'total'])+")"
    color=colormap(float(cumuvals[i])/total)
    labels.append(mpatches.Patch(color=color, label=label))
    
plt.legend(handles=labels,loc='lower center', ncol=len(newdata.index.values),bbox_to_anchor=(0., -0.15, 0.95, .1))
plt.savefig('waffle1.png')

'''
possible cmaps
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap,
 CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, 
 OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, 
 Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, 
 PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, 
 RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, 
 Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, 
 YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, 
 bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, 
 coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, 
 gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r,
 gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r,
 gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, 
 inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r
 , pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, 
 spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, 
 tab20c, tab20c_r, terrain, terrain_r, twilight, twilight_r, twilight_shifted, 
 twilight_shifted_r, viridis, viridis_r, winter, winter_r
'''