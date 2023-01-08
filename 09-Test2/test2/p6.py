def f(name, surname):
    import json
    
    file = open("data.json", encoding="utf-8")
    content = json.load(file)

    for line in content:
        if line["name"] == name:
            if line["surname"] == surname:
                lang = line["languages"]
                lang2 =",".join(lang)
    
    file.close()
    return lang2
    