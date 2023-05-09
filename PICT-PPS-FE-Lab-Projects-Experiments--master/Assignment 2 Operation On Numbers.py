'''
Write a Program in Python to accept N numbers from user. Compute
and display maximum in list, minimum in list, sum and average of
numbers.
'''
n=int(input("Enter length of list:"))
l=[]
for i in range(n):
    e=int(input("Enter the element number:".format(i+1)))
    l.append(e)
avg=sum(l)/n
print("The list is :",l)
print("The Maximum in the list is:",max(l))
print("The Minimum in the list is:",min(l))
print("The Sum of Elements in the list is:",sum(l))
print("The Average of Numbers in the list is:",avg)




