import matplotlib.pyplot as plt
import numpy as np
#random data
data = np.random.standard_normal(1000)
nb = 50
fig, ax = plt.subplots()
n, bins, patch=ax.hist(data, nb,density=True)
#standard normal distribution
std= ((1 / (np.sqrt(2 * np.pi) * 1))
      *np.exp(-0.5 * (1 / 1* (bins - 0))**2))
ax.plot(bins,std,0,'-')
plt.show()