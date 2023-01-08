def f(dictionary, grade):
    grades = dictionary["subject"]["grades"]
    if grade in grades:
        return True
    else: return False
    
