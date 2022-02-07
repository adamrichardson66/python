##LU decomposition
##This code follows the pseudocode on p. 406 of Burden's Numerical Analysis

#Package imports
import numpy as np
from scipy import linalg

#Dimension of matrix
n=4

#Matrix A
A=np.array([[1,2,3,4],[1,3,4,5],[1,3,5,6],[1,3,5,7]])

#Set entries type to float, print A
A=A.astype(float)
print('A= ',A)



#Algorithm begins here
#Make L an nxn identity matrix to begin
L=np.eye(n)
L=L.astype(float)

##Step 1
if A[0][0]==0:
    print('Factorization impossible.')
else:
    #Make U an nxn 0 matrix and assign first entry of A to first entry of U
    U=np.zeros((n,n))
    U=U.astype(float)
    U[0][0] = A[0][0]

##Step 2
for j in range(1,n):
    U[0][j]=A[0][j]/L[0][0]
    L[j][0]=A[j][0]/U[0][0]

    

##Step 3
for i in range(1,n-1):
    ##Step 4
    #Create an empty array
    B=np.empty(0)
    B=B.astype(float)
    
    #Create an array of values for L[i][k]*U[k][i]
    for k in range(0,i):
        B=np.append(B,L[i][k]*U[k][i])
       
    #Add those values up
    S1=np.sum(B)
    
    #Assign U[i][i]
    U[i][i]=(A[i][i]-S1)/L[i][i]

    #Check if factorization impossible
    if U[i][i]==0:
        print('Factorization impossible.')
        break

    ##Step 5
    for j in range(i,n):
        #Create empty arrays
        C=np.empty(0)
        C=C.astype(float)
        D=np.empty(0)
        D=D.astype(float)

        #Create arrays of values for L[i][k]*U[k][j] and L[j][k]*U[k][i]
        for k in range(0,i):
            C=np.append(C,L[i][k]*U[k][j])
            D=np.append(D,L[j][k]*U[k][i])

        #Add those values up
        S2=np.sum(C)
        S3=np.sum(D)

        #Assign U[i][j] and L[j][i]
        U[i][j]=(A[i][j]-S2)/L[i][i]
        L[j][i]=(A[j][i]-S3)/U[i][i]


##Step 6
#Create an empty array
E=np.empty(0)
E=E.astype(float)

#Create array of values for L[n-1][k]*U[k][n-1]
for k in range(0,n):
    E=np.append(E,L[n-1][k]*U[k][n-1])

#Add thos values up
S4=np.sum(E)

#Assign U[n-1][n-1]
U[n-1][n-1]=(A[n-1][n-1]-S4)/L[n-1][n-1]


#Print resulting L and U
print('L= ')
print(L)
print('U= ')
print(U)


#Check result with scipy.linalg.lu
##(P,L2,U2) = linalg.lu(np.transpose(A))
##print('linalg.lu in scipy produces: ')
##print('P= ')
##print(P)
##print('L= ')
##print(L2)
##print('U= ')
##print(U2)


#Compute inverses and assign vector b
L_inv = linalg.inv(L)
U_inv = linalg.inv(U)
A_inv = U_inv.dot(L_inv)
b = np.array([[0],[1],[1],[1]])

#Print inverse matrices
print('L_inv= ')
print(L_inv)
print('U_inv= ')
print(U_inv)

#Solve Ax=b for x via the inverses and print result
print('x = A_inv(b)= ')
print(A_inv.dot(b))
