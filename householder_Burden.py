##Householder Reflection
##This code follows the pseudocode on pp. 598-599 of Burden's Numerical Analysis


#Package imports
import numpy as np




#Dimension of matrix
n=4

#Matrix A
A=np.array([[1,2,3,4],[2,4,9,7],[3,9,1,1],[4,7,1,10]])
print('A= ','\n',A)

#Instantiating some vectors
v = np.array([0]).astype(float)
u = np.empty(0).astype(float)
z = np.empty(0).astype(float)


##Algorithm begins here
##Step 1
for k in range(0,n-2):
    ##Step 2
    B=np.empty(0).astype(float)
    
    #Create an array of values for A[j][k]**2
    for j in range(k,n):
        B=np.append(B,A[j][k]**2)

    #Assign q to the sum of those values
    q=np.sum(B)

    ##Step 3
    if A[k+1][k]==0:
        alpha = -np.sqrt(q)
    else:
        alpha = -np.sqrt(q)*A[k+1][k]/np.abs(A[k+1][k])

    ##Step 4
    RSQ = alpha**2 - alpha*A[k+1][k]

    ##Step 5
    v[k] = 0
    v = np.append(v,A[k+1][k]-alpha)
    #print(v)

    for j in range(k+1,n):
        v = np.append(v,A[j][k])
    #print(v)
    
    ##Step 6
    for j in range(k,n):
        C = np.empty(0).astype(float)
        for i in range(k,n):
                C=np.append(C,A[j][i]*v[i])
        S1 = np.sum(C)
        u = np.append(u, S1/RSQ)

    ##Step 7
    D=np.empty(0).astype(float)
    for i in range(k,n):
        D = np.append(D,v[i]*u[i])
    PROD = np.sum(D)

    ##Step 8
    for j in range(k,n):
        z = np.append(z,u[j] - (PROD/(2*RSQ))*v[j])

    ##Step 9
    for l in range(k,n-1):
        ##Step 10
        for j in range(l,n):
            A[j][l] = A[j][l] - v[l]*z[j] - v[j]*z[l]
            A[l][j] = A[j][l]
        ##Step 11
        A[l][l] = A[l][l] - 2*v[l]*z[l]

    ##Step 12
    A[n-1][n-1] = A[n-1][n-1] - 2*v[n-1]*z[n-1]

    ##Step 13
    for j in range(k+1,n):
        A[k][j] = 0
        A[j][k] = 0

    ##Step 14
    A[k+1][k] = A[k+1][k] - v[k+1]*z[k]
    A[k][k+1] = A[k+1][k]

    print('A= ','\n',A)
        
