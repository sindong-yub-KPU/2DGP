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
    DIE , HIT, ATTACK,IDLE  =4, 3,2 , 1
    basic_plants_image = None
    def __init__(self , x, y , line_ ,sit_):
        self.x , self.y = x, y
        self.y = (line_+ 1) * 100 - 10
        if(self.basic_plants_image == None):
            self.basic_plants_image = load_image('Tutorial/Baisc_plants.png')

        self.Bullet_Count = 0
        self.frame = random.randint(0, 11)
        self.total_frame = random.randint(0, 4)
        self.state = self.IDLE
        self.Line = line_  # 맨위에부터 0 1 2 3 4  개의 라인
        self.state_time = 0
        self.world_time =0
        self.hp = 3
        self.sitting = sit_  # 자리
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME * game_framework.frame_time) % 12
        if(self.state == 3): #식물이 지금 맞고 있다.
            self.world_time = get_time()
            if(self.world_time - self.state_time  > 2):
                self.state_time = get_time()
                self.hp -= 1 #식물의 피 달음
                if (self.hp <= 0):
                    self.state = self.DIE

        if(self.state == 4):
            game_world.remove_object(self)



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

 # 꽃






class Flower:
    DIE, HIT, Sun, IDLE = 4, 3, 2, 1
    basic_flower_image = None
    def __init__(self , x, y , line_,sit):
        self.x = x
        self.y = (line_ + 1) * 100 - 10  # 식물 라인 설정
        if(self.basic_flower_image == None):
            self.basic_flower_image = load_image('Stage1/Flower.png')
        self.Bullet_Count = 0
        self.frame = random.randint(0, 11)
        self.total_frame = random.randint(0, 4)
        self.state = self.IDLE
        self.Line = line_  # 맨위에부터 0 1 2 3 4  개의 라인
        self.state_time = 0
        self.Sun_time = get_time()
        self.world_time =0
        self.hp = 3
        self.sun_time =0
        self.sitting = sit  # 자리
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME * game_framework.frame_time) % 17
        if (self.state == self.HIT):  # 식물이 지금 맞고 있다.
            self.world_time = get_time()
            if (self.world_time - self.state_time > 2):
                self.state_time = get_time()
                self.hp -= 1  # 식물의 피 달음
                if (self.hp <= 0):
                    self.state = self.DIE


        if (self.state == 4):
            game_world.remove_object(self)

    def draw_card(self , card_select , mouse_x , mouse_y): # 카드를 그려줌 꽃
        if(card_select == 2):
            self.basic_flower_image.clip_draw( 0, 0, 84, 80, mouse_x + 10 , 600 - mouse_y)

    def draw(self): # 식물을 그려준다

        self.basic_flower_image.clip_draw(int(self.frame) * 103 -2 ,  0 , 70 , 90 , self.x , self.y , )
        self.draw_bb()

    def get_bb(self):
        return self.x - 42, self.y - 15, self.x + 42, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class walnut:
    DIE, HIT, Sun, IDLE = 4, 3, 2, 1
    basic_walnut_image = None

    def __init__(self, x, y, line_ , sit):
        self.x = x
        self.y = (line_ + 1) * 100 - 10  # 식물 라인 설정
        if (self.basic_walnut_image == None):
            self.basic_walnut_image = load_image('Stageleveltwo/Potato_state_good.png')

        self.Bullet_Count = 0
        self.frame = random.randint(0, 11)
        self.total_frame = random.randint(0, 4)
        self.state = self.IDLE
        self.Line = line_  # 맨위에부터 0 1 2 3 4  개의 라인
        self.state_time = 0
        self.Sun_time = get_time()
        self.world_time = 0
        self.hp = 5
        self.sun_time = 0
        self.sitting = sit #자리
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME * game_framework.frame_time) % 14
        if (self.state == self.HIT):  # 식물이 지금 맞고 있다.
            self.world_time = get_time()
            if (self.world_time - self.state_time > 2):
                self.state_time = get_time()
                self.hp -= 1  # 식물의 피 달음
                if (self.hp <= 0):
                    self.state = self.DIE

        if (self.state == 4):
            game_world.remove_object(self)

    def draw_card(self, card_select, mouse_x, mouse_y):  # 카드를 그려줌 꽃
        if (card_select == 3):
            self.basic_walnut_image.clip_draw(0, 0, 84, 80, mouse_x + 10, 600 - mouse_y)

    def draw(self):  # 식물을 그려준다

        self.basic_walnut_image.clip_draw(int(self.frame) * 95 - 2, 0, 70, 90, self.x, self.y, )
        self.draw_bb()

    def get_bb(self):
        return self.x - 42, self.y - 15, self.x + 42, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class cherryboom:
    pass