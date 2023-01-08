class C:
    @staticmethod
    def m1(n):
        text = str(n)
        new_text = ""
        for x in text:
            x = int(x)
            if x % 2 == 0:
                new_text += str(x)
        new_text = int(new_text)
        return new_text
    
    @staticmethod
    def m2(n):
        text = str(n)
        for x in range(len(text)-1):
            if text[x] > text[x+1]:
                return False
        return True

    @staticmethod
    def m3(n):
        text = str(n)
        new_text = ""
        for x in range(10):
            if str(x) not in text:
                new_text += str(x)
        return new_text



print(C.m3(23557))
print(C.m3(12340))
# C.m3(23557) = "014689"
# C.m3(12340) = "56789"

print(C.m1(4231564))
print(C.m1(79381))
# C.m1(4231564)  4264
# C.m1(79381)  8

print(C.m2(125579))
print(C.m2(4557879))
# C.m2(125579)  True
# C.m2(4557879)  False


