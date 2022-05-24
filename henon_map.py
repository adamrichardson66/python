##Henon map plotter

#Package imports
import numpy as np
import matplotlib.pyplot as plt

#Henon map function
def henon(x, y, a=1.2, b=0.4):
    x1 = a-x**2+b*y
    y1 = x
    return x1, y1

#Set number of iterations and create lists for coordinate data
N = 1000000
X = np.zeros(N+1)
Y = np.zeros(N+1)

#Set intial point coordinates
X[0], Y[0] = 0,0

#Iterate Henon map and store coordinate results
for i in range(N):
    x1, y1 = henon(X[i],Y[i])
    X[i+1] = x1
    Y[i+1] = y1

#Plot figure 
plt.plot(X, Y,'.',markersize=0.4)
plt.show()
