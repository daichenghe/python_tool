#!/usr/bin/python
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pylab import *
import xlrd
#from xlrd import open_workbook
import math
import numpy as np
from scipy.stats import norm


def get_cdf(data):
	cdf_data = []
	count = len(data)
	for i in range(count):
		count_now = (float)(i)
		one_cdf = count_now/count
		cdf_data.append(one_cdf)
	return cdf_data


x_data=[]
y_data=[]
X_pow = []
X = []
Y = []
x_chart = []
y_chart = []
x_sort = []
#wb = open_workbook('test.xlsx')
fh = open("2019-11-25-18-34-03--novatel_CPT7-2019_11_25_18_29_34.dif","r")
#for s in wb.sheets():
line = fh.readline()
line_count = 0
count_over = 0
count_low = 0

while line:
	ret = line.split(',')
    #print 'Sheet:',s.name
	#print ret[5]
	line = fh.readline()  
	#x_data.append(ret[4])
	#y_data.append(ret[5])
	#x1_float = (float)(ret[4])
	#x2_float = (float)(ret[5])
	
	x1_float = (float)(ret[4])
	x2_float = (float)(ret[5])	
	x1_2 = pow(x1_float,2)
	x2_2 = pow(x2_float,2)
	#math.sqrt( x )
	#X_pow.append(sqrt(x2+y2))
	x_sqrt = sqrt(x1_2 + x2_2)
	if x_sqrt < 0.5:
		count_low += 1
	else:
		count_over += 1
	x_chart.append(x_sqrt)
	'''
    for row in range(s.nrows):
        print 'the row is:',row
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print values
        x_data.append(values[0])
        y_data.append(values[1])
	'''
#plt.plot(x_data, y_data, 'bo-',label=u"Phase chart",linewidth=1)
'''
y_chart.append(np.percentile(X_pow, 50))
y_chart.append(np.percentile(X_pow, 68))
y_chart.append(np.percentile(X_pow, 95))
y_chart.append(np.percentile(X_pow, 99))
'''
x_chart.sort()
print x_chart
y_chart_2 = norm.cdf(x_chart)
'''
for mem in x_chart:
	if mem < 0:
		print "test"
		print mem
'''
count = len(x_chart)
y_cdf = 0.0
'''
for i in range(count):
	test = (float)(i)
	y_cdf = test/count
	y_chart.append(y_cdf)
'''
y_chart = get_cdf(x_chart)

#print x_chart
#print y_chart
'''
x_chart.append(50)
x_chart.append(68)
x_chart.append(95)
x_chart.append(99)
'''

plt.plot(x_chart, y_chart, 'bo-',label=u"data chart",linewidth=1)

#plt.plot(x_chart, y_chart_2, 'bo-',label=u"data chart_lib",linewidth=1)


plt.title(u"chart")
plt.legend()

'''
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
'''
plt.xlabel(u"Horizontal error")
plt.ylabel(u"CDF")

test_cdf = norm.cdf([0,2,5,10])
print test_cdf

print "radio"
print count_low
print count_over
plt.show()
print 'run!'













































