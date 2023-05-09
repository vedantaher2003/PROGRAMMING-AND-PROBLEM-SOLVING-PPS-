#Assignment 7
'''
Write a python program that accepts a string from user and perform
following string operations-
a) Calculate length of string
b) String reversal
c) Equality check of two strings
d) Check palindrome
e) Check substring
'''
s=(input("Enter the String:"))
print(" 1.)Length Of the String \n 2.)String Reverse \n 3.)String Comparison \n 4.)Check Palindrome \n 5.)Check Sub String \n")
c=int(input("Please enter your choice:"))
if c==1:
    counter=0
    for i in s:
        counter+=1
    print(counter)
elif c==2:
    reverse=""
    for i in range(len(s)):
        reverse=s[i]+reverse
    print(reverse)
elif c==3:
    str=input("Enter the other string for comparison:")
    if s==str:
        print("Both the strings are Equal")
    else:
        print("The strings are Unequal")
elif c==4:
    reverse = ""
    for i in range(len(s)):
        reverse = s[i] + reverse
    if s==reverse:
        print("It is a Palindrome!")
    else:
        print("It is not a Palindrome.")
elif c==5:
    substring=input("Enter the Sub-string")
    if substring in s:
        print("Substring Present")
    else:
        print("Substring Not Present")
