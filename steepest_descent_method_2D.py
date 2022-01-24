##Imports the math class so we can use the sqrt function
import math as m

##Enter given functions and partial derivatives here
def g(x,y): return m.cos(x+y)+m.sin(x)+m.cos(y)
def g_x(x,y): return -m.sin(x+y)+m.cos(x)
def g_y(x,y): return -m.sin(x+y)-m.sin(y)


##Prompts user for initial guess, tolerance, and number of iterations
x0 = list(float(x.strip()) for x in input('Enter initial guess as a list: x,y ').split(','))
TOL = float(input('What is the tolerance? '))
N = int(input('What is the maximum number of iterations? '))

i=0
while i<=N:
    g1 = g(x0[0],x0[1])
    z = [g_x(x0[0],x0[1]), g_y(x0[0],x0[1])]
    z0 = m.sqrt((g_x(x0[0],x0[1]))**2+(g_y(x0[0],x0[1]))**2)

    if z0 == 0:
        print('Zero gradient')
        print(x0, g1)
        break
    
    z = [g_x(x0[0],x0[1])/z0, g_y(x0[0],x0[1])/z0]
    a1 = 0
    a3 = 1
    g3 = g(x0[0]-a3*z[0],x0[1]-a3*z[1])

    while g3 >= g1:
        a3 = a3/2
        g3 = g(x0[0]-a3*z[0],x0[1]-a3*z[1])

        if a3 < TOL/2:
            print('No likely improvement')
            print(x0, g1)
            break

    a2 = a3/2
    g2 = g(x0[0]-a2*z[0],x0[1]-a2*z[1])

    h1 = (g2-g1)/a2
    h2 = (g3-g2)/(a3-a2)
    h3 = (h2-h1)/a3

    a0 = 0.5*(a2-h1/h3)
    g0 = g(x0[0]-a0*z[0],x0[1]-a0*z[1])

    gmin = min(g0,g3)

    if g3==gmin: a=a3
    else: a=a0

    print('x_'+str(i),'=',x0)
    
    #Prints lines for LaTeX table
    #print(i,'&', tuple(x0),'&', g1,'&',abs(gmin-g1),'\\\\[2mm]')

    if abs(gmin-g1)<TOL:
        print('x^* =',x0)
        print('Minimum value=',g(x0[0],x0[1]))
        break
    
    x0 = [x0[0]-a*z[0], x0[1]-a*z[1]]
    
    i+=1
else: print('SD method failed after',N+1,'iterations.')
