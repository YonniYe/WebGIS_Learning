
def pi_formatter(x, pos): 
	m = np.round(x / (np.pi/4))
	n = 4
	while m!=0 and m%2==0: m, n = m//2, n//2
	if m == 0:
		return "0"
	if m == 1 and n == 1:
		return r"$\pi$"
	if n == 1:
		return r"$%d \pi$" % m
	if m == 1:
		return r"$\frac{\pi}{%d}$" % n
	return r"$\frac{%d \pi}{%d}$" % (m,n)
    
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter 
import numpy as np

x = np.arange(0, 4*np.pi, 0.01)
y = np.sin(x)
plt.figure(figsize=(8,4))
plt.plot(x, y)
ax = plt.gca()

# 主刻度为pi/4
ax.xaxis.set_major_locator( MultipleLocator(np.pi/4) )
# 主刻度文本用pi_formatter函数计算
ax.xaxis.set_major_formatter( FuncFormatter( pi_formatter ) )
# 副刻度为pi/20
ax.xaxis.set_minor_locator( MultipleLocator(np.pi/20) )
# 设置刻度文本的大小
for tick in ax.xaxis.get_major_ticks():
	tick.label1.set_fontsize(16)
plt.show()
plt.show()
