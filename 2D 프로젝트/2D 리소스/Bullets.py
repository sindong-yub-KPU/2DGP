from pico2d import *
import time
import game_framework
import game_world
import Plants


PIXEL_PER_METER = (20.0 / 0.3)
#이동거리가 10pixsel 에 30cm간다는 뜻 임의로 정함
Bullet_SPEED_KMPH = 10.0
# 10.0 속도
#  10.0 속도 =  km / hour 킬로미터 거리 / 시간
Bullet_SPEED_MPM = (Bullet_SPEED_KMPH * 1000.0 / 60 )
# 경과시간을 분으로 바꿈 (속도 * 1000 / 60)
Bullet_SPEED_MPS = (Bullet_SPEED_MPM / 60.0)
# 경과시간을 초로 바꿈
Bullet_SPEED_PPS = (Bullet_SPEED_MPS * PIXEL_PER_METER) # 픽셀 퍼 세크 미터 퍼세크에다가 픽셀퍼 미터를 곱한것



class Bullet:
    #state = 0 이면 날아감 1이면 애니메이션 2 이면 없어짐
    basic_plants_bullet = None
    basic_plants_bullet_BAAM = None
    def __init__(self , x , y):
        if (self.basic_plants_bullet == None):
            self.basic_plants_bullet = load_image('Tutorial/Tutorial_bullet.png')
        if (self.basic_plants_bullet_BAAM == None):
            self.basic_plants_bullet_BAAM = load_image('Tutorial/Tutorial_bullet_BAAM.png')
        self.x = x
        self.y = y
        self.state = 0
        self.seta = 0
        self.action = 0
        self.velocity = Bullet_SPEED_PPS
    def draw(self):
        if self.state == 0:
            self.basic_plants_bullet.clip_composite_draw(0 , 0 , 29 , 30 , 0 + self.seta,'' ,self.x , self.y , 29 , 30  )
        if self.state == 1:
            self.basic_plants_bullet_BAAM.clip_draw(0 , 0 , 51 , 45 ,self.x , self.y ,29 + self.action , 30 + self.action  )
        self.draw_bb()
    def update(self):
        if self.state == 0:
            self.x += self.velocity * game_framework.frame_time  # 총알 속도
            self.seta += 0.2  # 총알의 회전
        if self.state == 1: # 총알 상태
            self.action += self.velocity * game_framework.frame_time

            if(self.action > 20):
                self.state = 2




        if self.state == 2:
            game_world.remove_object(self)


        if self.x > 1450 - 25: # 화면 밖에 나가면 사라짐
            self.state = 2
            game_world.remove_object(self)

        pass
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 12, self.y - 13, self.x + 12, self.y + 13
