import numpy as np
import matplotlib.pyplot as plt
import binascii


i=0
fh = open("./2019-11-25-18-34-03--novatel_CPT7-2019_11_25_18_29_34.dif","r")

line = fh.readline()

x = np.linspace(0, 10, 500)
dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off


x_test = np.linspace(0, 10, 500)

x_test = np.linspace(0, 10, 500)
y_test = 1



fig, ax = plt.subplots()
for i in range(10):
	line1, = ax.plot(i, i + 1, '--', linewidth=2,
                 label='Dashes set retroactively')


'''
line1, = ax.plot(x_test, x_test + 1, '--', linewidth=2,
                 label='Dashes set retroactively')
line1.set_dashes(dashes)

line2, = ax.plot(3, 3, dashes=[30, 5, 10, 5],
                 label='Dashes set proactively')
i += 1
'''

'''
line3, = ax.plot(x, np.sin(x), '--', linewidth=2,
                 label='Dashes set retroactively')
line3.set_dashes(dashes)
'''

ax.legend(loc='lower right')
plt.show()


















