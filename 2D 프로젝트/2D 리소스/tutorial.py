import game_framework
from pico2d import *
from Zombies import Zombie
from Plants import plant
from Sun import Sun_shine
import game_world


PIXEL_PER_METER = (10.0 / 0.3)
#이동거리가 10pixsel 에 30cm간다는 뜻 임의로 정함
CHANGE_SPEED_KMPH = 10.0
# 10.0 속도
#  10.0 속도 =  km / hour 킬로미터 거리 / 시간
CHANGE_SPEED_MPM = (CHANGE_SPEED_KMPH * 1000.0 / 60 )
# 경과시간을 분으로 바꿈 (속도 * 1000 / 60)
CHANGE_SPEED_MPS = (CHANGE_SPEED_MPM / 60.0)
# 경과시간을 초로 바꿈
CHANGE_SPEED_PPS = (CHANGE_SPEED_MPS * PIXEL_PER_METER) # 픽셀 퍼 세크 미터 퍼세크에다가 픽셀퍼 미터를 곱한것
#거리 = 시간 * 속도


# 튜토리얼 이벤트
SHOW_HOUSE, SHOW_MAP, SHOW_ZOMBIE, RETURN_MAP, START  = range(5)


Plants_Card = None
Zombies = []
Plants = []#객체 선언
Zombie_count = 0
Plant_Count = 0 # 객체의의 개수
def creat_Zombie():  # 좀비 생성
    global Zombies , Zombie_count
    new_zombie = Zombie()
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_count = Zombie_count +1
def creat_Plant_card():
    global Plants_Card
    Plants_Card = plant()
def creat_Plants():
    global Plants , Plant_Count
    new_plant = plant()
    game_world.add_object(new_plant, 1)
    Plants.append(new_plant)

#MAP States

class Start_state:
    @staticmethod
    def enter(tutorial ,event):
        tutorial.frame = 0
        tutorial.start_time = get_time()


    @staticmethod
    def exit(tutorial , event):


        pass
    @staticmethod
    def do(tutorial):
        if (tutorial.timer - tutorial.start_time >= 2):
            tutorial.add_event(SHOW_MAP)

    @staticmethod
    def draw(tutorial):
        tutorial.Tutorial_Map.clip_draw(0 + tutorial.frame, 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        tutorial.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        tutorial.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        tutorial.font.draw(20, 530, '%d' % tutorial.sun_value)
        tutorial.font.draw(600, 50, 'My house...')
class Move_state: # 맵을 움직이는 스테이트
    global Zombies ,Zombie_count
    @staticmethod

    def enter(tutorial ,event):
        for i in range(5):  # 객체 생성
            creat_Zombie()
        tutorial.frame = 0
        tutorial.move_time = get_time()
        tutorial.velocity += CHANGE_SPEED_PPS
        tutorial.map_x  = 0
        tutorial.re = 0
        tutorial.Move_timer = 0 # 무브 타임
    @staticmethod
    def exit(tutorial , event):
        for i in range(5):
            Zombies[i].state = 1;
    @staticmethod
    def do(tutorial):
      if(tutorial.map_x < 500):# 좀비가 나타나야할 시간 300
          if(tutorial.re == 0):
              tutorial.map_x += tutorial.velocity * game_framework.frame_time  # 속도 * 시간
              for i in range(5):
                  Zombies[i].x -= (tutorial.velocity * game_framework.frame_time) * 1.7
              if (tutorial.map_x > 500):
                  tutorial.re = 1

      if(tutorial.re == 1):
          tutorial.Move_timer += 1
          print(tutorial.Move_timer)
          if (tutorial.Move_timer == 150):
              tutorial.Move_timer = 0
              tutorial.re = 2
      if(tutorial.re == 2):
          if (tutorial.map_x > 0):
              tutorial.map_x -= tutorial.velocity * game_framework.frame_time  # 속도 * 시간
              for i in range(5):
                  Zombies[i].x += (tutorial.velocity * game_framework.frame_time) * 1.7  # 좀비야 멈춰라
              if(tutorial.map_x < 295): # 맵을 원위치로
                  tutorial.Move_timer += 1
                  if (tutorial.Move_timer == 150):
                      tutorial.add_event(START)

    @staticmethod
    def draw(tutorial):
        tutorial.Tutorial_Map.clip_draw(int(tutorial.map_x), 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        tutorial.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        tutorial.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        tutorial.font.draw(20, 530, '%d' % tutorial.sun_value)
        tutorial.font.draw(600, 50, 'My house...')
    pass

class Stage_state:
    @staticmethod
    def enter(tutorial, event):
        creat_Plant_card()
        tutorial.frame = 0
        tutorial.stage_time = get_time()
        tutorial.order = 0
        tutorial.Tutorial_Start_music.set_volume(64)
        tutorial.Tutorial_Start_music.repeat_play()
    @staticmethod
    def exit(tutorial, event):
            pass

    @staticmethod
    def do(tutorial):
        if(tutorial.timer - tutorial.stage_time >= 2 and tutorial.order == 0):
            tutorial.Tutorial_GAME_START.set_volume(64)
            tutorial.Tutorial_GAME_START.repeat_play()
            tutorial.order = 1


        pass

    @staticmethod
    def draw(tutorial):
        tutorial.Tutorial_Map.clip_draw(250, 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        tutorial.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        tutorial.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        Plants_Card.draw_card(tutorial.select_card, tutorial.mouse_x, tutorial.mouse_y)
        tutorial.font.draw(20, 530, '%d' % tutorial.sun_value)
        if (tutorial.timer - tutorial.stage_time <= 2 and tutorial.order == 0):
            tutorial.Tutorial_Start_logo.draw(700, 300)

next_state_table = {
    Start_state : {SHOW_HOUSE : Start_state , SHOW_MAP:Move_state },
    Move_state : {SHOW_MAP: Move_state , START : Stage_state},
    Stage_state : {START : Stage_state  }
}

class Tutorial:
    def __init__(self):
        self.Tutorial_Map = load_image('Tutorial/Tutorial_map.png')
        self.board = load_image('Tutorial/board.png')
        self.intro_music = load_music('Tutorial/intro_music.mp3')
        self.Tutorial_Start_music = load_music('Tutorial/Tutorial_start.mp3')  # 초반 도입 음악
        self.Tutorial_GAME_START = load_music('Tutorial/Tutorial_GAME_START.mp3')  # 게임 스타트 음악
        self.font = load_font('Tutorial/ConsolaMalgun.ttf', 30)
        self.Tutorial_Start_logo = load_image('Tutorial/Turtorial_Start.png')
        self.cards = load_image('Tutorial/cards.png')
        self.intro_music.set_volume(64)  # 스테이지 들어오면 음악이 바로 재생되게함
        self.intro_music.repeat_play()
        self.velocity = 0
        self.event_que = [] #이벤트 큐
        self.frame = 0  # 화면을 옮겨주는 프레임
        self.cur_state = Start_state  # 화면을 옮겨주는 순서 정의
        self.cur_state.enter(self, None)
        # 화면 정지 시간
        self.str = "우리들의 집"  # 글자 출력
        self.sun_value = 200  # 자원량
        self.select_card = 0  # 무슨 카드를 선택했는지 아는 변수
        self.timer = 0
        self.mouse_x =0
        self.mouse_y =0

    def add_event(self , event):
        self.event_que.insert(0,event) # 이벤트를 추가
    def update(self):
        self.timer = get_time() # 계속 시간을 잰다.
        self.cur_state.do(self) #현재 스테이트의 do를 해준다.
        if len(self.event_que) > 0: #이벤트 큐에서 이벤트를 하나씩 꺼냄
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self) #현재 상태를 드로우
        pass
    def handle_event(self,event):
        if(self.cur_state == Stage_state
        and event.type == SDL_MOUSEBUTTONDOWN): #마우스 버튼 다운시
            if (event.button == SDL_BUTTON_LEFT and event.x > 100 and event.x < 180 and 0 +600 - event.y - 1 < 0 +600 and 0 +600 - event.y - 1 > 0 +600 - 80 and self.sun_value >= 100 and self.select_card == 0):
                self.select_card = 1
                self.sun_value = self.sun_value - 100
                pass
            elif (event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1300 and event.y < 339 and event.y > 255 and self.select_card > 0):
                # 여기서부턴 튜토리얼 대지 영역
                for i in range(9):
                    if (event.x >= i * 140 and event.x <= i * 140 + 140):
                        global Plant_Count
                        creat_Plants()
                        Plants[Plant_Count].x = int(i * 140 + 70)
                        Plants[Plant_Count].y = int(282)
                        Plant_Count = Plant_Count + 1
                        self.select_card = 0
            if (event.button == SDL_BUTTON_RIGHT):
                self.select_card = 0  # 오른쪽 버튼을 누르면 초기화
                self.sun_value = self.sun_value + 100

        # 마우스 모션
        if (self.cur_state == Stage_state
                and event.type == SDL_MOUSEMOTION):
            self.mouse_x =  event.x
            self.mouse_y = event.y




