class Tv:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels_list = []
        # self.x = ""
        # self.y = ""
        
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no


    def set_channels(self, channels_list):
        self.channels_list.append(channels_list)
        # self.x = channels_list
        # self.y = self.x.split(", ")

    
    def show_channels(self):
        channels = ", ".join(self.channels_list)
        print("Available channels: " + channels) 
        

    def show_status(self):
        if self.is_on:
            if self.channel_no <= len(self.channels_list):
                print("TV is on, channel " + str(self.channel_no) + " (" + self.channels_list[self.channel_no - 1] + ")")
            else: 
                print("TV is on, channel " + str(self.channel_no))
        else: 
            print("TV is off")


tv = Tv()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.show_channels()

# tv.set_channels("TVP1, TVP2, Polsat, TVN, Filmbox, Discovery")
tv.set_channels("TVP1")
tv.set_channels("TVP2")
tv.set_channels("Polsat")
tv.set_channels("TVN")
tv.set_channels("Filmbox")
tv.set_channels("discovery")
tv.set_channels("Eska TV")
tv.set_channels("TVN7")

tv.set_channel(9)

tv.show_channels()
tv.show_status()
tv.turn_off()

# print(tv.channels_list)
# print(tv.y)
# print(tv.x)