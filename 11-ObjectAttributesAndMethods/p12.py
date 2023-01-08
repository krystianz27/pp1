class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self, second):
        if self.x == second.x and self.y == second.y:
            return True
        else:
            return False

    def distance(self, second):
        import math
        if self == second:
            return "Distance is 0"
        else:
            distance = math.sqrt((second.x - self.x)**2 + (second.y - self.y)**2)
            return "Distance is " + str(distance)


p3 = Point(5,7)
p4 = Point(15,7)

print(p3.distance(p4))
