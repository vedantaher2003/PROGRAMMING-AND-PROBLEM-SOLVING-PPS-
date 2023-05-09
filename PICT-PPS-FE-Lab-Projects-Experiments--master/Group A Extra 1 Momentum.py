'''
Write a Program in Python to accept an object mass in kilograms and velocity in
meters per second and display its momentum. Momentum is calculated as e=mc2
where m is the mass of the object and c is its velocity.
'''
m=float(input('Enter mass of object in kilograms:'))
c=float(input('Enter veloity in metres per second:'))
e=m*c*c
print('Momentum Of Object is:'+str(e))