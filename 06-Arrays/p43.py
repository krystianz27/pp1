def identity_matrix(n):
    array1 = [[0 for x in range(n)] for x in range(n)]
    i = 0

    while i < n:
        array1[i][i] = 1
        i += 1
    # return array1

    for x in array1:
        for y in x:
            print(y, end=" ")
        print()
    print()


identity_matrix(3)
identity_matrix(5)
identity_matrix(8)


# matrix = identity_matrix(3)      #lub usuwamy petle for z funkcji i przypisujemy do matrix wywolanie funkcji
# print(matrix)
# for x in matrix:
#     for y in x:
#         print(y, end=" ")
#     print()

