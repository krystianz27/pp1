class Tv:
    def __init__(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on:
            print("TV is on")
        else: 
            print("TV is off")


tv = Tv()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.turn_off()
tv.show_status()


# Then try using the TV set in the program:
# a.	Create TV set
# b.	Show TV status
# c.	Turn TV on
# d.	Show TV status
# e.	Turn TV off
# f.	Show TV status
