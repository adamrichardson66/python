##Lagrange interpolation


#Package imports
import numpy as np
import sympy as sp
from sympy import *

x = symbols('x')

#List of x-coordinates of nodes
A = (0,0.5,1)

#List of function values at nodes
f = (0,1,0)



#Computes the "Dirichlet character-like" function
def L(k,a,x):
    a = list(a)
    
    #Pops out kth entry of list a and stores it as x_k
    x_k = a.pop(k)

    #Duplicates updated list a
    b = a[:]

    #Subtracts entries in a from x
    a = [x - y for y in a]

    #Subtracts entries in a from x_k
    b = [x_k - y for y in b]

    #Returns the quotient of the products of the entries of a and b
    return prod(a)/prod(b)



#Computes the Langrange interpolating polynomial
def P(f,a,x):
    P=0
    for k in range(0,len(a)):
        P += f[k]*L(k,a,x)
    return P


print(P(f,A,x))
