#!/usr/bin/env python3
# by lgarciaorozco@gmail.com
# Ploting cosine function
# GNU/GPL

import matplotlib.pyplot as plt
import numpy as np
from math import pi

#N = 100
#A = 0
#B = 2*3.1416

#dx = (B-A)/N
#x_a = A

#for i in range(N):
#    print(x_a)
#    x_a = x_a + dx*i
    
x = np.arange(-pi,pi,0.00001)
y = np.cos(x)
y_2 = np.sin(x)

plt.plot(x,y,'-m',x,y_2,'-r')
plt.ylabel('Cosine')
plt.show()