x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
l=[]
for i in range(2,min(x,y)+1):
    if x%i==0 and y%i==0:
        l.append(i)
print(l)
print("GCD:",max(l))
print("SCD:",min(l))