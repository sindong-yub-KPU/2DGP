import game_framework
from pico2d import *
from ball import Ball
import random
import game_world
import math
# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3)
#이동거리가 10pixsel 에 30cm간다는 뜻
RUN_SPEED_KMPH = 20.0
#  20.0 속도 =  km / hour 킬로미터 거리 / 시간
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60 )
# 경과시간을 분으로 바꿈 (속도 * 1000 / 60)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
# 경과시간을 초로 바꿈
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER) # 픽셀 퍼 세크 미터 퍼세크에다가 픽셀퍼 미터를 곱한것
#거리 = 시간 * 속도
# 속도 = 거리 / 시간
RUN_DEGREE_PPS = 3.141592* 4 # 초당 더할 각도 360
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION #1초에 할 액션수 2개
FRAMES_PER_ACTION = 8 # 8개의 프레임
#액션의 싱크를 맞추기위해 만든 변수들 frame 값을 올려주는것을 1로 고정하는것이 아니라
#따로따로 다 관리 해주기 위해 만들어주는것
#게임 내에서 변화 하는 모든 것들은 속도의 개념이 필요함


# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE , Ghost  = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS

        boy.Idle_time = get_time()


    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        if boy.timer - boy.Idle_time >= 10.0: #

            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity ,1)
        # 미니멈과 변수 맥시멈
        # 변수의 최솟값 최대값을 찾을 수 있다.


    @staticmethod
    def exit(boy, event):

        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time
        #거리 = 속도 * 시간
        #보이의 x 좌표는 = 보이의속도 * 프레임 시간
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:

    @staticmethod
    def enter(boy, event):
        boy.frame = 0
        boy.sleep_time = get_time() #내가 딱 눕게 된 시간을 받는다 .
    @staticmethod
    def exit(boy, event):
        boy.image.opacify(1)
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if(boy.timer - boy.sleep_time >= 3):
            boy.add_event(Ghost)
    @staticmethod
    def draw(boy):

        boy.image.opacify(1)
        if boy.dir == 1:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
            boy.image.opacify(random.randint(1, 100) * 0.01)
            boy.image.clip_composite_draw(int(boy.frame) * 100 , 300 , 100 , 100 ,
            3.141592 / 2 -3.141592 / 8 * (boy.timer - boy.sleep_time),'' ,
            boy.x-25 , boy.y -25 + (boy.timer - boy.sleep_time) * 20,100,100   )
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
            boy.image.opacify(random.randint(1, 100) * 0.01)
            boy.image.clip_composite_draw(int(boy.frame) * 100 , 200 , 100 , 100 ,
            -3.141592 /2 + 3.141592/8 * (boy.timer - boy.sleep_time) , '' , boy.x+25,
            boy.y-25 + (boy.timer - boy.sleep_time) * 20 , 100 , 100)

class Ghost_State:
    @staticmethod
    def enter(boy ,event):
        boy.frame = 0
        boy.Ghost_time = get_time()
        boy.degree = 3.141592 /2
    @staticmethod
    def exit(boy , evnet):
        boy.image.opacify(1)
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time ) % 8
        boy.degree -= RUN_DEGREE_PPS * game_framework.frame_time
    @staticmethod
    def draw(boy):
        boy.image.opacify(1)
        if boy.dir == 1:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25,
                                          100, 100)
            boy.image.opacify(random.randint(1, 100) * 0.01)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100,
                                          3.141592 / 2 - 3.141592 / 8 * 4, '',
                                          boy.x - 25 + PIXEL_PER_METER *3 * math.cos(boy.degree),
                                          boy.y - 25 + 80 + PIXEL_PER_METER *3 * math.sin(boy.degree), 100, 100)
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25,
                                          boy.y - 25, 100, 100)
            boy.image.opacify(random.randint(1, 100) * 0.01)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100,
                                          -3.141592 / 2 + 3.141592 / 8 * 4, '', boy.x + 25 + PIXEL_PER_METER *3 * math.cos(-boy.degree),
                                          boy.y - 25 + 80 + PIXEL_PER_METER *3 * math.sin(-boy.degree), 100, 100)
        pass



next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState , Ghost : Ghost_State},
    Ghost_State: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState, Ghost : Ghost_State }
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF',16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.timer = 0
        self.postinon_y =0;
    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.timer = get_time()
        self.cur_state.draw(self)
        self.font.draw(self.x - 60 , self.y + 50, '(Time : %3.2f)' % get_time() , (255,255,0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_
            event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)