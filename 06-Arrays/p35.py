from random import randint
array1 = [randint(0,10) for k in range(10)]

def rand_elem(array):
    return array[randint(0, len(array)-1)] 

print(rand_elem(array1))
print(rand_elem(array1))
print(rand_elem(array1))
print(rand_elem(array1))