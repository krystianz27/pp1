class C:
    def __init__(self, value):
        self.value = value 

    def m1(self):
        print(self.value)

    def m2(self):
        self.value += 1

    def m3(self):
        self.value -= 1

    def m4(self, n):
        self.n = n
        self.value += self.n
    
c = C(5)
c.m1()
c.m2()
c.m1()
c.m4(-8)
c.m1()
c.m3()
c.m1()
c.m4(10)
c.m1()
    




# m1() - returns the counter value
# m2() - increases the counter value by 1
# m3() - decreases the counter value by 1
# m4(n) - increases the counter value by n
# Example:
# c=C(5)
# c.m1()  5
# c.m2()
# c.m1()  6
# c.m4(-8)
# c.m1()  -2
# c.m3()
# c.m1()  -3
# c.m4(10)
# c.m1()  7
