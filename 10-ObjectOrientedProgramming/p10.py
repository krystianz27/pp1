class Tv:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def show_status(self):
        if self.is_on:
            print("TV is on, channel " + str(self.channel_no))
        else: 
            print("TV is off")


tv = Tv()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.turn_off()
tv.show_status()



# a.	Create a TV set
# b.	Show TV status
# c.	Turn TV on
# d.	Show TV status
# e.	Change TV channel to 5
# f.	Show TV status
# g.	Turn TV off
# h.	Show TV status 
