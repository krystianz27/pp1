def  f(n1, n2, n3):
    a = int(n1)
    b = int(n2)
    c = int(n3)
    if a+b == 10:
        return True
    elif a+c==10:
        return True
    elif b+c == 10:
        return True
    else:
        return False
