# Area of the Triangle using Heron's Formula 
from math import sqrt

a,b,c = (input("Enther the length of the sides of the triangle: \n")).split()
a = float(a)
b = float(b)
c = float(c)

p = (a+b+c)/2
S = sqrt(p*(p-a)*(p-b)*(p-c))
S = round(S, 2)

# print("The area of the triangle is {0}".format(S))
# print(f"The area of the triangle is {S}")