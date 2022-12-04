file = open("numbers3.txt", "w", encoding="UTF-8")

for i in range(1,11):
    a=str(i**2)
    b=str(i**3)
    file.write(str(i) + "," + a + "," + b + "\n")


    # if i != 10:              #wtedy nie tworzy nowej lini na koncu
    #     file.write("\n")     # w 6 liniejce nalezy usunac dodawanie nowej lini    
                               
file.close()