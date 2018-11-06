import game_framework
from pico2d import *
from Zombies import Zombie
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
    def draw(tutorial):
        Stage_level_1.Tutorial_Map.clip_draw(0 + tutorial.frame, 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        Stage_level_1.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        Stage_level_1.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        Stage_level_1.font.draw(20, 530, '%d' % tutorial.sun_value)
        Stage_level_1.font.draw(600, 50, 'Stage 1')



class Stage_level_1:
    def __init__(self):
        self.Stage_level_1 = load_image('Tutorial/Tutorial_map.png')
        self.board = load_image('Tutorial/board.png')
        self.intro_music = load_music('Tutorial/intro_music.mp3')
        self.Stage_level_1_Start_music = load_music('Tutorial/Tutorial_start.mp3')  # 초반 도입 음악
        self.Stage_level_1_GAME_START = load_music('Tutorial/Tutorial_GAME_START.mp3')  # 게임 스타트 음악
        self.font = load_font('Tutorial/ConsolaMalgun.ttf', 30)
        self.Stage_level_1_Start_logo = load_image('Tutorial/Turtorial_Start.png')
        self.cards = load_image('Tutorial/cards.png')
        self.arrow = load_image('Tutorial/Tutorial_arrow.png')
        self.time_bar_image = load_image('Tutorial/progress_bar.png')
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