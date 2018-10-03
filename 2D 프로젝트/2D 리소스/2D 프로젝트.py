from pico2d import *

GAME_WIDTH = 1400
GAME_HEIGHT = 600
open_canvas(GAME_WIDTH, GAME_HEIGHT)

class Main_UI:
    def __init__(self) :
        self.Main_Screen = load_image('main_image.png')
        self.Main_bar = load_image('SelectorAdventureButton.png')


        self.bgm = load_music('Plants vs Zombies Soundtrack. [Main Menu].mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def main_darw(self):
        frame = 0
        bar_size_x = 332
        bar_size_y = 292
        clear_canvas()
        self.Main_Screen.draw(GAME_WIDTH//2 ,GAME_HEIGHT//2,1400,600 )
        self.Main_bar.clip_draw(0, 146 * frame , 332 , bar_size_y//2 , GAME_WIDTH//2 , GAME_HEIGHT//4)
        update_canvas()





GAME_UI = Main_UI()

while(True):
    GAME_UI.main_darw()
    events = get_events()

    delay(0.05)