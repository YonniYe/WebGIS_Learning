import matplotlib.pyplot as plt
import numpy as np
#random data
N = 60
np.random.seed(100)
x = np.random.rand(N)
y = np.random.rand(N)
s = np.pi * (10 * np.random.rand(N))**2 
c = -s
opacity=0.7
fig,axe=plt.subplots()
axe.scatter(x, y, s, c, alpha=opacity,marker='*')
plt.show()
