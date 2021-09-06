import matplotlib.pyplot as plt
import numpy as np
import math
r=np.arange(0,10,10)
theta=2*np.pi*r
ax=plt.subplot(111,projection='polar')
ax.plot(theta,r)
ax.set_rmax(20)
ax.set_rticks([2,4,6,8,10,12,14,16,18,20])
for curve in [[[45,90], [10, 12]]]:
        curve[0] = np.deg2rad(curve[0])
        ax.plot(curve[0], curve[1])
for curve in [[[90,90], [0, 12]]]:
        curve[0] = np.deg2rad(curve[0])
        ax.plot(curve[0], curve[1])
        
for curve in [[[45,45], [0, 10]]]:
        curve[0] = np.deg2rad(curve[0])
        ax.plot(curve[0], curve[1])

x=(90+45)/2                                                     #formula for finding theta value of point D
y=(90-45)/2
d=(2*12*10*math.cos(math.radians(y)))/(12+10)                   #formula for 'r' of point D.

theta = [i/180*np.pi for i in  [45,90,x]]
# Radius
radius = [10,12,round(d,2)]

ax.scatter(theta,radius, c ='r')
for t, r in zip(theta, radius):
    ax.annotate("{},{}".format(r,int(t*180/np.pi)), xy=[t, r], fontsize=10)

for curve in [[[x,x], [0, d]]]:
        curve[0] = np.deg2rad(curve[0])
        ax.plot(curve[0], curve[1])
print("To find coordinates of point 'D' which intersects line joining 'A' and 'B' and angle bisector of angle AOD ")
print("A(r1,\u03B81)=(12,90)")
print("O(r',\u03B8')=(0,0)")
print("B(r2,\u03B82)=(10,45)")
print("D(r,\u03B8)=(",d,",67.5)")