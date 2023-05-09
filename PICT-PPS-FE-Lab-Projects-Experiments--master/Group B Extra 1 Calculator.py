'''
Problem Statement:Write a Program in Python to simulate simple calculator that performs
basic tasks such as addition, subtraction, multiplication and division with special
operations like computing xy and x!
'''
def add(x,y):
    s=x+y
    print("Addition is:",s)
def sub(x,y):
    s=x-y
    print("Substraction is:",s)
def multi(x,y):
    s=x*y
    print("Multiplication is:",s)
def div(x,y):
    s=x/y
    print("Division is:",s)
def expo(x,y):
    s=x**y
    print("Exponential is",s)
def factorial(x):
    fac=1
    for i in range(1,x+1):
        fac=fac*i
    print("Factorial is:",fac)
x=int(input("Enter x:"))
y=int(input("Enter y:"))
i=input("Enter the operation")
if(i=="+"):
    add(x,y)
elif(i=="-"):
    sub(x,y)
elif(i=="*"):
    multi(x,y)
elif(i=="/"):
    div(x,y)
elif (i=="**"):
    expo(x,y)
elif(i=="!"):
    factorial(x)