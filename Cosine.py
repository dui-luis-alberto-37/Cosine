#!/usr/bin/env python3
# by lgarciaorozco@gmail.com
# Ploting cosine function
# GNU/GPL

import matplotlib.pyplot as plt
from math import cos
x = range(0,1000000,31416)
x = [i//10000 for i in x]
y = [cos(i) for i in x]
x_a = 0
dx = 3.1416
for i in range(8):
    print(x_a)
    x_a = x_a + dx*i
    

# plt.plot(x,y)
# plt.ylabel('Cosine')
# plt.show()