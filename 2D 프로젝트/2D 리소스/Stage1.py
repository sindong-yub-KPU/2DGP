import game_framework
from pico2d import *
from Zombies import Zombie
from Zombies import Buket_Zombie
from Plants import plant
from Sun import Sun_shine
from Bullets import Bullet
import game_world
import random
import title_state


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

next_state_table = {
(SDL_KEYDOWN, SDLK_1): SHOW_MAP,
(SDL_KEYDOWN,SDLK_2) : START


}
Plants_Card = None
Zombies = []
Plants = []
Sun = []
Bullets = [] # 객체 리스트
Zombie_Count = 0
Plant_Count = 0
Sun_Count = 0
Bullet_Count = 0 #객체 개수
def creat_Bullet( x , y ):
    global Bullets , Bullet_Count
    New_Bullet = Bullet(x + 30, y )
    Bullets.append(New_Bullet)
    game_world.add_object(New_Bullet, 1)
    Bullet_Count += 1
#총알 생산
def creat_Zombie():  # 좀비 생성
    global Zombies , Zombie_Count
    new_zombie = Zombie()
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count +1
def creat_Buket_Zombie():
    global Zombies, Zombie_Count
    new_zombie = Buket_Zombie()
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count + 1
#좀비 생산
def creat_Plant_card():
    global Plants_Card
    Plants_Card = plant(0 , 0, 0)
#식물을 눌렀을때 생산
def creat_Plants( x, y , Line_ ):
    global Plants , Plant_Count
    new_plant = plant(x, y , Line_)
    game_world.add_object(new_plant, 1)
    Plants.append(new_plant)
    Plant_Count = Plant_Count + 1
#식물 생산

def creat_Sun():
    global Sun , Sun_Count
    new_Sun = Sun_shine()

    Sun.append(new_Sun)
    game_world.add_object(new_Sun, 1)

    Sun_Count += 1
#자원 생산
def collide(a, b): #사각형 충돌제크
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False
    return True
#충돌을 알기 위한 함수
def Collide_check(): # 충돌체크 편하기 위해 만듬
    global Zombies , Plants , Bullets
    global Plant_Count

    for Zombie in Zombies:
        for Bullet in Bullets:
            if collide(Bullet, Zombie) and Bullet.state != 1 and Zombie.hp > 0:

                Zombie.hp -=  1
                Bullet.state = 1 # 총알을 없에준다
                break;
    for plant in Plants:
         #지금 식물에 대한 상태값을 위해 지금 식물이 맞고 있는중인지 아닌지
        for Zombie in Zombies: #좀비가 충돌이 아닌상태라면 상태를 바꿔줘야한다.
            if collide(plant, Zombie) and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5:
                Zombie.state = 2
                Zombie.collide = True
                plant.state = 3

            elif (Zombie.collide != True  and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5):
                Zombie.state = 1
         #   if(plant_hited != True): #지금 식물이 맞고 있는 중이 아니라면?
             #   plant.state = 1
    for Zombie in Zombies: # 모든 좀비에 대하여
        Zombie.collide = False
        if(Plant_Count == 0  and Zombie.state != 3 and Zombie.state != 4 and  Zombie.state != 5): # 모든 좀비가 죽은 상태가 아니고 식물 숫자가 0이라면
            Zombie.state = 1 #좀비의 상태는 워킹


    pass
#충돌체크
def Delete_all():
    global Zombies, Plants, Bullets
    global Zombie_Count
    global Plant_Count
    for Zombie in Zombies:
        if(Zombie.state == 5):

            Zombies.remove(Zombie)
            del Zombie
            Zombie_Count = Zombie_Count - 1

    for Bullet in Bullets:
        if(Bullet.state == 2):
            Bullets.remove(Bullet)
            del Bullet
    for plant in Plants:

        if (plant.state == 3 and plant.hp <= 0):
            Plants.remove(plant)
            del plant
            Plant_Count = Plant_Count - 1
#객체들이 경우에 따라서 삭제됨

def clear(): #객체 리스트 다 삭제
    global Zombies, Plants, Bullets , Sun
    global Zombie_Count
    global Plant_Count
    global Bullet_Count
    del Zombies
    del Plants
    del Bullets
    del Sun

    Zombies = []
    Plants = []
    Sun = []
    Bullets = []  # 객체 리스트

    Plant_Count =0
    Zombie_Count =0
    Bullet_Count=0
#객체 리스트 다 삭제

class Start_state:
    @staticmethod
    def enter(Stage_level_1 ,event):
        Stage_level_1.frame = 0
        Stage_level_1.start_time = get_time()


    @staticmethod
    def exit(Stage_level_1 , event):


        pass
    @staticmethod
    def do(Stage_level_1):
        if (Stage_level_1.timer - Stage_level_1.start_time >= 2):
            Stage_level_1.add_event(SHOW_MAP)

    @staticmethod
    def draw(Stage_level_1):
        Stage_level_1.Stage_level_1_map.clip_draw(0 + Stage_level_1.frame, 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        Stage_level_1.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        Stage_level_1.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        Stage_level_1.cards.clip_draw(64, 485, 70, 90, 210, 560, 64, 70)
        Stage_level_1.font.draw(28, 532, '%d' % Stage_level_1.sun_value)
        Stage_level_1.font.draw(600, 50, 'Stage 1')
class Move_state:
    global Zombies , Zombie_Count
    @staticmethod

    def enter(Stage_level_1 , event):
        Stage_level_1.frame = 0
        Stage_level_1.move_time = get_time()
        Stage_level_1.velocity += CHANGE_SPEED_PPS
        Stage_level_1.map_x = 0
        Stage_level_1.re = 0
        Stage_level_1.Move_timer = 0  # 무브 타임

        for i in range(2):
            creat_Zombie()
            creat_Buket_Zombie()


        for Zombie  in Zombies:

            Zombie.x += random.randint(100, 200)
        for Buket_Zombie in Zombies:
            Buket_Zombie.x += random.randint(100, 200)
    @staticmethod
    def exit(Stage_level_1,event):
        for Zombie in Zombies:
            Zombie.state = 1;
            Zombie.y = 300
            Zombie.x = 1500
    @staticmethod
    def do(Stage_level_1):
        if (Stage_level_1.map_x < 500):  # 좀비가 나타나야할 시간 300
            if (Stage_level_1.re == 0):
                Stage_level_1.map_x += Stage_level_1.velocity * game_framework.frame_time  # 속도 * 시간
                for Zombie in Zombies:
                    Zombie.x -= (Stage_level_1.velocity * game_framework.frame_time) * 1.7
                if (Stage_level_1.map_x > 500):
                    Stage_level_1.re = 1

        if(Stage_level_1.re == 1):
            Stage_level_1.Move_timer += 1

            if (Stage_level_1.Move_timer == 150):
                Stage_level_1.Move_timer = 0
                Stage_level_1.re = 2
        if (Stage_level_1.re == 2):
            if (Stage_level_1.map_x > 0):
                Stage_level_1.map_x -= Stage_level_1.velocity * game_framework.frame_time  # 속도 * 시간
                for Zombie in Zombies:
                    Zombie.x += (Stage_level_1.velocity * game_framework.frame_time) * 1.7  # 좀비야 멈춰라
                if (Stage_level_1.map_x < 330):  # 맵을 원위치로
                    Stage_level_1.Move_timer += 1
                    if (Stage_level_1.Move_timer == 150):
                        Stage_level_1.add_event(START)
    @staticmethod
    def draw(Stage_level_1):
        Stage_level_1.Stage_level_1_map.clip_draw(int(Stage_level_1.map_x), 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        Stage_level_1.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        Stage_level_1.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        Stage_level_1.cards.clip_draw(62, 485, 70, 90, 210, 560, 64, 70)
        Stage_level_1.font.draw(28, 532, '%d' % Stage_level_1.sun_value)
        Stage_level_1.font.draw(600, 50, 'Defence the Zombies!!', (255, 0, 0))

class Stage_state:
    pass


next_state_table = {
    Start_state : {SHOW_HOUSE : Start_state , SHOW_MAP:Move_state ,START : Stage_state },
    Move_state : {SHOW_MAP: Move_state , START : Stage_state},
    Stage_state : {START : Stage_state  }
}
class Stage_level_1:
    def __init__(self):
        self.Stage_level_1_map = load_image('Stage1/Tutorial_map.png')
        self.board = load_image('Stage1/board.png')
        self.intro_music = load_music('Stage1/intro_music.mp3')
        self.Stage_level_1_Start_music = load_music('Stage1/Tutorial_start.mp3')  # 초반 도입 음악
        self.Stage_level_1_GAME_START = load_music('Stage1/Tutorial_GAME_START.mp3')  # 게임 스타트 음악
        self.font = load_font('Stage1/ConsolaMalgun.ttf', 25)
        self.Stage_level_1_Start_logo = load_image('Stage1/Turtorial_Start.png')
        self.cards = load_image('Stage1/cards.png')
        self.arrow = load_image('Stage1/Tutorial_arrow.png')
        self.time_bar_image = load_image('Stage1/progress_bar.png')
        self.time_bar = 0
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
        self.mouse_x = 0
        self.mouse_y = 0
        self.game_over =0 # 게엠 오버 확인

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
            #카드 고르기
            if (event.button == SDL_BUTTON_LEFT and event.x > 100 and event.x < 180 and 0 +600 - event.y - 1 < 0 +600 and 0 +600 - event.y - 1 > 0 +600 - 80 and self.sun_value >= 100 and self.select_card == 0):
                self.select_card = 1
                self.sun_value = self.sun_value - 100
                if(self.Click_order == 0):
                    self.Click_order = 1
                pass
            elif (event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1300 and event.y < 339 and event.y > 255 and self.select_card > 0):
                # 여기서부턴 튜토리얼 대지 영역
                for i in range(9):
                    if (event.x >= i * 140 and event.x <= i * 140 + 140): #가운데 라인 생성
                        global Plant_Count
                        if(self.Click_order < 3):
                            self.Click_order = 3  # 튜토리얼 표지판 때문에 생성

                        creat_Plants(int(i * 140 + 70) ,int(282) , 2 )



                        self.select_card = 0

            # 자원을 얻는것
            elif (event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1400 and event.y >= 0 and event.y <= 600):
                global Sun_Count , Sun
                for Sun_shine in Sun:

                    if (event.x > Sun_shine.x - 50 and event.x < Sun_shine.x + 50 and 600 - event.y - 1 > Sun_shine.y - 50 and 600 - event.y - 1 < Sun_shine.y + 50):

                        self.Click_order = 5
                        Sun_shine.click = 1
                        Sun_shine.plus_x = Sun_shine.x# 좌표를 보내줌
                        Sun_shine.plus_y = Sun_shine.y
                        del Sun_shine  # 누르면 삭제

                        Sun_Count -= 1 # 자원의 개수를 줄여줌

                        self.sun_value = self.sun_value + 30  # 자원 증가
                        break
            #카드 선택 해제
            if (event.button == SDL_BUTTON_RIGHT and self.select_card > 0):
                self.select_card = 0  # 오른쪽 버튼을 누르면 초기화
                self.sun_value = self.sun_value + 100

        # 마우스 모션
        if (self.cur_state == Stage_state
                and event.type == SDL_MOUSEMOTION):
            self.mouse_x = event.x
            self.mouse_y = event.y
        # 장면 넘어가기
        if(event.type == SDL_KEYDOWN):
            if(event.key == SDLK_1):
                self.add_event(SHOW_MAP)
            if(event.key == SDLK_2):
                self.add_event(START)


