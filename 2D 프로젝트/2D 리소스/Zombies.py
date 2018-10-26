from pico2d import *
import random



class Zombie:
    WALK, ATTACK ,DIE ,END ,IDLE = 1, 2, 3 ,4 , 5
    start_frame = 0
    order = 0
    def __init__(self):
        self.x, self.y = random.randint(1800 , 1900) , random.randint(100 , 450)
        self.frame = random.randint(0, 11)
        self.total_frame = random.randint(0,10)
        self.state = self.IDLE

        self.Basic_Zombies = load_image('Tutorial/basic_zombie_idle.png')
        self.Basic_Zombies_Walk = load_image('Tutorial/Tutorial_Zombie_walk.png')

    def update(self):
        if(self.state == self.IDLE):

            self.frame = (self.frame) % 10
            if (self.total_frame >= 6):
                self.frame = self.frame + 1
                self.total_frame = 0
            self.total_frame = self.total_frame + 1
            # 좀비가 가만이 있는 상태일때
        if(self.state == self.WALK):
            self.frame = (self.frame) % 17
            if (self.total_frame >= 6):
                self.frame = self.frame + 1
                self.total_frame = 0
            self.total_frame = self.total_frame + 1






    def draw(self , order):
        if(self.state == self.IDLE):
            if (order < 2):
                self.start_frame = self.start_frame + 3
            if (order >= 3):
                self.start_frame = self.start_frame - 4

            self.Basic_Zombies.clip_draw(self.frame * 166, 0, 81, 120, self.x - self.start_frame, self.y)
        if(self.state == self.WALK):
            self.Basic_Zombies_Walk.clip_draw(self.frame * 166  - 3, 0 , 90 , 128 , self.x  , self.y)

    def Walk(self):
        self.y = 300
        self.state = self.WALK
    def Attack(self):
        pass


