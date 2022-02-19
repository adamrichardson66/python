##Jacobi Iteration


#Package imports
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


#Input matrix A, vector b, initial guess
A=np.array([[2,1],[1,3]])
b=np.array([1,2])

x0=np.array([1,1])

#Enter maximum number of iterations, N
N=50

#Enter desired tolerance for solution
TOL=0.0001


#Extract the matrices D and L+U, compute inverse of D
D=np.diag(np.diag(A))
LU = A-D
Dinv = np.linalg.inv(D)

print('A=\n',A)
print('b=',b,'\n')
##print('D=\n',D)
##print('L+U=\n',LU)
##print('Dinv=\n',Dinv)

x=x0
print('x 0=',x)

#Setup array to collect approximations
xstack=np.array([x0])


k=1
while k <= N:
    #Record previous approximation as p
    p = x

    #Update x using Jacobi iteration and print the new approximation
    x = -Dinv@LU@x.T+Dinv@b
    print('x',k,'=',x)
    #print(k, '&', x, '&',round(np.linalg.norm(p-x)/np.linalg.norm(x),4),'\\\\[2mm]') 

    #Append new approximation to the stack
    xstack = np.append(xstack,[x],axis=0)

    #Test for success
    if (np.linalg.norm(p-x)/np.linalg.norm(x))<TOL:
        print('x^*=',x)
        break
    else:
        k+=1

#Compare to np.linalg.solve
#print('X^*=',np.linalg.solve(A, b))

#Generate plot of the approximations
for i in range(len(xstack)):
    plt.scatter(xstack[i][0],xstack[i][1],s=10)
    #plt.text(xstack[i][0],xstack[i][1],'x^'+str(i))

#Set plot information and display plot
plt.suptitle('Approximations Using Jacobi Iteration')
plt.xlabel('x^(k)_1')
plt.ylabel('x^(k)_2')
plt.show()














