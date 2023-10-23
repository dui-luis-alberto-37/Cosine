#!/usr/bin/env python3
# by lgarciaorozco@gmail.com
# Ploting cosine function
# GNU/GPL

import matplotlib.pyplot as plt
from math import cos
x = range(0,1000000,31416)
x = [i//10000 for i in x]
y = [cos(i) for i in x]

plt.plot(x,y)
plt.ylabel('Cosine')
plt.show()