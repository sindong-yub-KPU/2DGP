from pico2d import *
import random
import time
import game_framework
import game_world
from Bullets import Bullet
font = None
TIME_PER_ACTION = 1.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION #1초에 할 액션수 2개
FRAMES_PER_ACTION_IDLE = 11 # 8개의 프레임
FRAMES_PER_ACTION_WALK = 17

class plant:
    ATTACK,IDLE = 2 , 1

    def __init__(self , x, y , line_):
        self.x , self.y = x, y

        self.basic_plants_image = load_image('Tutorial/Baisc_plants.png')

        self.Bullet_Count = 0
        self.frame = random.randint(0, 11)
        self.total_frame = random.randint(0, 4)
        self.state = self.IDLE
        self.Line = line_ ; # 맨위에부터 0 1 2 3 4  개의 라인
        self.state_time = get_time()


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME * game_framework.frame_time) % 12



    def draw_card(self , card_select , mouse_x , mouse_y): # 카드를 그려줌
        if(card_select == 1):
            self.basic_plants_image.clip_draw( 0, 0, 84, 80, mouse_x + 10 , 600 - mouse_y)

    def draw(self): # 식물을 그려준다

        self.basic_plants_image.clip_draw(int(self.frame) * 86 -2 ,  0 , 70 , 90 , self.x , self.y , )
        self.draw_bb()
    def attack(self):
        pass
    def get_bb(self):
        return self.x - 42, self.y - 15, self.x + 42, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())