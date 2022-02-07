##Power Method
##This code follows the pseudocode on pp. 418-419 of Burden's Numerical Analysis,
##but uses the Frobenius norm instead of the infinity norm.
##NOte also this 

#Package imports
import numpy as np



#Dimension of matrix
n=3

#Matrix A
A=np.array([[2,1,1],[1,2,1],[1,1,2]])

#Initial vector
x=np.array([[1],[-1],[2]])
x=x.astype(float)

#Tolerance
TOL=0.0001

#Maximum number of iterations
N=1000


#Algorithm begins here
##Step 1
k=1

##Step 2 and 3
#Create unit vector in the direction of x using Frobenius norm
x = x/np.linalg.norm(x)

##Step 4
while k <= N:
    ##Step 5
    #Set y equal to the output Ax
    y = A.dot(x)

    ##Step 6 and 7
    #Set mu equal to the Frobenius norm of y
    mu = np.linalg.norm(y)

    ##Step 8
    if mu==0:
        print(x)
        print('A has the eigenvalue 0, select a new starting vector x and restart.')
        break

    ##Step 9
    ERR = np.linalg.norm(x - (y/mu))
    x = y/mu

    #Prints lines for LaTeX table
    #print(k,'&',mu, '&', np.transpose(x),'\\\\[2mm]')
    
    print('Approximation #',k)
    print('lamba_1 ≈ ', mu)
    print('v ≈ ',x,'\n')
    
    ##Step 10
    if ERR < TOL:
        print('Final approximation')
        print('lamba_1 ≈ ', mu)
        print('v ≈ ',x,'\n')
        break

    ##Step 11
    #Increment k for the while loop
    k+=1

##Step 12
else: print('Maximum number of iterations exceeded.')





