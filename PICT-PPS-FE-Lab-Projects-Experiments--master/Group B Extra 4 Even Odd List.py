'''
Problem Statement:Write a Program in Python to accept list of N integers and
partition list into two sub lists even and odd numbers.
'''
l=[]
even=[]
odd=[]
N=int(input("Enter number of elements in list:"))
for i in range(1,N+1):
    a=int(input("Enter element {} in list:".format(i)))
    l.append(a)
print(l)
for j in l:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print(even)
print(odd)