'''
Problem Statement:Write a program in Python to accept from user the number of Fibonacci
numbers to be generated and print the Fibonacci series.
'''
n1,n2=0,1
n=int(input("Enter the Nth term for the series:"))
if(n<0):
    print("Please enter a positive number...")
elif(n==1):
    print(n1)
else:
    count=0
    while(count<n):
        temp=n1+n2
        print(n1,end=" ")
        n1=n2
        n2=temp
        count+=1