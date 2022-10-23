# def prime(x):
#     if x <= 1:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True

# # while True:
# x = int(input("x: "))
# print(prime(x))
# print(" ")



#Szukanie liczb pierwszych z przedziału [2, n]
def sito(n):
    temp = [1 for x in range(n+1)]
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if j%i == 0:
                temp[j] = 0

    primes = []
    for i in range(2, len(temp)):
        if temp[i] == 1:
            primes.append(i)

    return primes

print(sito(8))