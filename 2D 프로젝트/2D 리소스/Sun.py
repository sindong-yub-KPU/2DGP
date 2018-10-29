from pico2d import *
import random

class Sun_shine:
    Sun_image = None
    def __init__(self):
        self.x , self.y = random.randint(30 , 1000) , 600 # Sun 값 정의
        self.limit_y = random.randint(50 , 400 ) # y 값 리미트
        self.frame = random.randint(0,21)
        self.total_frame = random.randint(0 , 6)
        if(Sun_shine.Sun_image == None):
            Sun_shine.Sun_image = load_image('Tutorial/Sun.png')
    def draw(self):
        self.Sun_image.clip_draw(self.frame * 93, 0, 78, 79, self.x, self.y)


    def update(self):
        self.frame = (self.frame) % 20
        if (self.total_frame >= 6):
            self.frame = self.frame + 1
            self.total_frame = 0
        self.total_frame = self.total_frame + 1
        if(self.limit_y < self.y):
            self.y = self.y - 1
        pass
    def go_Sun(self):
        pass
