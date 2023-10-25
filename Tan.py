#!/usr/bin/env python3
# by lgarciaorozco@gmail.com
# Ploting cosine function
# GNU/GPL

import numpy  as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi/2,np.pi/2,100, endpoint=False)[1:]
y = np.tan(x)
print(y)

plt.plot(x,y,'-m')
plt.yscale('linear')
plt.xscale('linear')
plt.ylabel('Cosine')
plt.grid()


plt.show()