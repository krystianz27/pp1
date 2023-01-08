def f(name, surname):
    import csv
    
    file = open("data.csv", encoding="utf-8")
    content = csv.reader(file)

    for line in content:
        if name in line:
            if surname in line:
                a =int(line[9])
                b = int(line[11])
                file.close()
                if b >= a/2:
                    return True
                else:
                    return False
