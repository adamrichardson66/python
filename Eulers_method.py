##Composite Trapezoidal Rule


#Package imports
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt





#Analytical solution
x = np.arange(0.,5., 0.01)
y = np.exp(-15*x)
plt.plot(x,y)

#Set initial condition
x0 = 0
y0 = 1

#Set mesh size
#h = 1/4
#h = 2/15
h = 1/1000

###Set max number of iterations
N = 5/h


i=0
while i < N:

    x1 = x0 + h
    y1 = y0 + h*(-15*np.exp(-15*x0))

    plt.plot([x0,x1],[y0,y1])
    
    x0 = x1
    y0 = y1

    i += 1


#Generate plot


#Set plot information and display plot
plt.suptitle('Approximate solution to ODE using Euler\'s method.')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
