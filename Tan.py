#!/usr/bin/env python3
# by lgarciaorozco@gmail.com
# Ploting cosine function
# GNU/GPL

import numpy  as np
import matplotlib.pyplot as plt
for i in range(-8,8,2):
    x = np.linspace((i+1)*np.pi/2,(i+3)*np.pi/2,100, endpoint=False)[1:]
    y = np.tan(x)
    print(y)

    plt.plot(x,y,'-m')
    plt.ylabel('Cosine')
    

plt.grid()
plt.show()