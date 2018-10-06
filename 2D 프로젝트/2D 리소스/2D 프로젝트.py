from pico2d import *

GAME_WIDTH = 1400
GAME_HEIGHT = 600
open_canvas(GAME_WIDTH, GAME_HEIGHT)
Mouse_click = False
class Main_UI:
    def __init__(self) :
        self.Main_Screen = load_image('Mainresource/main_image.png')
        self.Main_bar = load_image('Mainresource/SelectorAdventureButton.png')
        self.Main_object = load_image('Mainresource/icono.png');
        self.Main_object_esc = load_image('Mainresource/areyousure.png')

        self.bgm = load_music('Mainresource/Plants vs Zombies Soundtrack. [Main Menu].mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def mouse_event(self):
        global Mouse_click
        events = get_events()
        print(Mouse_click)
        for event in events:
            if(event.type == SDL_MOUSEMOTION):
                mouse_x = event.x
                mouse_y = event.y
                if(mouse_x <= GAME_WIDTH//2 +146 and mouse_x >= GAME_WIDTH//2 - 146  and GAME_HEIGHT -mouse_y -1< GAME_HEIGHT//8 + 150 and GAME_HEIGHT - mouse_y -1 > GAME_HEIGHT//8):
                    Mouse_click = False
                else:
                    Mouse_click = True
             #if(event.type == SDL_MOUSEBUTTONDOWN):


    def main_darw(self):
        if(Mouse_click == True):
            frame = 0
        if(Mouse_click  == False):
            frame = 1
        bar_size_x = 332
        bar_size_y = 292
        clear_canvas()
        self.Main_Screen.draw(GAME_WIDTH//2 ,GAME_HEIGHT//2, 1400, 600 )
        self.Main_bar.clip_draw(0, 146 * frame , 332 , bar_size_y//2 , GAME_WIDTH//2 , GAME_HEIGHT//4)
        self.Main_object.draw(GAME_WIDTH//2  + 200,GAME_HEIGHT//4, 256, 256 )

        update_canvas()





GAME_UI = Main_UI()

while(True):
    GAME_UI.main_darw()
    GAME_UI.mouse_event()
    delay(0.05)