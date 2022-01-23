##Enter given function here
def f(x): return x**2-2

##Prompts user for left/right endpoints, tolerance, and number of iterations
p0 = float(input('What is the first initial point? '))
p1 = float(input('What is the second initial point? '))
TOL = float(input('What is the tolerance? '))
N = int(input('What is the maximum number of iterations? '))


i=2
q0=f(p0)
q1=f(p1)

print('p_0 =',p0)
print('p_1 =',p1)
while i<= N:
    p=p1-q1*(p1-p0)/(q1-q0)
    print('p_'+str(i),'=',p)
    #print(i,'&', p,'&', abs(p-p1),'\\\\')
    if abs(p-p1)<TOL:
        print('p^* =',p)
        break
    i+=1
    p0=p1
    q0=q1
    p1=p
    q1=f(p)
else: print('Secant method failed after',N+1,'iterations.')
