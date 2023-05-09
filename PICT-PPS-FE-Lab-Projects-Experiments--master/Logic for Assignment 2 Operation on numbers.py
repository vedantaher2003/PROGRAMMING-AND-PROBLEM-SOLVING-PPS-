n=int(input("Enter length of list:"))
l=[]
for i in range(n):
    e=int(input("Enter the element number:".format(i+1)))
    l.append(e)
print("The list is :",l)
max=l[0]
min=[0]
sum=0
max=l[0]
min=l[0]
for i in range(n):
    sum=sum+l[i]
    if l[i]<min:
        min=l[i]
    if l[i]>max:
        max=l[i]
print('Sum:',sum)
print("Minimum:",min)
print("Maximun:",max)
avg=sum/n
print("Average:",avg)

