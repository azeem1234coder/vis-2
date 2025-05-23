import matplotlib.pyplot as plt
x=[8,5,10,15,20,25,30,]
y1=[10,15,20,20,30,15,0]
y2=[10,12,15,12,20,10,0]
plt.plot(x,y1,linestyle='dashed',marker='D')
plt.plot(x,y2,linestyle='dashed',marker='D')
plt.title('veloxity-time graph')
plt.xlabel('veloxity m/s')
plt.ylabel('time (s)')
plt.xlim(5,25)
plt.ylim(5,25)
plt.legend()
plt.show()