from pico2d import *
import game_framework
import random

PIXEL_PER_METER = (10.0 / 0.3)
#이동거리가 10pixsel 에 30cm간다는 뜻 임의로 정함
Zombie_SPEED_KMPH = 2.0
# 10.0 속도
#  10.0 속도 =  km / hour 킬로미터 거리 / 시간
Zombie_SPEED_MPM = (Zombie_SPEED_KMPH * 1000.0 / 60 )
# 경과시간을 분으로 바꿈 (속도 * 1000 / 60)
Zombie_SPEED_MPS = (Zombie_SPEED_MPM / 60.0)
# 경과시간을 초로 바꿈
Zombie_SPEED_PPS = (Zombie_SPEED_MPS * PIXEL_PER_METER) # 픽셀 퍼 세크 미터 퍼세크에다가 픽셀퍼 미터를 곱한것

#액션 타임
TIME_PER_ACTION_IDLE = 2
ACTION_PER_TIME_IDLE = 1.0 / TIME_PER_ACTION_IDLE #1초에 할 액션수 2개
FRAMES_PER_ACTION_IDLE = 11 # 8개의 프레임



#워크 타임
TIME_PER_ACTION_WALK = 3
ACTION_PER_TIME_WALK = 1.0 / TIME_PER_ACTION_WALK #1초에 할 액션수 2개
FRAMES_PER_ACTION_WALK = 17
class Zombie:
    WALK, ATTACK ,DIE ,END ,IDLE = 1, 2, 3 ,4 , 5
    start_frame = 0
    order = 0
    def __init__(self):
        self.x, self.y = random.randint(1900 , 2000) , random.randint(100 , 450)
        self.frame = random.randint(0, 11)
        self.Line = 2
        self.state = self.IDLE
        self.velocity = Zombie_SPEED_PPS
        self.Basic_Zombies = load_image('Tutorial/basic_zombie_idle.png')
        self.Basic_Zombies_Walk = load_image('Tutorial/Tutorial_Zombie_walk.png')

    def update(self):
        if(self.state == self.IDLE):
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME_IDLE * game_framework.frame_time ) % 11


            # 좀비가 가만이 있는 상태일때
        if(self.state == self.WALK):
            self.frame = (self.frame + FRAMES_PER_ACTION_WALK * ACTION_PER_TIME_WALK * game_framework.frame_time) % 17
            self.x -= self.velocity * game_framework.frame_time
            self.get_bb()



    def draw(self):
        if(self.state == self.IDLE):


            self.Basic_Zombies.clip_draw(int(self.frame) * 166, 0, 81, 120, self.x , self.y)
        if(self.state == self.WALK):
            self.Basic_Zombies_Walk.clip_draw(int(self.frame) * 166  - 3, 0 , 90 , 128 , self.x  , self.y)
            self.draw_bb()

    def Walk(self):
        self.y = 300
        self.state = self.WALK
    def Attack(self):
        pass
    def get_bb(self):
        return self.x - 25, self.y - 30, self.x + 25, self.y + 30
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
