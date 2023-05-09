'''
Problem Statement:Write a Program in Python to check whether input number is
Armstrong number or not. An Armstrong number is an integer with three digits such that the
sum of the cubes of its digits is equal to the number itself. Ex. 371.
'''
n=int(input("Enter a Number:"))
a=0
while(n>0):
    temp=n%10
    n=n//10
    a=a+temp**3
    a1=a
print(a1)
if(a1==n):
    print("Armstrong")
else:
    print("Not Armstrong")