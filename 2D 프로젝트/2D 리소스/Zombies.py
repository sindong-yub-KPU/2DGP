from pico2d import *
import game_framework
import random

TIME_PER_ACTION = 2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION #1초에 할 액션수 2개
FRAMES_PER_ACTION = 11 # 8개의 프레임

class Zombie:
    WALK, ATTACK ,DIE ,END ,IDLE = 1, 2, 3 ,4 , 5
    start_frame = 0
    order = 0
    def __init__(self):
        self.x, self.y = random.randint(1900 , 2000) , random.randint(100 , 450)
        self.frame = random.randint(0, 11)

        self.state = self.IDLE

        self.Basic_Zombies = load_image('Tutorial/basic_zombie_idle.png')
        self.Basic_Zombies_Walk = load_image('Tutorial/Tutorial_Zombie_walk.png')

    def update(self):
        if(self.state == self.IDLE):
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time ) % 11


            # 좀비가 가만이 있는 상태일때
        if(self.state == self.WALK):
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 17








    def draw(self):
        if(self.state == self.IDLE):


            self.Basic_Zombies.clip_draw(int(self.frame) * 166, 0, 81, 120, self.x , self.y)
        if(self.state == self.WALK):
            self.Basic_Zombies_Walk.clip_draw(int(self.frame) * 166  - 3, 0 , 90 , 128 , self.x  , self.y)

    def Walk(self):
        self.y = 300
        self.state = self.WALK
    def Attack(self):
        pass


