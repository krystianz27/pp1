def f1(t):
    import re

    names = re.findall(r"[A-Z][a-z]+", t)
    ages = re.findall(r"\d+", t)

    result = {}
    for i in range(len(names)):
        result[names[i]] = int(ages[i])

    result_sorted = dict(sorted(result.items(), key=lambda x: x[0] ))
    return result_sorted

def f2(d):
    return sum(i for i in d.values())




print(f1("Mark is 24 and Ann is 27"))
print(f2(f1("Mark is 24 and Ann is 27")))
# print()
# print(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))
# print(f2(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))) 



