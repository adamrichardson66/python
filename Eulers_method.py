##Composite Trapezoidal Rule


#Package imports
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt





#Set mesh values
#h=1/4
#h=2/15
h=1/1000

#Set initial condition
x0 = 0
y0 = 1



#Analytical solution
x = np.arange(0.,5., 0.01)
y = np.exp(-15*x)
plt.plot(x,y)

###Set max number of iterations
N = 5/h

i=0
while i < N:

    x1 = x0 + h
    y1 = y0 + h*(-15*y0)

    plt.plot([x0,x1],[y0,y1])
    plt.draw
    x0 = x1
    y0 = y1

    i += 1


#Generate plot

title='Approximate solution using Euler\'s method with mesh size h='+str(h)

#Set plot information and display plot
plt.suptitle(title)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

  
