from pico2d import *
import game_framework
import game_world
import pause_state

from tutorial import Tutorial




name = "Tutorial_state"


tutorial = None


def enter():
    global tutorial
    tutorial = Tutorial()
    game_world.add_object(tutorial, 0)

def exit():
    global tutorial
    game_world.clear()
    del tutorial

def pause():
    pass
def resume():
    pass
def handle_events():
    global tutorial
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            tutorial.pausego.play()

            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            tutorial.pausego.play()
            game_framework.push_state(pause_state)
        else :
            tutorial.handle_event(event)
    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()