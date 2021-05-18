import matplotlib.pyplot as plt
import numpy as np
axe=plt.gca()
tdata=[14,9,7,5,12,19,23,26,27,24,21,19]
axe.plot(np.arange(0,24,2),tdata, '-o')
axe.set_xticks(np.arange(0,24,2))
axe.annotate('hottest at 16:00',
                xy=(16, 27),
                xytext=(16, 24),
                arrowprops=dict(facecolor='black',
                                shrink=0.1),
                horizontalalignment='center', 
                verticalalignment='center')
axe.text(12, 10, 'Date: March 26th, 2018', 
         bbox={'facecolor': 'cyan', 
               'alpha': 0.3, 'pad': 6})
plt.show()
