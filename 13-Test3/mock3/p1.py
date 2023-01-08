def f(n):
    n = int(n)
    text = ""
    if n <= 0:
        return text
    else:
        for i in range(1, n+1):
            text += "/"
            if i % 5 == 0:
                text += "-"
        return text
            


# print(f(-3))



