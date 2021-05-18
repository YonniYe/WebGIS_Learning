import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
axe = Axes3D(fig)
# random data
N = 60
np.random.seed(100)
x = np.random.rand(N)
y = np.random.rand(N)
z= np.random.rand(N)
axe.scatter(x,y,z,marker='*')
plt.show()
