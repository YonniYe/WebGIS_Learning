import numpy as np
import mpl_toolkits.mplot3d 
import matplotlib.pyplot as plt
x, y = np.mgrid[-2:2:20j, -2:2:20j] 
z = x * np.exp( - x**2 - y**2)
ax = plt.subplot(121, projection='3d')
ax.plot_surface(x, y, z, 
               rstride=1, 
               cstride=1, 
               cmap = plt.cm.Blues_r,alpha=0.7) 
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.subplot(122)
plt.plot(x,z)
plt.show()