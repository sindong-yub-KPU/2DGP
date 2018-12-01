from pico2d import *
import game_framework
import game_world
import Tutorial_state
import Stage1_state
import StageLevelTwo_state
GAME_WIDTH = 1400
GAME_HEIGHT = 600

game_start = False
game_menu = False
game_running = True
change_screen = 0
select_what =0
MAIN = None
class Main_UI:
    def __init__(self) :
        self.Main_Screen = load_image('Mainresource/main_image.png')
        self.Main_bar = load_image('Mainresource/SelectorAdventureButton.png')
        self.Main_object = load_image('Mainresource/icono.png');
        self.Main_object_esc = load_image('Mainresource/areyousure.png')
        self.Main_UI = load_image('Mainresource/Main_UI.png')
        self.Select_stage = load_image('Mainresource/Select_Stage.png')
        self.soundtime = 0
        self.clicksound = load_wav('Gamesoundeffect/clicksound.ogg')
        self.clicksound.set_volume(64)
        self.start_music = load_music('start_sound.mp3')
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


                if(mouse_x <= GAME_WIDTH//2 +146 and mouse_x >= GAME_WIDTH//2 - 146  and GAME_HEIGHT -mouse_y -1< GAME_HEIGHT//8 + 150 and GAME_HEIGHT - mouse_y -1 > GAME_HEIGHT//8):
                    game_start = False
                else:
                    if(change_screen == 0):
                        game_start = True

            elif(event.type == SDL_MOUSEBUTTONDOWN):


                  # 게임 시작
                if( game_start == False and change_screen == 0): #게임 스타트가 false일떄 마우스 다운
                    change_screen = 1
                    self.clicksound.play()


                elif (event.x < 674  and event.x > 490 and GAME_HEIGHT - event.y - 1 < (GAME_HEIGHT // 4 + 20) + 40 and GAME_HEIGHT - event.y - 1 > (GAME_HEIGHT // 4 + 20) - 40 and game_menu == True):
                    game_running = False

                elif (event.x < 895 and event.x > 711 and GAME_HEIGHT - event.y - 1 < (GAME_HEIGHT // 4 + 20) + 40 and GAME_HEIGHT - event.y - 1 > (GAME_HEIGHT // 4 + 20) - 40 and game_menu == True):
                    game_menu = False
                elif(change_screen == 1 and event.x > 390 and event.x < 1010 and GAME_HEIGHT - event.y -1 < 490 and GAME_HEIGHT - event.y -1 > 370):
                    change_screen = 2
                    self.start_music.set_volume(64)
                    self.start_music.play()
                elif (change_screen == 1 and event.x > 390 and event.x < 1010 and GAME_HEIGHT - event.y - 1 < 320 and GAME_HEIGHT - event.y - 1 > 200):
                    change_screen = 3
                    self.start_music.set_volume(64)
                    self.start_music.play()
                elif (change_screen == 1 and event.x > 390 and event.x < 1010 and GAME_HEIGHT - event.y - 1 < 150 and GAME_HEIGHT - event.y - 1 > 25):
                    change_screen = 4
                    self.start_music.set_volume(64)
                    self.start_music.play()



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
        self.Main_UI.draw(700 , 450)
        if (change_screen == 1):
            self.Select_stage.draw(700, 300)
        if(game_menu == True):
            self.Main_object_esc.draw(GAME_WIDTH//2 ,GAME_HEIGHT//2, 510, 380 )

        update_canvas()

def update():
    global MAIN


    if(change_screen == 2):
        MAIN.soundtime = MAIN.soundtime + 1
        delay(0.02)
        if(MAIN.soundtime > 140):
            game_framework.change_state(Tutorial_state)
    if (change_screen == 3):
        MAIN.soundtime = MAIN.soundtime + 1
        delay(0.02)
        if (MAIN.soundtime > 140):
            game_framework.change_state(Stage1_state)
    if (change_screen == 4):
        MAIN.soundtime = MAIN.soundtime + 1
        delay(0.02)
        if (MAIN.soundtime > 140):
            game_framework.change_state(StageLevelTwo_state)

    pass
def enter():
    global MAIN

    game_world.objects = [[],[]]
    MAIN = Main_UI()
    pass
def draw():
    global MAIN
    MAIN.draw()
def exit():
    global MAIN , change_screen , game_start ,game_running , game_menu
    game_start = False
    game_menu = False
    game_running = True
    change_screen = 0

    change_screen =0
    del MAIN

def handle_events():
    global MAIN
    global game_running
    MAIN.handle_events()
    if(game_running == False):
        game_framework.quit()

    pass
def pause():

    pass
