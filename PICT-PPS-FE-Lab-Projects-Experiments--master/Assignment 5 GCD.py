'''
Problem Statement:Write a program in Python to accept two numbers from user and compute
smallest divisor and Greatest Common Divisor of these two numbers.
'''
 '''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
if(x>0 and y>0):
    for i in range(min(x, y), 1, -1):
        if x % i == 0:
            if y % i == 0:
                print(i)
                break
else:
    print("Please enter positive numbers")
'''


x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
l=[]
for i in range(2,min(x,y)+1):
    if x%i==0 and y%i==0:
        l.append(i)
print(l)
print("GCD:",max(l))
print("SCD:",min(l))
