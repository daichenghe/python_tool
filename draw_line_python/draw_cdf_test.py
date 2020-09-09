#!/usr/bin/python
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from pylab import *
import xlrd
#from xlrd import open_workbook
import math
import numpy as np
from scipy.stats import norm

test_cdf = []

test_cdf = norm.cdf([1,2,1,1,8,10])
print test_cdf