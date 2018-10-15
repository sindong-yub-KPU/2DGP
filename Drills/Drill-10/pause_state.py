
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
    pass
def update():
    pass




def pause():
    pass


def resume():
    pass

def draw():
    pass

