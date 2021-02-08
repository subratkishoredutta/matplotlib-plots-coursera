# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 03:43:11 2021

@author: Asus
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
novel=  open('alice_novel.txt','r').read()
stopwords=set(STOPWORDS)
stopwords.add('said')

WC=WordCloud(
        background_color='black',
        max_words=200,
        stopwords=stopwords
        )

WC.generate(novel)
fig=plt.figure()
fig.set_figwidth(10)
fig.set_figheight(5)
plt.imshow(WC, interpolation='bilinear')
plt.axis('off')
plt.savefig('wordcloud.png')
plt.show()