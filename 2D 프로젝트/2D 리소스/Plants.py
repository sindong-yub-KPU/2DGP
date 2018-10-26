from pico2d import *
import random
import time
font = None

class plants:

    
    def __init__(self ,mouse_x,mouse_y):
        self.x , self.y = int(mouse_x) , int(mouse_y)
        self.frame = random.randint(0 , 12 )
        self.basic_plants_image  ('Baisc_plants.png')
        self.total_frame, self.frame = 0.0 , 0.0

    def update(self):
        if (self.state == self.IDLE):

            self.frame = (self.frame) % 10
            if (self.total_frame >= 6):
                self.frame = self.frame + 1
                self.total_frame = 0
            self.total_frame = self.total_frame + 1

