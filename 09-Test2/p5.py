def f(first_letter, last_letter):
    file = open("test.txt", encoding="UTF-8")
    content = file.read()
    file.close()

    import re
    pattern = r"\b" + first_letter +r".+" + last_letter +r"\b"
    words = re.findall(pattern, content)
    # words = re.findall(r"\b" + first_letter + r"\w*" + last_letter + r"\b", content)
    # words = re.findall(rf"\b{first_letter}\S*{last_letter}\b", content)
    return len(words)

print(f("w", "d"))