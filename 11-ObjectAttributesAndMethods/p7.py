class Student():

    university = "UEK"
    id = 100000
    
    def __init__(self, name, surname, field):
        self.name = name
        self.surname = surname
        self.field = field
        self.id = Student.id
        Student.id +=1
    
    def __str__(self):
        return f"{self.name} {self.surname} ({self.id}) {self.field} {Student.university}"
    

student1 = Student("Anna", "Maj", "IT")
print(student1)

student2 = Student("Jan", "Kowalski", "IT")
print(student2)

student2 = Student("Kacper", "Nowak", "IT")
print(student2)