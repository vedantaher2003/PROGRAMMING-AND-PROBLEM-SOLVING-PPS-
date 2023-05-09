'''
Problem Statement:Write a Program in Python to input binary number from user and
convert it into decimal number.
'''
temp=0
count=0
b=int(input("Enter a binary Number:"))
while(b>0):
    a=b%10
    b=b//10
    if(a==1):
        temp=temp+(2**count)*a
    count+=1
print(temp)
if(a!=0 and a!=1):
        print("Please enter a binary number only...")

