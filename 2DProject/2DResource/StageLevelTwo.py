import game_framework
from pico2d import *
from Zombies import Zombie
from Zombies import Buket_Zombie
from Zombies import Cone_Zombie
from Zombies import Helmet_Zombie
from Plants import plant
from Plants import Flower
from Plants import walnut
from Plants import cherryboom
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


# Stage1 이벤트
SHOW_HOUSE, SHOW_MAP, SHOW_ZOMBIE, RETURN_MAP, START  = range(5)

next_state_table = {
(SDL_KEYDOWN, SDLK_1): SHOW_MAP,
(SDL_KEYDOWN,SDLK_2) : START


}
Plants_Card = None
Plants_Card2 = None
Plants_Card3 = None
Zombies = []
Plants = []
Flowers = []
Walnuts = []
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
    new_zombie.Line = random.randint(0 , 4)
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count +1
def creat_Buket_Zombie(): #뚜껑 좀비 생산
    global Zombies, Zombie_Count
    new_zombie = Buket_Zombie()
    new_zombie.Line = random.randint(0, 4)
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count + 1
def creat_Cone_Zombie(): # 콘 좀비 생산
    global Zombies, Zombie_Count
    new_zombie = Cone_Zombie()
    new_zombie.Line = random.randint(0, 4)
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count + 1
def creat_Helmet_Zombie():
    global Zombies, Zombie_Count
    new_zombie = Helmet_Zombie()
    new_zombie.Line = random.randint(0, 4)
    game_world.add_object(new_zombie, 1)
    Zombies.append(new_zombie)
    Zombie_Count = Zombie_Count + 1
#좀비 생산
def creat_Plant_card():
    global Plants_Card
    global Plants_Card2
    global Plants_Card3
    Plants_Card = plant(0 , 0, 0 , 0)
    Plants_Card2 = Flower(0, 0, 0 , 0)
    Plants_Card3 =  walnut(0,0,0 , 0)
#식물을 눌렀을때 생산
def creat_Plants( x, y , Line_, select  ,sitting):
    global Plants , Plant_Count
    if(select == 1):
        new_plant = plant(x, y , Line_ , sitting)
        game_world.add_object(new_plant, 1)
        Plants.append(new_plant)
        Plant_Count = Plant_Count + 1
    if(select == 2):
        new_plant = Flower(x, y, Line_ , sitting)
        game_world.add_object(new_plant, 1)
        Flowers.append(new_plant)
        Plant_Count = Plant_Count + 1
    if(select == 3):
        new_plant = walnut(x, y, Line_ , sitting)
        game_world.add_object(new_plant, 1)
        Walnuts.append(new_plant)
        Plant_Count = Plant_Count + 1
    #식물 생산

def creat_Sun():
    global Sun , Sun_Count
    new_Sun = Sun_shine()

    Sun.append(new_Sun)
    game_world.add_object(new_Sun, 1)

    Sun_Count += 1
def Flower_creat_Sun(x_ , y_):
    global Sun, Sun_Count
    new_Sun = Sun_shine()
    new_Sun.x = x_
    new_Sun.y = y_ + 20
    new_Sun.limit_y = y_ - 10
    Sun.append(new_Sun)
    game_world.add_object(new_Sun, 1)

    Sun_Count += 1
    pass
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
def Collide_check(stageleveltwo): # 충돌체크 편하기 위해 만듬
    global Zombies , Plants , Bullets
    global Plant_Count

    for Zombie in Zombies:
        for Bullet in Bullets:
            if collide(Bullet, Zombie) and Bullet.state == 0 and Zombie.hp > 0 and Zombie.state != 3 and Zombie.state != 4 and  Zombie.state !=5:
                stageleveltwo.splat.play()
                Zombie.hp -=  1
                Bullet.state = 1 # 총알을 없에준다
                break

    for plant in Plants:
         #지금 식물에 대한 상태값을 위해 지금 식물이 맞고 있는중인지 아닌지
        for Zombie in Zombies: #좀비가 충돌이 아닌상태라면 상태를 바꿔줘야한다.
            if collide(plant, Zombie) and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5:
                Zombie.state = 2
                Zombie.collide = True
                plant.state = 3

            elif (Zombie.collide != True  and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5):
                Zombie.state = 1
            else:
                plant.state = 0

    #Flower하고도 체크
    for Flower in Flowers:
        # 지금 식물에 대한 상태값을 위해 지금 식물이 맞고 있는중인지 아닌지
        for Zombie in Zombies:  # 좀비가 충돌이 아닌상태라면 상태를 바꿔줘야한다.
            if collide(Flower, Zombie) and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5:
                Zombie.state = 2
                Zombie.collide = True
                Flower.state = 3

            elif (Zombie.collide != True and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5):
                Zombie.state = 1
            else:
                Flower.state = 1
    for walnut in Walnuts:
            # 지금 식물에 대한 상태값을 위해 지금 식물이 맞고 있는중인지 아닌지
        for Zombie in Zombies:  # 좀비가 충돌이 아닌상태라면 상태를 바꿔줘야한다.
            if collide(walnut, Zombie) and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5:

                Zombie.state = 2
                Zombie.collide = True
                walnut.state = 3

            elif (Zombie.collide != True and Zombie.state != 3 and Zombie.state != 4 and Zombie.state != 5):
                Zombie.state = 1
            else:
                walnut.state = 0
        #   if(plant_hited != True): #지금 식물이 맞고 있는 중이 아니라면?
        #   plant.state = 1

    for Zombie in Zombies: # 모든 좀비에 대하여
        Zombie.collide = False
        if(Plant_Count == 0  and Zombie.state != 3 and Zombie.state != 4 and  Zombie.state != 5): # 모든 좀비가 죽은 상태가 아니고 식물 숫자가 0이라면
            Zombie.state = 1 #좀비의 상태는 워킹

    for Bullet in Bullets:
        if(Bullet.action > 20 and Bullet.state == 1):
            Bullet.state = 2

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


#객체들이 경우에 따라서 삭제됨

def clear(): #객체 리스트 다 삭제
    global Zombies, Plants, Bullets , Sun , Flowers , Walnuts
    global Zombie_Count
    global Plant_Count
    global Bullet_Count
    global Sun_Count
    del Zombies
    del Plants
    del Bullets
    del Sun
    del Flowers
    del Walnuts
    Zombies = []
    Plants = []
    Sun = []
    Bullets = []  # 객체 리스트
    Flowers = []
    Walnuts = []
    Plant_Count =0
    Zombie_Count =0
    Bullet_Count=0
    Sun_Count = 0
#객체 리스트 다 삭제

class Start_state:
    @staticmethod
    def enter(stageleveltwo ,event):
        stageleveltwo.frame = 0
        stageleveltwo.start_time = get_time()


    @staticmethod
    def exit(stageleveltwo , event):


        pass
    @staticmethod
    def do(stageleveltwo):
        if (stageleveltwo.timer - stageleveltwo.start_time >= 2):
            stageleveltwo.add_event(SHOW_MAP)

    @staticmethod
    def draw(stageleveltwo):
        stageleveltwo.stageleveltwo_map.clip_draw(0 + stageleveltwo.frame, 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        stageleveltwo.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        stageleveltwo.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        stageleveltwo.Impa.draw(600, 560)
        stageleveltwo.cards.clip_draw(62, 485, 70, 90, 210, 560, 64, 70)
        stageleveltwo.cards.clip_draw(191, 485, 70, 90, 280, 560, 64, 70)
        stageleveltwo.font.draw(28, 532, '%d' % stageleveltwo.sun_value)
        stageleveltwo.font.draw(600, 50, 'Stage Level Two')
class Move_state:
    global Zombies , Zombie_Count
    @staticmethod

    def enter(stageleveltwo , event):
        stageleveltwo.frame = 0
        stageleveltwo.move_time = get_time()
        stageleveltwo.velocity += CHANGE_SPEED_PPS
        stageleveltwo.map_x = 0
        stageleveltwo.re = 0
        stageleveltwo.Move_timer = 0  # 무브 타임

        for i in range(2): # 2마리 씩 생산
            creat_Zombie()
            creat_Buket_Zombie()
            creat_Cone_Zombie()
            creat_Helmet_Zombie()

        for Zombie  in Zombies:

            Zombie.x += random.randint(100, 200)
        for Buket_Zombie in Zombies:
            Buket_Zombie.x += random.randint(100, 200)
    @staticmethod
    def exit(stageleveltwo,event):
        for Zombie in Zombies:
            Zombie.state = 1;
            Zombie.y = 300
            Zombie.x = 1500
    @staticmethod
    def do(stageleveltwo):
        if (stageleveltwo.map_x < 500):  # 좀비가 나타나야할 시간 300
            if (stageleveltwo.re == 0):
                stageleveltwo.map_x += stageleveltwo.velocity * game_framework.frame_time  # 속도 * 시간
                for Zombie in Zombies:
                    Zombie.x -= (stageleveltwo.velocity * game_framework.frame_time) * 1.7
                if (stageleveltwo.map_x > 500):
                    stageleveltwo.re = 1

        if(stageleveltwo.re == 1):
            stageleveltwo.Move_timer += 1

            if (stageleveltwo.Move_timer == 150):
                stageleveltwo.Move_timer = 0
                stageleveltwo.re = 2
        if (stageleveltwo.re == 2):
            if (stageleveltwo.map_x > 0):
                stageleveltwo.map_x -= stageleveltwo.velocity * game_framework.frame_time  # 속도 * 시간
                for Zombie in Zombies:
                    Zombie.x += (stageleveltwo.velocity * game_framework.frame_time) * 1.7  # 좀비야 멈춰라
                if (stageleveltwo.map_x < 330):  # 맵을 원위치로
                    stageleveltwo.Move_timer += 1
                    if (stageleveltwo.Move_timer == 150):
                        stageleveltwo.add_event(START)
    @staticmethod
    def draw(stageleveltwo):
        stageleveltwo.stageleveltwo_map.clip_draw(int(stageleveltwo.map_x), 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        stageleveltwo.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)
        stageleveltwo.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        stageleveltwo.Impa.draw(600, 560)
        stageleveltwo.cards.clip_draw(62, 485, 70, 90, 210, 560, 64, 70)
        stageleveltwo.cards.clip_draw(191, 485, 70, 90, 280, 560, 64, 70)
        stageleveltwo.font.draw(28, 532, '%d' % stageleveltwo.sun_value)
        stageleveltwo.font.draw(600, 50, 'Defence the Zombies!!', (255, 0, 0))

class Stage_state:
    global Plants , Plant_Count
    @staticmethod
    def enter(stageleveltwo , event):
        creat_Plant_card()
        stageleveltwo.frame = 0
        stageleveltwo.stage_time = get_time()
        stageleveltwo.time_bar_time = get_time()
        stageleveltwo.order = 0
        stageleveltwo.stageleveltwo_Start_music.set_volume(32)
        stageleveltwo.stageleveltwo_Start_music.play()
        stageleveltwo.velocity += CHANGE_SPEED_PPS
        stageleveltwo.game_over_time = 0
        for i in range(5): # 24 마리
            creat_Zombie()
            creat_Buket_Zombie()
            creat_Cone_Zombie()
            creat_Helmet_Zombie()
        creat_Helmet_Zombie()
        for Zombie in Zombies:
            Zombie.state = 1
            Zombie.x = 1600

            Zombie.frame = random.randint(0 , 10)

        for i in range(Zombie_Count):
            Zombies[i].x += i * random.randint(100, 400) # 좀비들 거리 띄어줌
        #처음에 생산한 좀비들을 처리

    @staticmethod
    def exit(stageleveltwo , event):
        pass
    @staticmethod
    def do(stageleveltwo):
        if (stageleveltwo.timer - stageleveltwo.stage_time >= 2 and stageleveltwo.order == 0):
            stageleveltwo.stageleveltwo_GAME_START.set_volume(32)
            stageleveltwo.stageleveltwo_GAME_START.repeat_play()
            stageleveltwo.order = 1
        if stageleveltwo.zombiecome == False:
            if (Zombies[0].x < 1500):
                stageleveltwo.ZombiescomingSound.play()
                stageleveltwo.zombiecome = True
        if stageleveltwo.order >= 0:
            if (stageleveltwo.timer - stageleveltwo.stage_time > 5):
                stageleveltwo.stage_time = get_time()  # 20초 마다 자원이 나오게함
                creat_Sun()
        # 식물과 좀비 상호작용
        for plant in Plants:
            Zombie_line = False
            for i in range(Zombie_Count):
                if ((plant.Line == Zombies[i].Line) and Zombies[i].x < 1400 and Zombies[i].state != 4):
                     #라인이 같고 1400 이하일때 쏜다 . 라인이 같은 좀비가 없다면
                    plant.state = 2
                    Zombie_line = True
                if(((plant.Line != Zombies[i].Line) or Zombies[i].x > 1400) and Zombie_line != True):
                    plant.state = 1
            if(Zombie_Count == 0):
                plant.state = 1
        for plant in Plants:
            if(plant.state == 2):
                if stageleveltwo.timer - plant.state_time > 5:
                    stageleveltwo.shoot.play()
                    creat_Bullet(plant.x , plant.y + 30)
                    plant.state_time = get_time()

        #Flower 객체의 자원생성
        for Flower in Flowers:
            if(Flower.state == 1):
                if stageleveltwo.timer - Flower.Sun_time > 20:
                    Flower_creat_Sun(Flower.x , Flower.y)
                    Flower.Sun_time = get_time()

        #타임바 해줘야함
        if(stageleveltwo.timer - stageleveltwo.time_bar_time >= 1):
            if(stageleveltwo.time_bar <= 300):
                stageleveltwo.time_bar = (28 - Zombie_Count) * 11  #시간바의 이동속도

                stageleveltwo.time_bar_time = get_time() # 아래 게임 시간 바를 그려주는것

        Collide_check(stageleveltwo) #객체들의 충돌 체크
        global Plant_Count
        for plant in Plants:
            if (plant.state == 3 and plant.hp <= 0):
                for i in range(len(stageleveltwo.count)):
                    if (plant.sitting == stageleveltwo.count[i]):
                        stageleveltwo.count.remove(plant.sitting)
                        game_world.remove_object(plant)
                        Plants.remove(plant)

                        Plant_Count = Plant_Count - 1
                        break

                break
        # Flower 충돌 체크
        for Flower in Flowers:

            if (Flower.state == 3 and Flower.hp <= 0):
                for i in range(len(stageleveltwo.count)):
                    if (Flower.sitting == stageleveltwo.count[i]):
                        stageleveltwo.count.remove(Flower.sitting)
                        game_world.remove_object(Flower)
                        Flowers.remove(Flower)
                        Plant_Count = Plant_Count - 1
                        break



                break

        for walnut in Walnuts:

            if (walnut.state == 3 and walnut.hp <= 0):
                for i in range(len(stageleveltwo.count)):
                    if (walnut.sitting == stageleveltwo.count[i]):
                        stageleveltwo.count.remove(walnut.sitting)
                        game_world.remove_object(walnut)
                        Walnuts.remove(walnut)

                        Plant_Count = Plant_Count - 1
                        break

                break
        Delete_all() # 객체들의 삭제
        if (stageleveltwo.game_over == 0):
            for Zombie in Zombies:
                if (Zombie.x < 0):
                    stageleveltwo.game_over = 1
                    stageleveltwo.game_over_sound.play()

        if (stageleveltwo.game_over == 1):
            stageleveltwo.game_over_time = get_time()
            stageleveltwo.game_over = 2


        # 다음 스테이지로 넘어감 스테이지 클리어
        if(Zombie_Count == 0 and stageleveltwo.win == 0): # 스테이지 넘어가는 조건

            stageleveltwo.wintime = get_time()
            stageleveltwo.win = 1
            stageleveltwo.stageleveltwo_GAME_START.pause()
            stageleveltwo.winsound.play()
        if stageleveltwo.win == 1 and stageleveltwo.timer - stageleveltwo.wintime > 5:
            stageleveltwo.win = 2

        if stageleveltwo.win == 2:
            clear()
            game_framework.change_state(title_state)
        if (stageleveltwo.game_over == 2 and stageleveltwo.timer - stageleveltwo.game_over_time > 8):

            clear()
            game_framework.change_state(title_state)

    @staticmethod
    def draw(stageleveltwo):
        stageleveltwo.stageleveltwo_map.clip_draw(250, 0, 800, 600, 700, 300, 1400, 600)  # 맵을 그려줌
        stageleveltwo.board.clip_draw(0, 0, 557, 109, 280, 560, 557, 80)  # 보드판
        stageleveltwo.cards.clip_draw(0, 485, 64, 90, 140, 560, 64, 70)  # 카드
        stageleveltwo.Impa.draw(600, 560)
        stageleveltwo.cards.clip_draw(62, 485, 70, 90, 210, 560, 64, 70)
        stageleveltwo.cards.clip_draw(191, 485, 70, 90, 280, 560, 64, 70)
        Plants_Card.draw_card(stageleveltwo.select_card, stageleveltwo.mouse_x, stageleveltwo.mouse_y)
        Plants_Card2.draw_card(stageleveltwo.select_card, stageleveltwo.mouse_x, stageleveltwo.mouse_y)
        Plants_Card3.draw_card(stageleveltwo.select_card, stageleveltwo.mouse_x, stageleveltwo.mouse_y)
        stageleveltwo.font.draw(28, 532, '%d' % stageleveltwo.sun_value)
        stageleveltwo.time_bar_image.clip_draw(0, 0, 300, 60, 1230, 30) #스테이지 타임바
        stageleveltwo.time_bar_image.clip_draw_to_origin(0, 60, 300 - stageleveltwo.time_bar, 60, 1080,1)
        if (stageleveltwo.game_over > 0):
            stageleveltwo.font.draw(600, 550, 'GAME OVER.....', (0, 150, 0))
        if(stageleveltwo.win > 0):
            stageleveltwo.font.draw(600, 550, 'YOU WIN!! ALL CLEAR', (150, 0, 0))
#박스 그리기

next_state_table = {
    Start_state : {SHOW_HOUSE : Start_state , SHOW_MAP:Move_state ,START : Stage_state },
    Move_state : {SHOW_MAP: Move_state , START : Stage_state},
    Stage_state : {START : Stage_state  }
}
class stageleveltwo:
    stageleveltwo_map = None
    board = None
    stageleveltwo_GAME_START = None
    stageleveltwo_Start_logo =  None
    cards = None
    time_bar_image = None
    def __init__(self):
        if (self.stageleveltwo_map == None ):
            self.stageleveltwo_map = load_image('Stageleveltwo/Stagelevel2map.png')
        if (self.board == None):
             self.board = load_image('Stage1/board.png')

        self.intro_music = load_music('Stage1/intro_music.mp3')

        self.stageleveltwo_Start_music = load_music('Stage1/Tutorial_start.mp3')  # 초반 도입 음악
        self.stageleveltwo_GAME_START = load_music('Stageleveltwo/Stagelevel2music.mp3')  # 게임 스타트 음악
        self.font = load_font('Stage1/ConsolaMalgun.ttf', 25)
        self.Impa = load_image('Tutorial/lampa.png')
        if(self.stageleveltwo_Start_logo == None):
            self.stageleveltwo_Start_logo = load_image('Stage1/Turtorial_Start.png')
        if (self.cards == None ):
            self.cards = load_image('Stage1/cards.png')
        if (self.time_bar_image == None ):
            self.time_bar_image = load_image('Stage1/progress_bar.png')
        self.ZombiescomingSound = load_wav('Gamesoundeffect/Zombiescoming.wav')
        self.ZombiescomingSound.set_volume(64)
        self.zombiecome = False
        self.time_bar = 0
        self.Planting_plant = load_wav('Gamesoundeffect/plant1.wav')
        self.Planting_plant.set_volume(64)
        self.getpoint = load_wav('Gamesoundeffect/points.ogg')
        self.getpoint.set_volume(64)
        self.pausego = load_wav('Gamesoundeffect/pause.wav')
        self.pausego.set_volume(64)
        self.splat = load_wav('Gamesoundeffect/splat1.wav')
        self.splat.set_volume(64)
        self.shoot = load_wav('Gamesoundeffect/Shoot.ogg')
        self.shoot.set_volume(64)
        self.buttonclick = load_wav('Gamesoundeffect/buttonclick.ogg')
        self.buttonclick.set_volume(64)

        self.game_over_sound = load_wav('Gamesoundeffect/scream.ogg')
        self.game_over_sound.set_volume(64)

        self.intro_music.set_volume(32)  # 스테이지 들어오면 음악이 바로 재생되게함
        self.intro_music.repeat_play()

        self.win = 0
        self.wintime = 0
        self.winsound = load_wav('Gamesoundeffect/winmusic.ogg')
        self.winsound.set_volume(64)

        self.velocity = 0
        self.event_que = [] #이벤트 큐
        self.frame = 0  # 화면을 옮겨주는 프레임
        self.cur_state = Start_state  # 화면을 옮겨주는 순서 정의
        self.cur_state.enter(self, None)
        # 화면 정지 시간
        self.str = "우리들의 집"  # 글자 출력
        self.sun_value = 500  # 자원량
        self.select_card = 0  # 무슨 카드를 선택했는지 아는 변수
        self.timer = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.game_over =0 # 게엠 오버 확인
        self.plant_setting = 0 # 식물 못 겹치게 하기
        self.count = [] # 식물 중복 금지
        self.what_plants = [] # 어떤 식물을 넣었는지 알게하기
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
        check = True
        if(self.cur_state == Stage_state
        and event.type == SDL_MOUSEBUTTONDOWN): #마우스 버튼 다운시
            # 자원을 얻는것
            if (event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1400 and event.y >= 0 and event.y <= 600):
                global Sun_Count , Sun
                for Sun_shine in Sun:

                    if (event.x > Sun_shine.x - 50 and event.x < Sun_shine.x + 50 and 600 - event.y - 1 > Sun_shine.y - 50 and 600 - event.y - 1 < Sun_shine.y + 50):

                        self.Click_order = 5
                        Sun_shine.click = 1
                        Sun_shine.plus_x = Sun_shine.x# 좌표를 보내줌
                        Sun_shine.plus_y = Sun_shine.y
                        self.getpoint.play()
                        Sun.remove(Sun_shine)
                        check = False
                        Sun_Count -= 1 # 자원의 개수를 줄여줌

                        self.sun_value = self.sun_value + 30  # 자원 증가
                        break
            if (event.button == SDL_BUTTON_LEFT and event.x > 600 - 50 and event.x < 600 + 50 and 0 + 600 - event.y - 1 < 0 + 600 and 0 + 600 - event.y - 1 > 0 + 600 - 80 and self.select_card == 0 and check == True):
                  self.select_card = 10  # 삽
            #카드 고르기
            if (event.button == SDL_BUTTON_LEFT and event.x > 100 and event.x < 180 and 0 +600 - event.y - 1 < 0 +600 and 0 +600 - event.y - 1 > 0 +600 - 80 and self.sun_value >= 100 and self.select_card == 0):
                self.select_card = 1
                self.sun_value = self.sun_value - 100
                self.buttonclick.play()
                pass
            elif (event.button == SDL_BUTTON_LEFT and event.x > 180 and event.x < 260 and 0 +600 - event.y - 1 < 0 +600 and 0 +600 - event.y - 1 > 0 +600 - 80 and self.sun_value >= 50 and self.select_card == 0):
                self.select_card = 2
                self.sun_value = self.sun_value - 50
                self.buttonclick.play()
            elif (event.button == SDL_BUTTON_LEFT and event.x > 260 and event.x < 340 and 0 + 600 - event.y - 1 < 0 + 600 and 0 + 600 - event.y - 1 > 0 + 600 - 80 and self.sun_value >= 50 and self.select_card == 0):
                self.select_card = 3 #walnut
                self.sun_value = self.sun_value - 50
                self.buttonclick.play()

            elif (event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1300 and 0 +600 - event.y - 1 < 600 and 0 +600 - event.y > 0 and self.select_card > 0):
                # 여기서부턴 튜토리얼 대지 영역
                count = False
                for i in range(-1, 4):  # y  값
                    if (count == True):
                        break
                    for j in range(9):  # x 값
                        self.plant_setting += 1
                        if (event.x >= j * 140 and event.x <= j * 140 + 140 and 600 - event.y - 1 > (
                        i) * 100 + 30 and 600 - event.y - 1 <= (i + 1) * 100 + 130):  # 가운데 라인 생성
                            global Plant_Count
                            for k in range(len(self.count)):
                                if (self.plant_setting == self.count[k]):
                                    if (self.select_card == 10):
                                        for plant in Plants:
                                            if (plant.sitting == self.count[k]):
                                                self.count.remove(plant.sitting)
                                                Plants.remove(plant)
                                                Plant_Count -= 1
                                                game_world.remove_object(plant)
                                                self.select_card = 0
                                                self.Planting_plant.play()
                                                break
                                        for Flower in Flowers:
                                            if (Flower.sitting == self.count[k]):
                                                self.count.remove(Flower.sitting)
                                                Flowers.remove(Flower)
                                                Plant_Count -= 1
                                                game_world.remove_object(Flower)
                                                self.select_card = 0
                                                self.Planting_plant.play()
                                                break
                                        for walnut in Walnuts:
                                            if (walnut.sitting == self.count[k]):
                                                self.count.remove(walnut.sitting)
                                                Walnuts.remove(walnut)
                                                Plant_Count -= 1
                                                game_world.remove_object(walnut)
                                                self.select_card = 0
                                                self.Planting_plant.play()
                                                break

                                    count = True
                                    self.plant_setting = 0
                                    break
                            if (count == False and self.select_card != 10):
                                creat_Plants(int(j * 140 + 70), i + 1, i + 1, self.select_card , self.plant_setting)
                                self.select_card = 0
                                self.count.append(self.plant_setting)
                                self.Planting_plant.play()
                                self.plant_setting = 0
                                print(i)
                                count = True
                                break
                self.plant_setting = 0


            #카드 선택 해제
            if (event.button == SDL_BUTTON_RIGHT and self.select_card > 0):
                if(self.select_card == 1):
                    self.sun_value = self.sun_value + 100
                elif(self.select_card == 2 or self.select_card == 3):
                    self.sun_value = self.sun_value + 50
                self.select_card = 0  # 오른쪽 버튼을 누르면 초기화



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
            if(event.key == SDLK_3):
                global Zombies  , Zombie_Count
                Zombies[0].x = 100
            if (event.key == SDLK_4):
                Zombie_Count = 0
