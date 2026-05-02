import math
a= float(input('enter the value of first side'))
b= float(input('enter the the value of second side'))
c= float(input('enter the value of third side'))
s= (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of the triangle=",area)
