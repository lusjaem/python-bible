import random

#new class of object

class Pound:
    #constructor
    def __init__(self, name="Coin", rare=False): #self refers to object instance
        self.rare = rare
        if self.rare: #if self.rare == True:
            self.value = 1.25
        else:
            self.value = 1.00
        #states definitions
        self.name = name
        self.colour = "gold"
        self.num_edges = 1 #circle
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True

    def rust(self):
        self.colour = "greenish"
        
    def clean(self):
        self.colour = "gold"

    def flip(self):
        head_options = [True, False]
        choice = random.choice(head_options)
        self.heads = choice

    #destructor
    def __del__(self):
        print("{} spent!".format(self.name))

#class asignment

coin1 = Pound(name="Coin1", rare=True)
coin2 = Pound(name="Coin2") 

print("{} value is: {}".format(coin1.name,coin1.value))
print("{} value is: {}".format(coin2.name,coin2.value))
coin1.rust()
print("{} colour is: {}".format(coin1.name,coin1.colour))
coin1.clean()
print("{} colour is: {}".format(coin1.name,coin1.colour))
print("{} is flipped up on heads: {}".format(coin1.name,coin1.heads))
coin1.flip()
print("{} is flipped up on heads: {}".format(coin1.name,coin1.heads))
del coin2

