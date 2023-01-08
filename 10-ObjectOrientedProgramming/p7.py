class University:
    def __init__(self):
        self.name = 'CUE'    

    def print_name(self):  
        print(self.name)

    def set_name(self, name):
     self.name = name


obj = University()
obj.print_name()
obj.set_name("UEK")
obj.print_name()

