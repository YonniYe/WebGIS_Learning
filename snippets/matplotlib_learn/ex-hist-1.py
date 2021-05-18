import matplotlib.pyplot as plt
import numpy as np
#random data
data = np.random.standard_normal((1000,2))
bins = 50
fig, ax = plt.subplots()
hist=ax.hist(data, bins)
print(hist)
ax.set_title(r'Histogram')
ax.legend(loc='best')
plt.show()
