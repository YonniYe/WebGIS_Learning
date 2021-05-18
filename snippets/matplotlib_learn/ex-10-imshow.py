import matplotlib.pyplot as plt
import numpy as np
img = plt.imread("lena.png")

ax0=plt.subplot(2,2,1)
ax0.imshow(img)
ax0.set_title("color")

ax1=plt.subplot(2,2,2)
ax1.imshow(img[:,:,0],cmap='gray')
ax1.set_title("R")

ax2=plt.subplot(2,2,3)
gray=np.average(img,axis=2)/255.0
m=ax2.imshow(gray,cmap='hot')
plt.colorbar(m,ax=ax2)
ax2.set_title("gray")

ax3=plt.subplot(2,2,4)
x=np.linspace(0,np.pi,20)
ax3.plot(x,np.sin(x),color='r',
        linestyle='--',marker='o',
        mec='g',lw=0.5)
ax3.imshow(img,extent=(0,2,-1,1))
ax3.set_xlim(0,np.pi)
ax3.set_title("origin=lower")

plt.show()