# Ask user to input the length of the 3 sides of a triangle
x = float(input("enter the length of the first side"))
y = float(input("enter the length of the second side"))
z = float(input("enter the the length of third side"))
# if all the sides are equal print equilateral
if x == y== z:
    print("the triangle is an equilateral triangle")
elif x==y or y==z or x==z:
    print("the triangle is isosceles")
else:
    print("the triangle is a scalene triangle")