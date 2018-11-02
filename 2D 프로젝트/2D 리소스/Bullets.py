from pico2d import *
import time
import game_framework
import Plants
PIXEL_PER_METER = (10.0 / 0.3)
#이동거리가 10pixsel 에 30cm간다는 뜻 임의로 정함
Bullet_SPEED_KMPH = 5.0
# 10.0 속도
#  10.0 속도 =  km / hour 킬로미터 거리 / 시간
Bullet_SPEED_MPM = (Bullet_SPEED_KMPH * 1000.0 / 60 )
# 경과시간을 분으로 바꿈 (속도 * 1000 / 60)
Bullet_SPEED_MPS = (Bullet_SPEED_MPM / 60.0)
# 경과시간을 초로 바꿈
Bullet_SPEED_PPS = (Bullet_SPEED_MPS * PIXEL_PER_METER) # 픽셀 퍼 세크 미터 퍼세크에다가 픽셀퍼 미터를 곱한것
class Bullet:
    basic_plants_bullet = None
    def __init__(self , x , y):
        if (self.basic_plants_bullet == None):
            self.basic_plants_bullet = load_image('Tutorial/Tutorial_bullet.png')
        self.x = x
        self.y = y
        self.velocity = Bullet_SPEED_PPS
    def draw(self):
        pass
    def update(self):
        self.x += self.velocity * game_framework.frame_time
        pass
