import matplotlib.pyplot as plt
import numpy as np
fig, axe = plt.subplots()
labels = 'Taxi', 'Metro', 'Walk', 'Bus','Bicycle','Drive'
sizes = [10, 30, 5, 25, 5, 25]
explode = (0, 0.1, 0, 0, 0, 0)
axe.pie(sizes, explode=explode, 
        labels=labels,
        autopct='%1.1f%%',
        shadow=True, 
        startangle=90)
#axe.axis('equal')
#axe.axis('tight')
axe.set_title('pie chart')
plt.show()
