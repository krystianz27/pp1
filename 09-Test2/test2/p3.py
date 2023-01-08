import numbers


def f(array2D):
    number = []
    for x in array2D:
        sum = 0
        for y in x:
            sum +=y
        number.append(sum)

    index = number.index(min(number))

    return index
        
