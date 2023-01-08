class C:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        text =""
        total = 0
        for x in self.array:
            text += str(x) + "+"
        
        for x in self.array:
            total += x
        total = str(total)

        text = text[:len(text)-1]
        text += "=" + total

        return text



k = C([5,12])
print(k)

l = C([6,0,15])
print(l)

# C([5,12])  "5+12=17"
# C([6,0,15])  "6+0+15=21"
