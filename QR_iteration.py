##QR Decomposition
##This code follows the pseudocode on pp. 608-609 of Burden's Numerical Analysis


#Package imports
import numpy as np





#Input matrix H0
##H0= np.array(
## [[ 4.   ,    3.  ,     0.  ,     0.     ],
## [ 3.    ,   3.33333 , 1.66666 , 0.     ],
## [ 0.    ,   1.66666 ,-1.31999 ,-0.90667],
## [ 0.   ,    0.   ,   -0.90667 , 1.98666]])

##H0= np.array( [[ 1. ,      5.38516,  0. ,      0.     ],
## [ 5.38516 ,14.7931 ,  7.18417 , 0.     ],
## [ 0.  ,     7.18417 ,-5.14379,  0.96201],
## [ 0. ,      0.   ,    0.96201 , 5.35069]] )

##H0= np.array(
## [[ 1.   ,    5.38516 , 0.  ,     0.     ],
## [ 5.38516 ,14.7931  , 7.18417 , 0.     ],
## [ 0.   ,    7.18417, -5.14379  ,0.96201],
## [ 0.  ,     0.   ,    0.96201 , 5.35069]])

#H0 = np.array([[3,1,0],[1,3,1],[0,1,3]])




#Input initial matrix A
A=np.array([[1,2,3,4],[2,4,9,7],[3,9,1,1],[4,7,1,10]])


#Function to convert A to an upper Hessenberg matrix
def upper_Hessenberg(A):

    ##Algorithm begins here
    #Dimension of matrix
    n = A.shape[0]

    k=0
    while k < n-2:
        #Pick out appropriate w_k vector from column k
        w = A[k+1:,k]
        #print('w=',w,'\n')
        
        #Compute unit vector v
        v = (w - np.linalg.norm(w)*np.eye(n-k-1)[:,0])/(np.linalg.norm(w - np.linalg.norm(w)*np.eye(n-k-1)[:,0]))

        #Compute rotation matrix
        P = np.array(np.eye(n-k-1)-2*np.outer(v,v.T))
        #print('P= \n',P,'\n')

        #Create identity matrix with rotation matrix in lower right corner
        B = np.eye(n)
        B[k+1:,k+1:] = P

        #Compute H
        A = np.round(B@A@B,5)
        #print('A',k+1,'= \n',A,'\n')

        #Increment the loop
        k+=1

    #Return converted A
    return A



H0=upper_Hessenberg(A)

print('H0= ','\n',H0)


#Maximum number of iterations
N = 50

#Tolerance
TOL = 0.0001





##Algorithm begins here
#Dimension of matrix
n = H0.shape[0]

H=H0
j=1
while j < N:
    Q = np.eye(n)

    for k in range(0,n-1):
        #Pick out appropriate w_k vector from column k
        v = H[k:k+2,k]
        #print('v=',v,'\n')

        #Create 2x2 rotation matrix to insert
        Rtheta = np.array([[v[0], v[1]],[-v[1],v[0]]])/np.linalg.norm(v)
        #print('Rtheta= \n',Rtheta)

        #Create identity matrix and insert Rtheta in the approprate space
        Rot = np.eye(n)
        Rot[k:k+2,k:k+2] = Rtheta
        #print('Rot= \n',Rot,'\n')

        #Compute inverse of rotation matrix and multiply it by the previous one
        Rot_inv = np.linalg.inv(Rot)
        Q = Q@Rot_inv
        #print('Q= \n',Q,'\n')

        #Compute R
        R = np.round(Rot@H,5)
        #print('R= \n',R,'\n')
        H = R

    #print('R',j-1,'= \n',H,'\n')
    #print('Q',j-1,'= \n',Q,'\n')
    
    H = np.round(R@Q,5)
    print('H',j,'= \n',H,'\n')
    #print(np.linalg.norm(H.diagonal(1)))

    if np.linalg.norm(H.diagonal(1)) <= TOL:
        print('H^*= \n',H,'\n')
        print('Eigenvalues of A are approximately: ',np.diagonal(H))
        break
    else:
        j+=1
else:
    print('Maximum number of iterations exceeded.')


    
    
    
