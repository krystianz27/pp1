def power(x, n):
    if x == 0:
        return 0
    if x == 1:
        return x
    if n == 0:
        return 1

    while n > 0:
        return x*power(x, n-1)


# print(power(5,3))