import matplotlib.pyplot as plt
import numpy as np
fig,axe=plt.subplots()
data_m=(40, 60, 120, 180, 20, 200)
data_f=(30, 100, 150, 30, 20, 50)
index = np.arange(6)
width=0.4
opacity=0.4
axe.barh(index, data_m, width, 
        color='c', 
        align='center',
        alpha=opacity,
        label='men')
axe.barh(index, data_f, width, 
        color='b',
        align='edge',
        alpha=opacity, 
        label='women')
axe.set_yticks(index + width / 2)
axe.set_yticklabels(('Taxi','Metro','Walk','Bus','Bicycle','Driving'))
axe.legend()
plt.show()
