##Enter given functions and partial derivatives here
def F(x): return x**2+x-1

##Prompts user for left and right endpoints, tolerance, and number of iterations
a = float(input('What is the left endpoint? '))
b = float(input('What is the right endpoint? '))
TOL = float(input('What is the tolerance? '))
N = int(input('What is the maximum number of iterations? '))


i=0
while i<=N:
    x=a+(b-a)/2
    Fx=F(x)
    print('i='+str(i),'a='+str(a),'b='+str(b),'Midpoint:', x,'F(x)='+str(Fx))
    ##prints lines for LaTeX table
    #print(i,'&', a,'&', b,'&', x,'&', Fx,'&', b-a,'\\\\')
    if Fx==0 or (b-a)<TOL:
        print('x^* =',x)
        break

    i+=1
    Fa=F(a)
    if Fa*Fx>0:
        a=x
        Fa==Fx
    else:
        b=x
else: print('Bisection method failed after',N,'iterations.')
