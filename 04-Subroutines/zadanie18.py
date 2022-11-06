def sum(n):
    n = str(n)
    total = 0
    for x in n:
        x = int(x)
        total += x
    return total

print(sum(7182))
