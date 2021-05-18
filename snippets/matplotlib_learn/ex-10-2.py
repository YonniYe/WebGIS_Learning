import matplotlib.pyplot as plt
import numpy as np
#fig=plt.figure()
fig,axe=plt.subplots()
#plot1
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
axe.plot(t,s,color='k',linestyle='-',label='line1')
#plot2
s = np.sin(2 * np.pi * (t+0.5))
axe.plot(t,s,color='c',linestyle='--', label='line2')
#ticks styles
axe.set_xticks(np.arange(0.0,2.5,0.5))
axe.set_yticks([-1,0,1])
axe.minorticks_on()
#axis position
axe.spines['right'].set_color('none')
axe.spines['top'].set_color('none')
axe.spines['bottom'].set_position(('data', 0))
axe.spines['left'].set_position(('data', 0))
#legend
axe.legend(loc='upper right',bbox_to_anchor=(1.1, 1))
plt.show()