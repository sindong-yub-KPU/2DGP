from pico2d import *
import random
import time
font = None

class plant:


    def __init__(self):
        self.x , self.y = 0, 0
        self.frame = random.randint(0 , 12 )
        self.basic_plants_image = load_image('Tutorial/Baisc_plants.png')
        self.frame = random.randint(0, 11)
        self.total_frame = random.randint(0, 10)


    def update(self):
        if (self.state == self.IDLE):

            self.frame = (self.frame) % 12
            if (self.total_frame >= 6):
                self.frame = self.frame + 1
                self.total_frame = 0
            self.total_frame = self.total_frame + 1

    def draw_card(self , card_select , mouse_x , mouse_y):
        if(card_select == 1):
            self.basic_plants_image.clip_draw( 0, 0, 71, 80, mouse_x + 10 , 600 - mouse_y)

    def draw(self):
        print(self.x)
        self.basic_plants_image.clip_draw(self.frame * 70 ,  0 , 80 , 120 , self.x , self.y )