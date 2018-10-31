import game_framework
from Plants import *
from Zombies import *
from pico2d import*
from Sun import*

name = "Tutorial"
tutorial = None
game_menu = None
Zombies = None
Sun = None
Plants = None
Plants_Card = None
current_time = 0
Sun_Count , Plant_Count  , Zombie_Count = 0 , 0 , 0
mouse_x = 0
mouse_y = 0
class Tutorial:

    def __init__(self):
        self.Tutorial_Map = load_image('Tutorial/Tutorial_map.png')
        self.board = load_image('Tutorial/board.png')
        self.Main_object_esc = load_image('Mainresource/areyousure.png')
        self.intro_music = load_music('Tutorial/intro_music.mp3')
        self.Tutorial_Start = load_music('Tutorial/Tutorial_start.mp3') # 초반 도입 음악
        self.Tutorial_GAME_START = load_music('Tutorial/Tutorial_GAME_START.mp3') # 게임 스타트 음악
        self.font = load_font('Tutorial/ConsolaMalgun.ttf', 30)
        self.Tutorial_Start_logo = load_image('Tutorial/Turtorial_Start.png')
        self.cards = load_image('Tutorial/cards.png')
        self.intro_music.set_volume(64)
        self.intro_music.repeat_play()
        self.frame = 0 # 화면을 옮겨주는 프레임
        self.order = 0 # frame을 움직여야할 상태값
        self.idle_time = 0 # 화면 정지 시간
        self.str = "우리들의 집" # 글자 출력
        self.sun_value = 200 # 자원량
        self.select_card = 0 #무슨 카드를 선택했는지 아는 변수

        #self.arrow('Tutorial/arrow.png')
        pass
    def handle_events(self):
        global game_menu
        global mouse_x , mouse_y
        global Plant_Count , Sun_Count
        events = get_events()
        for event in events:

            if (event.type == SDL_QUIT or event.key == SDLK_ESCAPE):  # 게임 나가기
                game_menu = True
            if(event.type == SDL_MOUSEMOTION): #마우스 좌표 받음
                mouse_x = event.x
                mouse_y = event.y  # 게임 시작
            elif (event.type == SDL_MOUSEBUTTONDOWN):
                GAME_HEIGHT = 600

                if (event.x < 674  and event.x > 490 and GAME_HEIGHT - event.y - 1 < (GAME_HEIGHT // 4 + 20) + 40 and GAME_HEIGHT - event.y - 1 > (GAME_HEIGHT // 4 + 20) - 40 and game_menu == True):
                    game_framework.quit()

                elif (event.x < 895 and event.x > 711 and GAME_HEIGHT - event.y - 1 < (GAME_HEIGHT // 4 + 20) + 40 and GAME_HEIGHT - event.y - 1 > (GAME_HEIGHT // 4 + 20) - 40 and game_menu == True):
                    game_menu = False

                elif(event.button == SDL_BUTTON_LEFT and event.x > 100 and event.x < 180 and GAME_HEIGHT - event.y - 1 <  GAME_HEIGHT and GAME_HEIGHT - event.y - 1 >  GAME_HEIGHT - 80 and self.sun_value >= 100):
                    self.select_card = 1
                    self.sun_value  = self.sun_value - 100
                elif(event.button == SDL_BUTTON_RIGHT):
                    self.select_card = 0 # 오른쪽 버튼을 누르면 초기화
                    self.sun_value = self.sun_value + 100
                elif(event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1300 and event.y < 339 and event.y > 255 and self.select_card > 0):
                    #여기서부턴 튜토리얼 대지 영역
                    for i in range(9):
                        if(event.x >= i * 140 and event.x <=  i* 140 + 140):
                            creat_plant()
                            Plants[Plant_Count].x = int(i * 140 + 70)
                            Plants[Plant_Count].y = int(277)
                            Plant_Count = Plant_Count + 1
                            self.select_card = 0
                            break
                elif(event.button == SDL_BUTTON_LEFT and event.x >= 0 and event.x <= 1400 and event.y >= 0 and event.y <= 600):

                    for i in range(Sun_Count):
                        print(i)
                        if(event.x > Sun[i].x - 50 and event.x < Sun[i].x + 50  and GAME_HEIGHT - event.y - 1 > Sun[i].y -50 and GAME_HEIGHT - event.y - 1 < Sun[i].y + 50  ):
                            del Sun[i]  # 자원을 클릭 하면 삭제 해줌
                            Sun_Count = Sun_Count - 1 # 자원의 개수 빼준다 .
                            self.sun_value = self.sun_value + 30 # 자원 증가
                            break










    def draw(self):
        global mouse_x, mouse_y
        clear_canvas()
        #처음 시작시는 0 으로 바꿔줌 # 700 까지 올려주고 다시 200으로 내려줌
        #글자 써줘야함
        #200 # 800  게임 시작시
        #도로에 좀비들을 아이들 상태로 그려줘야함

        self.Tutorial_Map.clip_draw(0 + self.frame, 0 , 800 , 600 , 700 , 300, 1400, 600 ) #맵을 그려줌
        self.board.clip_draw(0 , 0 ,557 , 109  , 280, 560 ,  557 , 80) #보드판
        self.font.draw(20, 530, '%d' % self.sun_value) # 가지고 있는 돈의 값
        self.cards.clip_draw(0 , 485 , 64, 90 , 140 , 560 , 64, 70) # 카드
        if(game_menu == True):
            self.Main_object_esc.draw(1400//2 ,600//2, 510, 380 )
        if(self.order < 4):
            self.font.draw(600, 50, 'My house...')
        if(self.order == 4):
            self.Tutorial_Start_logo.draw(700, 300)

        # 식물을 위치시킬 곳을 그려줌
        for i in range (9):
            draw_rectangle(i * 140 , 330 , i* 140 + 140 , 225) # 상자 평균적인 위치
        #draw_rectangle(0 , 330 , 150 , 225) # 150
        #draw_rectangle(150, 330,280, 225)  # 130
        # draw_rectangle(280, 330,440, 225)  # 160
        #draw_rectangle(440, 330, 580, 225) # 140
        #draw_rectangle(580, 330, 710, 225) # 130
        # draw_rectangle(710, 330, 860, 225) # 150
        #draw_rectangle(860, 330, 990, 225)# 140
        #draw_rectangle(990, 330, 1140, 225) # 150
        # draw_rectangle(1140, 330,1300, 225) # 160

        Plants_Card.draw_card(self.select_card , mouse_x , mouse_y)

        for Zombie in Zombies: #리스트에 있는 좀비들을 그려준다

            Zombie.draw(self.order)
        for plant in Plants:
            plant.draw()
        for Sun_shine in Sun:
            Sun_shine.draw()
        update_canvas()
        delay(0.02)


    def update(self):
        global current_time
        global Zombie_Count
        global Zombies
        for Zombie in Zombies:
            Zombie.update() # 좀비 프레임 업데이트
        for plant in Plants:
            plant.update()
        for Sun_shine in Sun:
            Sun_shine.update()
        if(self.idle_time >= 50 and self.order == 0): # 처음에 좀비 어떤 종류인지 알려줌
            self.order = 1

        if(self.order == 0):
            self.idle_time = self.idle_time + 1

        elif(self.order == 1):
            self.frame = self.frame + 3
            if(self.frame >= 600):
                self.order = 2

        elif (self.order == 2):

            if(self.idle_time > 100):

                self.order = 3
            self.idle_time = self.idle_time + 1
        elif(self.order == 3):
            self.frame = self.frame - 2
            if(self.frame <= 250):

                self.order = 4
        elif(self.order == 4):
            if (self.idle_time > 130):
                self.Tutorial_Start.set_volume(64)
                self.Tutorial_Start.repeat_play()
                self.order = 5
            self.idle_time = self.idle_time + 1

        elif(self.order == 5):
            self.idle_time = self.idle_time + 1
            if (self.idle_time > 160):
                self.Tutorial_GAME_START.set_volume(64)
                self.Tutorial_GAME_START.repeat_play()
                self.order = 6
        elif(self.order == 6):
            for i in range(5):
                Zombies[i].state = 1
                Zombies[i].y = 300
                self.order = 7
        elif(self.order == 7): #좀비를 다 알려줬다면 좀비들이 이제 등장
            for i in range(0 , Zombie_Count):
                Zombies[i].x = Zombies[i].x - 1

            current_time = (current_time + 1)
            create()






def enter():
    global mouse_x, mouse_y
    global tutorial
    global Zombies , Plants ,Plants_Card , Sun
    Plants_Card = plant()
    Plants = [] # 객체 초기화
    Zombies = []
    Sun = []
    tutorial = Tutorial()
    for i in range(5):  # 객체 생성
        creat_Zombie()  # 리스트에 좀비들을 집어넣어줌

def creat_Sun():
    global Sun
    new_Sun = Sun_shine()
    Sun.append(new_Sun)

def creat_Zombie():  # 좀비 생성
    global Zombies
    new_zombie = Zombie()

    Zombies.append(new_zombie) # 리스트에 추가해줌
def creat_plant(): # 식물 생성
    global Plants
    new_Plant = plant()
    Plants.append(new_Plant)

def create(): # 모든 걸 만드는 부분
    global current_time
    global Zombies , Zombie_Count , Sun_Count
    if(current_time % 200 == 199):
        creat_Zombie()
        Zombie_Count = Zombie_Count + 1
        Zombies[4 + Zombie_Count].state = 1
        Zombies[4 + Zombie_Count].y = 300
    if(current_time % 100 == 99 ):
        creat_Sun()
        Sun_Count = Sun_Count + 1







def update():
    global tutorial
    global Zombies

    tutorial.update()







def draw():
    global tutorial
    tutorial.draw()

    pass
def exit():
    pass
def handle_events():
    global tutorial
    tutorial.handle_events()

    pass


def pause():
    if(game_menu == True):
        pass

    pass
def resume():
    pass