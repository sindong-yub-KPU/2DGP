from pico2d import *
import random
import time


class Zombie:
    WALK, ATTACK ,DIE ,END = 1, 2, 3 ,4
    Basic_Zombies = None
    start_frame = 0
    order = 0
    def __init__(self):
        self.x, self.y = random.randint(1800 , 1900) , random.randint(100 , 450)
        self.frame =random.randint(0, 11)
        self.total_frame = 0.0
        if Zombie.Basic_Zombies == None:
            Zombie.Basic_Zombies = load_image('Tutorial/basic_zombie_idle.png')


    def update(self):
        self.frame = (self.frame) % 10
        if(self.total_frame >= 6):
            self.frame = self.frame + 1
            self.total_frame = 0
        self.total_frame = self.total_frame + 1




    def draw(self , order):
        if(order  < 2):
            self.start_frame = self.start_frame + 2.2
        if(order >= 3):
            self.start_frame = self.start_frame - 4

        self.Basic_Zombies.clip_draw(self.frame * 166  ,0 , 81 ,120 , self.x - self.start_frame , self.y)
        print(self.start_frame)
