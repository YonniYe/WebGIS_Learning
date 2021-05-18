import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
y, x = np.ogrid[-2:2:200j, -2:2:200j]
z = x * np.exp( - x**2 - y**2)
extent = [np.min(x), np.max(x), np.min(y), np.max(y)]
plt.imshow(z, extent=extent, origin="lower",cmap='gray') 
plt.colorbar()
plt.show()
