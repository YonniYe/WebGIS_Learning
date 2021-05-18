import matplotlib.pyplot as plt
import numpy as np
#random data
N = 60
np.random.seed(100)
x = np.random.rand(N)
y = np.random.rand(N)
fig,axe=plt.subplots()
axe.scatter(x, y)
plt.show()