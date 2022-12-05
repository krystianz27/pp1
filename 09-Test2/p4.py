def f(dictionary,x,y):
    sum = 0
    for m in dictionary.values():
        for n in m:
            if n >= x and n <= y:
                sum +=n
                # print(n)
    return sum



# f({"arr1":[5,7]}, 1, 10)
# f({"arr1":[5,7], "arr2":[4,5,6]}, 1, 10)


# print(f({"arr1":[5,7], "arr2":[4,5,6]}, 5, 6))

# f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6) => 16