'''
Write a Program in Python to accept student‟s five courses marks and compute his/her
result. Student is passing if he/she scores marks equal to and above 40 in each course.
If student scores aggregate greater than 75%, then the grade is distinction. If
aggregate is 60>= and <75 then the grade if first division. If aggregate is 50>= and
<60, then the grade is second division. If aggregate is 40>= and <50, then the grade is
third division.
'''
l=[]
for i in range(0,5):
    e=float(input("Enter the marks of subject {}:".format(i+1)))
    l.append(e)
print("Your Mark list is:",l)
if l[i]>=40:
    print("You have passed in each Subject!")
else:
    print("You have Failed...")
print("Your total marks are:",sum(l))
avg=sum(l)/len(l)
print("Average is:",avg)
if avg>=75:
    print("Distinction")
elif avg<75 and avg>=60:
    print("First Division")
elif avg<60 and avg>=50:
    print("Second Division")
elif avg<50 and avg>=40:
    print("Third Division")

