array1  = []
def create_2d_arr(x,y):
    for k in range(x):
        array1.append([0 for m in range(y)])
    return array1

print(create_2d_arr(3,5))