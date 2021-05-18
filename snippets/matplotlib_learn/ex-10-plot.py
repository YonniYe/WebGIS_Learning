import matplotlib.pyplot as plt
import numpy as np
fig,axe=plt.subplots()
np.random.seed(100)
x=np.arange(0, 10, 1)
y1=np.random.rand(10)
y2=np.random.rand(10)
axe.plot(x, y1, '-o', color='c')
axe.plot(x, y2, '--o', color='b')
plt.show()