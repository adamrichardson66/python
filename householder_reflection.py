##Householder Reflection

#Package imports
import numpy as np





#Input matrix A
A=np.array([[1,2,3,4],[2,4,9,7],[3,9,1,1],[4,7,1,10]])
#A=np.array([[4,1,-2,2],[1,2,0,1],[-2,0,3,-2],[2,1,-2,-1]])
print('A0= ','\n',A)






##Algorithm begins here
#Dimension of matrix
n = A.shape[0]

k=0
while k < n-2:
    #Pick out appropriate w_k vector from column k
    w = A[k+1:,k]
    print('w=',w,'\n')
    
    #Compute unit vector v
    v = (w - np.linalg.norm(w)*np.eye(n-k-1)[:,0])/(np.linalg.norm(w - np.linalg.norm(w)*np.eye(n-k-1)[:,0]))

    #Compute rotation matrix
    P = np.array(np.eye(n-k-1)-2*np.outer(v,v.T))
    print('P= \n',P,'\n')

    #Create identity matrix with rotation matrix in lower right corner
    B = np.eye(n)
    B[k+1:,k+1:] = P

    #Compute H
    A = np.round(B@A@B,5)
    print('A',k+1,'= \n',A,'\n')

    #Increment the loop
    k+=1
else:
    print('H= \n',A,'\n')


