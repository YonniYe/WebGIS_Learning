import matplotlib.pyplot as plt
import numpy as np
fig,axe=plt.subplots()
data_m=(40, 60, 120, 180, 20, 200)
data_f=(30, 100, 150, 30, 20, 50)
index = np.arange(6)
width=0.4
axe.bar(index, data_m, width, color='c', label='men')
axe.bar(index+width, data_f, width, 
        color='b', 
        label='women')
axe.set_xticks(index + width / 2)
labels=('Taxi','Metro','Walk','Bus','Bicycle','Driving')
axe.set_xticklabels(labels)
axe.legend()
plt.show()
