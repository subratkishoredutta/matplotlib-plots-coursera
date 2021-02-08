# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 04:22:47 2021

@author: Asus
"""

from wordcloud import WordCloud,STOPWORDS
import cv2
import numpy as np

stopwords=set(STOPWORDS).add('said')
novel=open('alice_novel.txt','r').read()
Amask=cv2.imread('alice_mask.png')
Amask=cv2.cvtColor(Amask,cv2.COLOR_BGR2GRAY)

WC=WordCloud(
        background_color='white',
        mask=Amask,
        max_words=200,
        stopwords=stopwords
        )

WC.generate(novel)
fig=plt.figure()
fig.set_figwidth(10)
fig.set_figheight(5)
plt.imshow(WC, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloudmask.png')
plt.show()