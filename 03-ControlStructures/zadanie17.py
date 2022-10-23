x = int(input("Enter the x coordinate: "))
y = int(input("Enter the y coordinate: "))

if x == 0 and y == 0:
    print(f"The point P{x, y} is located in the position (0,0) of the coordinate system")

elif x == 0 and y!=0:
    print(f"The point P{x, y} is located on OY axis")

elif y == 0 and x !=0:
    print(f"The point P{x, y} is located on OX axis")

elif x > 0 and y > 0:
    print(f"The point P{x, y} is in the first quadrant of the coordinate system")

elif x > 0 and y < 0:
    print(f"The point P{x, y} is in the fourth quadrant of the coordinate system")

elif x < 0 and y > 0:
    print(f"The point P{x, y} is in the second quadrant of the coordinate system")

elif x < 0 and y < 0:
    print(f"The point P{x, y} is in the third quadrant of the coordinate system")

