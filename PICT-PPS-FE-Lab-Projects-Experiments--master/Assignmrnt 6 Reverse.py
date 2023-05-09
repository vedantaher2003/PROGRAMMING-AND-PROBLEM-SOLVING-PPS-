'''
Problem Statement:Write a program in Python to accept a number from user and print
digits of number in a reverse order.
'''
n=int(input("Enter a number:"))
c2=''
while(n>0):
    a=n%10
    n=n//10
    c2=str(c2)+str(a)
print(c2)
if(n<=0):
    print("Please enter a positive number")