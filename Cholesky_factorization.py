##Cholesky factorization
##This code follows the pseudocode on p. 419 of Burden's Numerical Analysis

#Package imports
import numpy as np



#Dimension of matrix
n=4

#Matrix A. Note: Matrix A must be symmetric and positive definite
A=np.array([[1,2,3,4],[2,5,7,9],[3,7,11,14],[4,9,14,19]])

##n=2
##A=np.array([[3,4],[8,-2]])

#Set entries type to float, print A
A=A.astype(float)
print('A= ',A)


#Algorithm begins here
#Make L an nxn 0 matrix to begin
L=np.zeros((n,n))
L=L.astype(float)

##Step 1
L[0][0] = np.sqrt(A[0][0])

#Step 2
for j in range(1,n):
    L[j][0] = A[j][0]/L[0][0]

##Step 3
for i in range(1,n-1):
    ##Step 4
    #Create an empty array
    B=np.empty(0)
    B=B.astype(float)
    
    #Create an array of values for L[i][k]**2
    for k in range(0,i):
        B=np.append(B,L[i][k]**2)

    #Add those values up
    S1=np.sum(B)

    #Assign L[i][i]
    L[i][i] = np.sqrt(A[i][i]-S1)

    ##Step 5
    for j in range(i,n):
        #Create an empty array
        C=np.empty(0)
        C=C.astype(float)
        
        #Create an array of values for L[j][k]*L[i][k]
        for k in range(0,i):
            C=np.append(C,L[j][k]*L[i][k])

        #Add those values up
        S2=np.sum(C)

        #Assign L[j][i]
        L[j][i] = (A[j][i]-S2)/L[i][i]

##Step 6
#Create an empty array
D=np.empty(0)
D=D.astype(float)

#Create an array of values for L[n-1][k]**2
for k in range(0,n):
    D=np.append(D,L[n-1][k]**2)

#Add those values up
S3=np.sum(D)

#Assign L[n-1][n-1]
L[n-1][n-1] = np.sqrt(A[n-1][n-1]-S3)

#Print L
print(L)
