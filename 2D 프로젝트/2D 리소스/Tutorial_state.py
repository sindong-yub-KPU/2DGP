import game_framework
from pico2d import*


name = "Tutorial"
tutorial = None
game_menu = None
class Tutorial:
    def __init__(self):
        self.Tutorial_Map = load_image('Tutorial/Tutorial_map.png')
        self.board = load_image('Tutorial/board.png')
        self.Main_object_esc = load_image('Mainresource/areyousure.png')
        self.intro_music = load_music('Tutorial/intro_music.mp3')
        self.Tutorial_Start = load_music('Tutorial/Tutorial_start.mp3')
        self.font = load_font('Tutorial/ConsolaMalgun.ttf', 30)
        self.intro_music.set_volume(64)
        self.intro_music.repeat_play()
        self.frame = 0 # 화면을 옮겨주는 프레임
        self.order = 0 # frame을 움직여야할 상태값
        self.idle_time = 0 # 화면 정지 시간
        self.str = "우리들의 집" # 글자 출력


        #self.arrow('Tutorial/arrow.png')
        pass
    def handle_events(self):
        global game_menu
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

                if (event.x < 895 and event.x > 711 and GAME_HEIGHT - event.y - 1 < (GAME_HEIGHT // 4 + 20) + 40 and GAME_HEIGHT - event.y - 1 > (GAME_HEIGHT // 4 + 20) - 40 and game_menu == True):
                    game_menu = False

    def draw(self):

        clear_canvas()
        #처음 시작시는 0 으로 바꿔줌 # 700 까지 올려주고 다시 200으로 내려줌
        #글자 써줘야함
        #200 # 800  게임 시작시
        #도로에 좀비들을 아이들 상태로 그려줘야함
        self.Tutorial_Map.clip_draw(0 + self.frame, 0 , 800 , 600 , 700 , 300,1400,600 )
        self.board.clip_draw(0 , 0 ,557 , 109  , 280, 560 ,  557 , 80)
        if(game_menu == True):
            self.Main_object_esc.draw(1400//2 ,600//2, 510, 380 )
        if(self.order < 4):
            self.font.draw(600, 50, 'My house...')
        update_canvas()
        delay(0.02)

    def update(self):
        if(self.idle_time >= 50 and self.order == 0):
            self.order = 1
        if(self.order == 0):
            self.idle_time = self.idle_time + 1

        elif(self.order == 1):
            self.frame = self.frame + 3
            if(self.frame >= 600):
                self.order = 2
                print(0)
        elif (self.order == 2):
            if(self.idle_time > 100):
                self.order = 3
            self.idle_time = self.idle_time + 1
        elif(self.order == 3):
            self.frame = self.frame - 3
            if(self.frame <= 200):
                self.order = 4
        elif(self.order == 4):
            self.Tutorial_Start.set_volume(64)
            self.Tutorial_Start.repeat_play()
            self.order = 5




def enter():
    global tutorial
    tutorial = Tutorial()
    pass
def update():
    global tutorial
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