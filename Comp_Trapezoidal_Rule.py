##Composite Trapezoidal Rule


#Package imports
import numpy as np

#Enter endpoints as a tuple
E = (0,np.pi/2)

#Enter mesh size
N = 40

#Set increment
dx = np.abs(E[1]-E[0])/N

#Define function to use
def f(x):
    return np.cos(x)

#Set initial input as left endpoint
x = E[0]

totalArea = 0
i=0
while i <= N:
    area = dx/2*(f(x) + f(x + dx))
    totalArea += area
    x = x + dx
    i += 1
    #print(totalArea)

print(totalArea)
