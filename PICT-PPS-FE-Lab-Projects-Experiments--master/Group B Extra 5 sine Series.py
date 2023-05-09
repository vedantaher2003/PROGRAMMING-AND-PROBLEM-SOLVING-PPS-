'''
Problem Statement:Write a Program in Python to accept the number of terms a finds the
sum of sine series.
'''
n=int(input("Enter the limit of series:"))
angle=float(input("Enter value:"))
def factorial(x):
    fac=1
    for i in range(1,x+1):
        fac=fac*i
    return fac
for j in range(0,n):
    pi = 22 / 7
    x = angle *(pi / 180)
    sin=0
    sign=(-1)**n
    f=factorial(2*j+1)
    sin=sin+(x**(2*j+1))/f*sign
print(sin)



