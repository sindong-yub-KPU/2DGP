from pico2d import *
import game_framework
import game_world

from tutorial import Tutorial




name = "Tutorial_state"


tutorial = None


def enter():
    global tutorial
    tutorial = Tutorial()
    game_world.add_object(tutorial, 0)
def exit():
    game_world.clear()

def pause():
    pass
def resume():
    pass
def handle_events():
    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()