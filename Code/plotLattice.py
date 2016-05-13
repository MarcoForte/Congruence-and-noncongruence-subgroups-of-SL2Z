# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:57:13 2016

@author: Marco
"""

import matplotlib.pyplot as plt
import numpy as np
c = np.array(range(0,10))
d = np.array(range(-10,10))
x = 0.3
y = 1.43

for i in c:
    plt.plot(i*x + d, i*y*np.ones(len(d)), 'ko')
plt.xlim(-6.1,6.1)
plt.ylim(0,6)
plt.annotate(s= "0.3 + 1.43i", xy = (0.3,1.43), xytext = (0.4,0.7),  arrowprops=dict(facecolor='black',  headwidth = 0.4, width = 0.2))
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_smart_bounds(True)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.gca().set_aspect('equal', adjustable='box')

plt.xticks(np.arange(-6,7, 1.0))
plt.yticks(np.arange(1,7, 1.0))
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',) 
plt.savefig("lattice.png",dpi = 1000)