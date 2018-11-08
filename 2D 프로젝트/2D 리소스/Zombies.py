from pico2d import *
import game_framework
import random
import game_world
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

#공격
TIME_PER_ACTION_ATTACK = 2
ACTION_PER_TIME_ATTACK = 1.0 / TIME_PER_ACTION_WALK #1초에 할 액션수 2개
FRAMES_PER_ACTION_ATTACK = 20 # 21 개

# 죽음
TIME_PER_ACTION_Dead = 3.5
ACTION_PER_TIME_Dead = 1.0 / TIME_PER_ACTION_Dead #1초에 할 액션수 2개
FRAMES_PER_ACTION_Dead = 9
class Zombie:
    IDLE, WALK, ATTACK ,HEAD_DOWN , DIE , Remove = 0, 1, 2 ,3 , 4 , 5
    start_frame = 0
    order = 0
    Basic_Zombies = None
    Basic_Zombies_Walk = None
    Basic_Zombies_Head = None
    Basic_Zombies_NO_Head = None
    Basic_Zombies_Die = None
    Basic_Zombies_Attack = None
    def __init__(self):
        self.x, self.y = random.randint(1700 , 1800) , random.randint(100 , 450)
        self.frame = random.randint(0, 11)
        self.Line = 2
        self.state = self.IDLE
        self.collide = False
        self.head = 0
        self.velocity = Zombie_SPEED_PPS
        self.Zombie_time = 0
        if(self.Basic_Zombies == None):
            self.Basic_Zombies = load_image('Tutorial/basic_zombie_idle.png')
        if (self.Basic_Zombies_Walk == None):
            self.Basic_Zombies_Walk = load_image('Tutorial/Tutorial_Zombie_walk.png')
        if (self.Basic_Zombies_Head == None):
            self.Basic_Zombies_Head = load_image('Tutorial/Tutorial_Zombie_head.png')
        if(self.Basic_Zombies_NO_Head == None):
            self.Basic_Zombies_NO_Head = load_image('Tutorial/Tutorial_Zombie_nohead_walk.png')
        if(self.Basic_Zombies_Die == None):
            self.Basic_Zombies_Die = load_image('Tutorial/Tutorial_Zombie_nohead_Die.png')
        if(self.Basic_Zombies_Attack == None):
            self.Basic_Zombies_Attack = load_image('Tutorial/Tutorial_Zombie_Attack.png')
        self.hp = 2
        self.world_time = get_time()
    def update(self):
        self.world_time = get_time()

        if(self.state == self.IDLE):
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME_IDLE * game_framework.frame_time ) % 11


            # 좀비가 가만이 있는 상태일때
        if(self.state == self.WALK):
            self.frame = (self.frame + FRAMES_PER_ACTION_WALK * ACTION_PER_TIME_WALK * game_framework.frame_time) % 17
            self.x -= self.velocity * game_framework.frame_time
            self.get_bb()

            if(self.hp <= 0):
                self.state = self.HEAD_DOWN # 머리가 떨어져서 걷다가 죽어야함
                self.head = 1 # 머리가 떨어짐
                self.Zombie_time = get_time() #머리가 떨어진 시간을 잰다 .
        if (self.state == self.ATTACK):
            if (self.hp <= 0):
                self.state = self.HEAD_DOWN  # 머리가 떨어져서 걷다가 죽어야함
                self.head = 1  # 머리가 떨어짐
                self.Zombie_time = get_time()  # 머리가 떨어진 시간을 잰다 .
        #좀비 머리 떨어짐
        if(self.state == self.HEAD_DOWN): #머리가 떨어져서 걷고 있을때
            self.frame = (self.frame + FRAMES_PER_ACTION_WALK * ACTION_PER_TIME_WALK * game_framework.frame_time) % 17
            self.x -= self.velocity * game_framework.frame_time
            if(self.world_time - self.Zombie_time > 4):
                self.state = self.DIE
                self.Zombie_time = get_time() # 상태변화 시간을 잰다 .
                self.frame = 0
        #좀비 사망
        if (self.state == self.DIE):
            if(self.frame > 8):
                if(self.world_time - self.Zombie_time > 5):
                    self.state = self.Remove
                    game_world.remove_object(self)
            elif(self.frame < 8):
                self.frame = (self.frame + FRAMES_PER_ACTION_Dead * ACTION_PER_TIME_Dead * game_framework.frame_time) % 9
        #좀비 공격
        if (self.state == self.ATTACK):
            self.frame = (self.frame + FRAMES_PER_ACTION_ATTACK * ACTION_PER_TIME_ATTACK * game_framework.frame_time) % 20

        #line 에 따라서 y 값 관리
        for i in range(0, 5):
            if self.Line == i and self.state != self.IDLE:
                self.y = self.y = (i + 1) * 100




    def draw(self):
        if(self.state == self.IDLE):


            self.Basic_Zombies.clip_draw(int(self.frame) * 166, 0, 81, 120, self.x , self.y)
        if(self.state == self.WALK):
            self.Basic_Zombies_Walk.clip_draw(int(self.frame) * 166 - 3, 0, 90, 128, self.x, self.y)
            self.draw_bb()
        if (self.state == self.HEAD_DOWN):
            self.Basic_Zombies_NO_Head.clip_draw(int(self.frame) * 181 - 3, 0, 90, 95, self.x, self.y , 90 , 100)
        if (self.state == self.DIE):
            self.Basic_Zombies_Die.clip_draw(int(self.frame) * 173 - 20, 0, 180, 95, self.x, self.y)  # 여백 안둬서
        if (self.state == self.ATTACK):
            self.Basic_Zombies_Attack.clip_draw(int(self.frame) * 181 - 3, 0, 90, 128, self.x, self.y)

    def Attack(self):
        pass
    def get_bb(self):
        return self.x - 25, self.y - 30, self.x + 25, self.y + 30
    def draw_bb(self):
        draw_rectangle(*self.get_bb())



class Buket_Zombie(): # 상속
    IDLE, WALK, ATTACK, HEAD_DOWN, DIE, Remove = 0, 1, 2, 3, 4, 5
    Buket_IDLE = None
    Buket_Walk = None
    def __init__(self):
        if(self.Buket_IDLE == None):
            self.Buket_IDLE = load_image('Stage1/Buket_Zombie_Idle.png')
        if (self.Buket_Walk == None):
            self.Buket_Walk = load_image('Stage1/Buket_Zombie_Walk.png')
            self.x, self.y = random.randint(1700, 1800), random.randint(100, 450)
            self.frame = random.randint(0, 11)
            self.Line = 2
            self.state = self.IDLE
            self.collide = False
            self.head = 0
            self.velocity = Zombie_SPEED_PPS
            self.Zombie_time = 0
            print(10102)
    def draw(self):
        if (self.state == self.IDLE):
            self.Buket_IDLE.clip_draw(int(self.frame) * 196, 0, 176, 134, self.x, self.y)
        pass
    def update(self):
        self.world_time = get_time()

        if(self.state == self.IDLE):
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME_IDLE * game_framework.frame_time ) % 5

        for i in range(0, 5):
            if self.Line == i and self.state != self.IDLE:
                self.y = self.y = (i + 1) * 100

class Cone_Zombie:
    IDLE, WALK, ATTACK, HEAD_DOWN, DIE, Remove = 0, 1, 2, 3, 4, 5
    Cone_Zombie_IDLE = None
    Cone_Zombie_Walk = None
    def __init__(self):
        if(self.Cone_Zombie_IDLE == None):
            self.Cone_Zombie_IDLE = load_image('Stage1/Cone_Zombie_Idle.png')
        if (self.Cone_Zombie_Walk == None):
            self.Cone_Zombie_Walk = load_image('Stage1/Cone_Zombie_Walk.png')
            self.x, self.y = random.randint(1700, 1800), random.randint(100, 450)
            self.frame = random.randint(0, 11)
            self.Line = 2
            self.state = self.IDLE
            self.collide = False
            self.head = 0
            self.velocity = Zombie_SPEED_PPS
            self.Zombie_time = 0
            print(10102)
    def draw(self):
        if (self.state == self.IDLE):
            self.Cone_Zombie_IDLE.clip_draw(int(self.frame) * 196, 0, 176, 143, self.x, self.y)
        pass
    def update(self):
        self.world_time = get_time()

        if(self.state == self.IDLE):
            self.frame = (self.frame + FRAMES_PER_ACTION_IDLE * ACTION_PER_TIME_IDLE * game_framework.frame_time ) % 7

        for i in range(0, 5):
            if self.Line == i and self.state != self.IDLE:
                self.y = self.y = (i + 1) * 100