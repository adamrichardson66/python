##Imports the math class so we can use the sqrt function
import math

##Enter given functions and partial derivatives here
def f(x,y): return x**2+y**2-25
def g(x,y): return x**2-y-2
def f_x(x,y): return 2*x
def f_y(x,y): return 2*y
def g_x(x,y): return 2*x
def g_y(x,y): return -1

##Prompts user for initial guess, tolerance, and number of iterations
x0 = list(float(x.strip()) for x in input('Enter initial guess as a list: x,y ').split(','))
TOL = float(input('What is the tolerance? '))
N = int(input('What is the maximum number of iterations? '))

##Returns vector of given functions, F(x,y)
def F(x,y): return [f(x,y),g(x,y)]

##Returns the value of the determinant of the Jacobian after evaluation at a vector x
def det(x): return f_x(x[0],x[1])*g_y(x[0],x[1])-f_y(x[0],x[1])*g_x(x[0],x[1])

#Returns the inverse of the Jacobian evaluated at a given vector x
def inverse_jac(x): return [[g_y(x[0],x[1])/det(x),-f_y(x[0],x[1])/det(x)], [-g_x(x[0],x[1])/det(x),f_x(x[0],x[1])/det(x)]]


i=0
while i<= N:
    print('x_'+str(i),'=',x0)
    Jinv = inverse_jac(x0)
    ##Method execution componentwise:
    x10 = x0[0]-(Jinv[0][0]*F(x0[0],x0[1])[0]+Jinv[0][1]*F(x0[0],x0[1])[1])
    x11 = x0[1]-(Jinv[1][0]*F(x0[0],x0[1])[0]+Jinv[1][1]*F(x0[0],x0[1])[1])
    
    x1 = [x10,x11]
    ##Stopping condition is when distance between consecutive approximations is within TOL
    if math.sqrt((x1[0]-x0[0])**2+(x1[1]-x0[1])**2)<TOL:
        print('x^* =',x0)
        break
    i+=1
    x0=x1
    
else: print('Newtons method failed after',N,'iterations.')
