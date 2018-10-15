
import game_framework
import title_state
import main_state
from pico2d import *

name = "Pause_state"
image = None
frame = 0
def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del(image)
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type , event.key) == (SDL_KEYDOWN , SDLK_ESCAPE):
                game_framework.change_state(title_state)
            elif (event.type , event.key) == (SDL_KEYDOWN , SDLK_p):
                game_framework.pop_state()
def update():
    global frame
    frame = (frame + 1) % 300
    pass




def pause():
    pass


def resume():
    pass

def draw():
    clear_canvas()

    image.clip_draw(225,250, 450,450, 400, 300)

    update_canvas()
