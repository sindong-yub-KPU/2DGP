from pico2d import *
import game_framework
import Tutorial_state
GAME_WIDTH = 1400
GAME_HEIGHT = 600

game_start = False
game_menu = False
game_running = True
change_screen = 0
class Main_UI:
    def __init__(self) :
        self.Main_Screen = load_image('Mainresource/main_image.png')
        self.Main_bar = load_image('Mainresource/SelectorAdventureButton.png')
        self.Main_object = load_image('Mainresource/icono.png');
        self.Main_object_esc = load_image('Mainresource/areyousure.png')
        pass


        self.bgm = load_music('Mainresource/Plants vs Zombies Soundtrack. [Main Menu].mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def handle_events(self):
        global game_running
        global game_start
        global change_screen
        global game_menu
        events = get_events()

        for event in events:

            if(event.type == SDL_QUIT or event.key == SDLK_ESCAPE): # 게임 나가기
                game_menu = True

            if(event.type == SDL_MOUSEMOTION): #마우스 좌표 받음
                mouse_x = event.x
                mouse_y = event.y  # 게임 시작
                print(event.x)
                print(event.y)


                if(mouse_x <= GAME_WIDTH//2 +146 and mouse_x >= GAME_WIDTH//2 - 146  and GAME_HEIGHT -mouse_y -1< GAME_HEIGHT//8 + 150 and GAME_HEIGHT - mouse_y -1 > GAME_HEIGHT//8):
                    game_start = False
                else:
                    game_start = True

            elif(event.type == SDL_MOUSEBUTTONDOWN):


                  # 게임 시작
                if( game_start == False):
                    change_screen = 1
                if (event.x < 674  and event.x > 490 and GAME_HEIGHT - event.y - 1 < (GAME_HEIGHT // 4 + 20) + 40 and GAME_HEIGHT - event.y - 1 > (GAME_HEIGHT // 4 + 20) - 40 and game_menu == True):
                    game_running = False

                if (event.x < 895 and event.x > 711 and GAME_HEIGHT - event.y - 1 < (GAME_HEIGHT // 4 + 20) + 40 and GAME_HEIGHT - event.y - 1 > (GAME_HEIGHT // 4 + 20) - 40 and game_menu == True):
                    game_menu = False


    def draw(self):
        if(game_start == True):
            frame = 0
        if(game_start  == False):
            frame = 1
        bar_size_x = 332
        bar_size_y = 292
        clear_canvas()
        self.Main_Screen.draw(GAME_WIDTH//2 ,GAME_HEIGHT//2, 1400, 600 )
        self.Main_bar.clip_draw(0, 146 * frame , 332 , bar_size_y//2 , GAME_WIDTH//2 , GAME_HEIGHT//4)
        self.Main_object.draw(GAME_WIDTH//2  + 200,GAME_HEIGHT//4, 256, 256 )
        if(game_menu == True):
            self.Main_object_esc.draw(GAME_WIDTH//2 ,GAME_HEIGHT//2, 510, 380 )

        update_canvas()
def update():
    pass
def enter():
    global Main_UI

    Main_UI = Main_UI()
    pass
def draw():
    global Main_UI
    Main_UI.draw()
def exit():
    global Main_UI
    del (Main_UI)

def handle_events():
    global Main_UI
    global game_running
    Main_UI.handle_events()
    if(game_running == False):
        game_framework.quit()
    if(change_screen == 1):
        game_framework.change_state(Tutorial_state)
    pass
