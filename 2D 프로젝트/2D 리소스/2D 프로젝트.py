from pico2d import *

GAME_WIDTH = 1400
GAME_HEIGHT = 600
open_canvas(GAME_WIDTH, GAME_HEIGHT)

class Main_UI:
    def __init__(self) :
        self.Main_Screen = load_image('main_image.png')
        self.Main_bar_green = load_image('loading_bar_green.png')
        self.Main_bar_Red = load_image('loading_bar_red.png')

        self.bgm = load_music('Main_UI_music.mp3')
        self.bgm = load_music()

    def main_darw(self):

        clear_canvas()
        self.Main_Screen.draw(GAME_WIDTH//2 ,GAME_HEIGHT//2,1400,600 )
        self.Main_bar_green.draw(GAME_WIDTH/2 , GAME_HEIGHT/5)
        update_canvas()





GAME_UI = Main_UI()

while(True):
    GAME_UI.main_darw()
    events = get_events()

    delay(0.05)