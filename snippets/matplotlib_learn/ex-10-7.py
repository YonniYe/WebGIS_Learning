import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
fig,axe=plt.subplots()
#plot1
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
axe.plot(t,s,color='k',linestyle='-')
#plot2
s = np.sin(2 * np.pi * (t+0.5))
axe.plot(t,s,color='c',linestyle='--')
plt.show()
