from pico2d import *
import random
import time


class Zombies:
    WALK, ATTACK ,DIE ,END = 1, 2, 3 ,4
    Basic_Zombies = None

    def __init__(self):
        self.x, self.y = random.randint(600 , 700) , random.randint(100 , 500)
        self.frame =random.randint(0, 11)
        self.total_frame = 0.0
        if Zombies.Basic_Zombies == None:
            Zombies.Basic_Zombies = load_image('basic_zombie_idle')


    def update(self):
        if(self.total_frame == 40):
            self.frame = self.frame + 1
        self.frame = (self.frame) % 11

        self.total_frame = self.total_frame +1 % 40 + 1

    def draw(self):
        pass