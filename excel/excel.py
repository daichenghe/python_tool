import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import sys
'''
x = np.linspace(0, 2000, 2000)
y1 = x + 3      # 曲线 y1
y2 = 3 - x      # 曲线 y2
plt.figure()    # 定义一个图像窗口
plt.plot(x, y1) # 绘制曲线 y1
plt.plot(x, y2) # 绘制曲线 y2
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# np.set_printoptions(threshold=np.inf) # 去掉print省略的内容
 
# 导入数据
csv_file = sys.argv[1]


info=np.loadtxt(csv_file,dtype=str,delimiter=',',usecols=(5),unpack=True)

print(info)
i = len(info)
print(i)


wheel_tick = np.zeros(i-1, dtype = np.int) 
xx = np.zeros(i-1, dtype = np.int) 
for i in range(1,len(info)-1):
	wheel_tick[i] = int(info[i+1]) - int(info[i])
	xx[i] = i

print(len(xx))
print(len(wheel_tick))
print(xx)

plt.figure(1)                # 第一个图形
plt.subplot(2,1,1)             # 第一个图形的第一个子图。看成2行1列，当前为第1行
plt.plot(xx,wheel_tick,linewidth=0.5) 

plt.show()