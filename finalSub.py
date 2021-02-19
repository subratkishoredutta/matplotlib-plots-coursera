# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:23:15 2021

@author: Asus
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
data=pd.read_csv('TheSurvey.csv',index_col=0)
data.sort_values(by='Very interested', ascending=False, inplace=True)
ax=(data.div(data.sum(axis=1),axis=0)).plot(kind="bar",figsize=(20,8),width=0.8,color=['#5cb85c','#5bc0de','#d9534f'])
plt.legend(labels=data.columns,fontsize= 14)
plt.title("Percentage of Respondents' Interest in Data Science Areas",fontsize= 16)

plt.xticks(fontsize=14)
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.yticks([])

# Add this loop to add the annotations

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.annotate('{:.0%}'.format(height), (x, y + height + 0.01))

plt.show()

data=pd.read_csv('police.csv',index_col=0)
data.rename(columns={'PdDistrict':'Neighborhood'},inplace=True)
new=data.groupby(['Neighborhood']).size().reset_index(name='Count')
print(new) 