array1 = [5,4,3,2,6,5]
array2 = []

# tekst = ""

def f(array): 
    for x in array:
        array2.append(str(x))

    tekst = ",".join(array2)
    return tekst                       #1 sposob


    # tekst = ""
    # for y in array:
    #     tekst += f"{str(y)},"
    # z = tekst[0:len(tekst)-1]
    # return z                             #sposob

print(f(array1))
print(array2)

# print(f(array1))