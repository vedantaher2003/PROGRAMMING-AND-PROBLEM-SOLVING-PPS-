'''
Problem Statement:Write a program in Python to accept the number and Compute
a) square root of number,
b) Square of number,
c) Cube of number
d) check for prime,
e) factorial of number
f) prime factors
'''
def sqroot(x):
    s=x**0.5
    print("Square Root is:",s)
def square(x):
    s=x**2
    print("Square of the number is:",s)
def cube(x):
    s=x**3
    print("Cube of the Number is:",s)
def prime(x):
    n = 0
    for i in range(2, x):
        if (x % i == 0):
            n = 1
            break
    if (n == 1):
        print("Number is not prime")
    else:
        print("Number is Prime")
def factorial(x):
    f=1
    for i in range(1,x+1):
        f=f*i
    print("Factorial is:",f)
x=int(input("Enter your Number:"))
if(x>0):
    sqroot(x)
    square(x)
    cube(x)
    prime(x)
    factorial(x)
else:
    print("Please enter a positive number!")
