class C:
    def __init__(self, dic):
        self.dic = dic

    def m(self, n):
        from statistics import mean
        self.n = n
        names = []
        for x, y in self.dic.items():
            # print(x, mean(y))
            average = mean(y)
            if average >= self.n:
                names.append(x)
        names.sort()
        text = ",".join(names)
        return text
        





s = C( {"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5] } )

print(s.m(4))
print(s.m(3))
print(s.m(5))

# s.m(4)  "Barbara,Peter"
# s.m(3)  "Barbara,Harry,Peter"
# s.m(5)  ""
