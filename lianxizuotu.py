import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(-1,100,50)#从(-1,100)均匀取50个点
y = 2 * x
plt.figure 
plt.plot(x,y)
plt.show()

x1 = np.linspace(-1,1,50)#从(-1,1)均匀取50个点
y1 = 2 * x1
plt.figure 
plt.plot(x1,y1)
plt.show()
