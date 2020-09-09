#!/usr/bin/python
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pylab import *
import xlrd
from xlrd import open_workbook
import math


x_data=[]
y_data=[]
x_volte=[]
temp=[]
wb = open_workbook('test.xlsx')
#fh = open("2019-11-25-18-34-03--novatel_CPT7-2019_11_25_18_29_34.dif","r")
for s in wb.sheets():
#line = fh.readline()
#line_count = 0
#while line:
	#ret = line.split(',')
    #print 'Sheet:',s.name
	#print ret[5]
	#line = fh.readline()  
	#x_data.append(ret[4])
	#y_data.append(ret[5])
	#math.sqrt( x )
	
    for row in range(s.nrows):
        print 'the row is:',row
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print values
        x_data.append(values[0])
        y_data.append(values[1])
	
plt.plot(x_data, y_data, 'bo-',label=u"Phase chart",linewidth=1)


plt.title(u"chart")
plt.legend()

ax = gca()
'''
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
'''
plt.xlabel(u"data5")
plt.ylabel(u"data6")

plt.show()
print 'over!'
