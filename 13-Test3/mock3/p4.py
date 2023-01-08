def f(d):
    dic = {}
    for x in d:
        dic[x[0]] = dic.get(x[0], 0) + 1
        
    car1 = []
    for x, y in dic.items():
        if y % 2 == 1:
            car1.append(x)
    car1.sort()

    return car1


        




cars = [["KR234","in"], ["BA123","in"], ["GX444","in"], ["KR234","out"], ["BA111","in"], ["BA123","out"], ["KR234","in"]]


print(f(cars))


# f(cars)  ["BA111","GX444","KR234"]

