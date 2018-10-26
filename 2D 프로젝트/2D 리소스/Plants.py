from pico2d import *
import random
import time
font = None

class plant:
    ATTACK,IDLE = 2 , 1

    def __init__(self):
        self.x , self.y = 0, 0
        self.frame = random.randint(0 , 12 )
        self.basic_plants_image = load_image('Tutorial/Baisc_plants.png')

        self.frame = random.randint(0, 11)
        self.total_frame = random.randint(0, 4)
        self.state = self.IDLE
    def update(self):
        if (self.state == self.IDLE):

            self.frame = (self.frame) % 12
            if (self.total_frame >= 6):
                self.frame = self.frame + 1
                self.total_frame = 0
            self.total_frame = self.total_frame + 1

    def draw_card(self , card_select , mouse_x , mouse_y): # 카드를 그려줌
        if(card_select == 1):
            self.basic_plants_image.clip_draw( 0, 0, 71, 80, mouse_x + 10 , 600 - mouse_y)

    def draw(self): # 식물을 그려준다

        self.basic_plants_image.clip_draw(self.frame * 70 ,  0 , 70 , 90 , self.x , self.y , )
    def attack(self):
        pass
