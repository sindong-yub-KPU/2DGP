import game_framework
from pico2d import *
from Zombies import Zombie
from Plants import plant
from Sun import Sun_shine
from Bullets import Bullet
import game_world
import random
import title_state
import Stage1_state
import math

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
def creat_Zombie():  # 좀비 생성
    global Zombies , Zombie_Count
    new_zombie = Zombie()
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count +1
def creat_Plant_card():
    global Plants_Card
    Plants_Card = plant(0 , 0, 0 , 0)
def creat_Plants( x, y , Line_  , sitting):
    global Plants , Plant_Count
    new_plant = plant(x, y , Line_ ,sitting)
    game_world.add_object(new_plant, 1)
    Plants.append(new_plant)
    Plant_Count = Plant_Count + 1


def creat_Sun():
    global Sun , Sun_Count
    new_Sun = Sun_shine()

    Sun.append(new_Sun)
    game_world.add_object(new_Sun, 1)

    Sun_Count += 1

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
def Collide_check(tutorial): # 충돌체크 편하기 위해 만듬
    global Zombies , Plants , Bullets
    global Plant_Count

    for Zombie in Zombies:

        for Bullet in Bullets:
            if collide(Bullet, Zombie) and Bullet.state == 0 and Zombie.hp > 0 :

                tutorial.splat.play()
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
    global Zombies ,Zombie_Count
    @staticmethod

    def enter(tutorial ,event):
        for i in range(5):  # 객체 생성
            creat_Zombie()
            Zombies[i].Line = random.randint(0, 4)
            Zombies[i].x += 300
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
            Zombies[i].y = 300 # 좌표를 다 300으로 바꿔줌
            Zombies[i].x = 1500

        for i in range(5):
            Zombies[i].x += random.randint(100, 300)
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

          if (tutorial.Move_timer == 150):
              tutorial.Move_timer = 0
              tutorial.re = 2
      if(tutorial.re == 2):
          if (tutorial.map_x > 0):
              tutorial.map_x -= tutorial.velocity * game_framework.frame_time  # 속도 * 시간
              for i in range(5):
                  Zombies[i].x += (tutorial.velocity * game_framework.frame_time) * 1.7  # 좀비야 멈춰라
              if(tutorial.map_x < 330): # 맵을 원위치로
                  tutorial.Move_timer += 1
                  if (tutorial.Move_timer == 150):
                      tutorial.add_event(START)



    @staticmethod
    def draw(tutorial):
        tutorial.Tutorial_Map.clip_draw(int(tutorial.map_x), 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        tutorial.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        tutorial.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        tutorial.font.draw(20, 530, '%d' % tutorial.sun_value)
        tutorial.font.draw(600, 50, 'Defence the Zombies!!' ,(255, 0 , 0) )
    pass

class Stage_state:
    global Plants, Plant_Count
    @staticmethod
    def enter(tutorial, event):
        creat_Plant_card()
        tutorial.frame = 0
        tutorial.stage_time = get_time()
        tutorial.time_bar_time = get_time()
        tutorial.order = 0
        tutorial.Tutorial_Start_music.set_volume(32)
        tutorial.Tutorial_Start_music.play(1)
        tutorial.velocity += CHANGE_SPEED_PPS
        tutorial.arrow_y = 560 - 100
        tutorial.arrow_x = 0
        tutorial.game_over_time = 0
        for i in range(5):

            Zombies[i].state = 1;
            Zombies[i].y = 300 # 좌표를 다 300으로 바꿔줌
            Zombies[i].x = 1800
            Zombies[i].frame = random.randint(0, 17)
            Zombies[i].Line = 2
        for i in range(5):
            Zombies[i].x += i * random.randint(200 , 400)
    @staticmethod
    def exit(tutorial, event):
            pass

    @staticmethod
    def do(tutorial):
        if tutorial.zombiecome == False:
            if(Zombies[0].x < 1500):
                tutorial.ZombiescomingSound.play()
                tutorial.zombiecome = True
        if(tutorial.timer - tutorial.stage_time >= 2 and tutorial.order == 0):
            tutorial.Tutorial_GAME_START.set_volume(32)
            tutorial.Tutorial_GAME_START.repeat_play()
            tutorial.order = 1

        if(tutorial.Click_order == 0 or tutorial.Click_order == 2 or tutorial.Click_order == 4): #첫번째 화살표 , 두번째 화살표 애니메이션을 위해
            if (tutorial.timer % 0.8 < 0.4):
                tutorial.arrow_y += tutorial.velocity * game_framework.frame_time
            elif (tutorial.timer % 0.8 >= 0.4):
                tutorial.arrow_y -= tutorial.velocity * game_framework.frame_time
        if tutorial.Click_order == 1: # 화살표의 좌표를 바꿔주기 위해
            tutorial.arrow_y = 340
            tutorial.Click_order = 2

        # 화살표 때문에 만든것
        if tutorial.Click_order >= 3: # 태양을 생산

            if(tutorial.timer - tutorial.stage_time > 5 ):
                tutorial.stage_time = get_time() # 5초 마다 Sun이 나오게함
                creat_Sun()
                if(tutorial.Click_order < 4):
                    tutorial.Click_order = 4
                    if tutorial.Click_order == 4:
                        tutorial.arrow_y = Sun[0].x  # y가 대신 받는다.
        #식물 라인에 좀비가 등장할 경우 식물은 탄을 쏘게 해야한다 라인마다 번호를 부여해서 좀비가 그 라인에
        #등장하면 쏘게한다.
        for plant in Plants:
            Zombie_line = False
            for Zombie in Zombies:
                if ((plant.Line == Zombie.Line) and Zombie.x < 1400 and Zombie.state != 4):
                     #라인이 같고 1400 이하일때 쏜다 . 라인이 같은 좀비가 없다면
                    plant.state = 2
                    Zombie_line = True
                if(((plant.Line != Zombie.Line) or Zombie.x > 1400) and Zombie_line != True):
                    plant.state = 1
            if(Zombie_Count == 0):
                plant.state = 1
        for plant in Plants:
            if(plant.state == 2):
                if tutorial.timer - plant.state_time > 5:
                    tutorial.shoot.play()
                    creat_Bullet(plant.x , plant.y + 30)
                    plant.state_time = get_time()


        if(tutorial.timer - tutorial.time_bar_time >= 1):
            if(tutorial.time_bar <= 300):
                tutorial.time_bar = (5 - Zombie_Count) * 60  #시간바의 이동속도

            tutorial.time_bar_time = get_time() # 아래 게임 시간 바를 그려주는것

        Collide_check(tutorial) #객체들의 충돌 체크

        Delete_all() # 객체들의 삭제
        global Plant_Count
        for plant in Plants:

            if (plant.state == 3 and plant.hp <= 0):
                for i in range(len(tutorial.count)):
                    if (plant.sitting == tutorial.count[i]):
                        tutorial.count.remove(plant.sitting)
                        break
                Plants.remove(plant)
                del plant
                Plant_Count = Plant_Count - 1
        # 다음 스테이지로 넘어감 스테이지 클리어
        if(Zombie_Count == 0): # 스테이지 넘어가는 조건
            clear()
            game_framework.change_state(Stage1_state)

        # 게임 오버
        if(tutorial.game_over == 0):
            for Zombie in Zombies:
                if (Zombie.x < 0):
                    tutorial.game_over = 1
                    tutorial.game_over_sound.play()

        if(tutorial.game_over == 1):
            tutorial.game_over_time = get_time()
            tutorial.game_over = 2
        if(tutorial.game_over == 2 and tutorial.timer - tutorial.game_over_time > 8 ):
            clear()
            game_framework.change_state(title_state)
        pass

    @staticmethod
    def draw(tutorial):
        tutorial.Tutorial_Map.clip_draw(250, 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        tutorial.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80) # 보드판
        tutorial.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        tutorial.time_bar_image.clip_draw(0, 0, 300, 60, 1230, 30) #스테이지 타임바
        tutorial.time_bar_image.clip_draw_to_origin(0, 60, 300 - tutorial.time_bar, 60, 1080,1)
        if(tutorial.Click_order == 0): # 화살표
            tutorial.arrow.clip_composite_draw(0, 0, 80, 80, 3.141592 / 2, '', 140, int(tutorial.arrow_y), 80, 80)
            tutorial.font.draw(80, 460 - 100, 'Click here!' ,(255, 255, 0))
        if (tutorial.Click_order == 2):# 화살표
            tutorial.arrow.clip_composite_draw(0, 0, 80, 80, -3.141592 / 2, '', 210, int(tutorial.arrow_y), 80, 80)
            tutorial.font.draw(150, 340 + 100, 'Click here!', (255, 255, 0)) # 튜토리얼 화살표와 누르라는 명령
        if (tutorial.Click_order == 4):
            tutorial.arrow.clip_composite_draw(0, 0, 80, 80,   0, '',int(tutorial.arrow_y - 100) , int(Sun[0].y), 80, 80)
            tutorial.font.draw(Sun[0].x -350, Sun[0].y , 'Click here!', (255, 255, 0))  # 튜토리얼 화살표와 누르라는 명령
            tutorial.font.draw(600 , 50 , "you can get the money ^^",(255 ,0,0))  # 튜토리얼 화살표와 누르라는 명령
        Plants_Card.draw_card(tutorial.select_card, tutorial.mouse_x, tutorial.mouse_y)
        tutorial.font.draw(20, 530, '%d' % tutorial.sun_value)
        if (tutorial.timer - tutorial.stage_time <= 2 and tutorial.order == 0):
            tutorial.Tutorial_Start_logo.draw(700, 300)

        #게임 오버
        if(tutorial.game_over > 0):

            tutorial.font.draw(600 , 550 , 'GAME OVER.....', (0 , 150, 0))


next_state_table = {
    Start_state : {SHOW_HOUSE : Start_state , SHOW_MAP:Move_state ,START : Stage_state },
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
        self.arrow = load_image('Tutorial/Tutorial_arrow.png')
        self.time_bar_image = load_image('Tutorial/progress_bar.png')
        self.ZombiescomingSound = load_wav('Gamesoundeffect/Zombiescoming.wav')
        self.getpoint = load_wav('Gamesoundeffect/points.ogg')
        self.getpoint.set_volume(64)
        self.pausego = load_wav('Gamesoundeffect/pause.wav')
        self.pausego.set_volume(64)

        self.Planting_plant = load_wav('Gamesoundeffect/plant1.wav')
        self.Planting_plant.set_volume(64)
        self.ZombiescomingSound.set_volume(64)
        self.zombiecome = False

        self.splat = load_wav('Gamesoundeffect/splat1.wav')
        self.splat.set_volume(64)


        self.shoot = load_wav('Gamesoundeffect/Shoot.ogg')
        self.shoot.set_volume(64)

        self.buttonclick = load_wav('Gamesoundeffect/buttonclick.ogg')
        self.buttonclick.set_volume(64)

        self.game_over_sound = load_wav('Gamesoundeffect/scream.ogg')
        self.game_over_sound.set_volume(64)
        self.time_bar = 0
        self.intro_music.set_volume(32)  # 스테이지 들어오면 음악이 바로 재생되게함
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
        self.Click_order = 0
        self.game_over =0
        self.plant_setting = 0 # 식물 못 겹치게 하기
        self.count = []
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
                self.buttonclick.play()
                self.sun_value = self.sun_value - 100
                if(self.Click_order == 0):
                    self.Click_order = 1
                pass
            elif (event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1300 and event.y < 339 and event.y > 255 and self.select_card > 0):
                # 여기서부턴 튜토리얼 대지 영역
                count = False
                for i in range(9):
                    self.plant_setting += 1
                    if (event.x >= i * 140 and event.x <= i * 140 + 140): #가운데 라인 생성
                        global Plant_Count
                        for j in range(len(self.count)):
                            if(self.count[j] == self.plant_setting):
                                self.plant_setting = 0
                                count = True
                                break

                        if(count == False):
                            if (self.Click_order < 3):
                                self.Click_order = 3  # 튜토리얼 표지판 때문에 생성
                            self.count.append(self.plant_setting)
                            creat_Plants(int(i * 140 + 70), int(282), 2 , self.plant_setting)
                            self.select_card = 0
                            self.plant_setting = 0
                            self.Planting_plant.play()
                            break
                self.plant_setting = 0
            elif (event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1400 and event.y >= 0 and event.y <= 600):
                global Sun_Count , Sun
                for Sun_shine in Sun:

                    if (event.x > Sun_shine.x - 50 and event.x < Sun_shine.x + 50 and 600 - event.y - 1 > Sun_shine.y - 50 and 600 - event.y - 1 < Sun_shine.y + 50):

                        self.Click_order = 5
                        Sun_shine.click = 1
                        Sun_shine.plus_x = Sun_shine.x# 좌표를 보내줌
                        Sun_shine.plus_y = Sun_shine.y
                        self.getpoint.play()
                        del Sun_shine  # 누르면 삭제

                        Sun_Count -= 1 # 자원의 개수를 줄여줌

                        self.sun_value = self.sun_value + 30  # 자원 증가
                        break
            if (event.button == SDL_BUTTON_RIGHT and self.select_card > 0):
                self.select_card = 0  # 오른쪽 버튼을 누르면 초기화
                self.sun_value = self.sun_value + 100

        # 마우스 모션
        if (self.cur_state == Stage_state
                and event.type == SDL_MOUSEMOTION):
            self.mouse_x =  event.x
            self.mouse_y = event.y

        if(event.type == SDL_KEYDOWN):
            if(event.key == SDLK_1):
                clear()
                game_framework.change_state(Stage1_state)
            if(event.key == SDLK_2):
                self.add_event(START)
            if(event.key == SDLK_3):
                global Zombies
                Zombies[0].x = 100

