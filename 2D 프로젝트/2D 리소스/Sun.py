from pico2d import *
import game_framework
import game_world
import random
import tutorial
import math

PIXEL_PER_METER = (10.0 / 0.3)
#이동거리가 10pixsel 에 30cm간다는 뜻 임의로 정함
CHANGE_SPEED_KMPH = 5.0
# 10.0 속도
#  10.0 속도 =  km / hour 킬로미터 거리 / 시간
CHANGE_SPEED_MPM = (CHANGE_SPEED_KMPH * 1000.0 / 60 )
# 경과시간을 분으로 바꿈 (속도 * 1000 / 60)
CHANGE_SPEED_MPS = (CHANGE_SPEED_MPM / 60.0)
# 경과시간을 초로 바꿈
CHANGE_SPEED_PPS = (CHANGE_SPEED_MPS * PIXEL_PER_METER) # 픽셀 퍼 세크 미터 퍼세크에다가 픽셀퍼 미터를 곱한것

TIME_PER_ACTION = 1.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION #1초에 할 액션수 2개
FRAMES_PER_ACTION = 21 # 8개의 프레임

class Sun_shine:
    Sun_image = None
    def __init__(self):
        self.x , self.y = random.randint(300 , 1000) , 700 # Sun 값 정의
        self.limit_y = random.randint(50 , 400 ) # y 값 리미트
        self.frame = random.randint(0,21)
        self.velocity = CHANGE_SPEED_PPS
        self.click = 0
        self.plus_y = 0
        self.plus_x = 0
        self.plus_time = 0
        self.index =0 # 지울 자원의 인덱스
        if(Sun_shine.Sun_image == None):
            Sun_shine.Sun_image = load_image('Tutorial/Sun.png')
    def draw(self):
        self.Sun_image.clip_draw(int(self.frame) * 93, 0, 78, 79, self.x, int(self.y))


    def update(self):

        if(self.click == 0):
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 20


        if(self.limit_y < self.y and self.click == 0):
            self.y -=  self.velocity * game_framework.frame_time
        if(self.click == 1):
            t = self.plus_time / 100
            self.x = (1 - t) * self.plus_x + t *  50
            self.y = (1 - t) * self.plus_y + t *  550




            self.plus_time += 1
            if(self.plus_time == 100):

                self.click = 2
        if (self.click == 2):

            game_world.remove_object(self)


        pass
    def go_Sun(self):
        pass
    def delete_Sun(self):

        pass
