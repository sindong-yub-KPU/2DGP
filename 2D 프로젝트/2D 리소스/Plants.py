from pico2d import *
import random
import time
font = None

class plants:


    def __init__(self ,mouse_x,mouse_y):
        self.x , self.y = int(mouse_x) , int(mouse_y)
        self.frame = random.randint()
        self.basic_plants_image  ('Baisc_plants.png')
        self.total_frame, self.frame = 0.0 , 0.0


