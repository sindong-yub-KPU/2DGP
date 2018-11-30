from pico2d import *
import game_framework
import game_world
import pause_state

from Stage1 import Stage_level_1




name = "Stage1"


Stage1 = None


def enter():
    game_world.objects = [[], []]
    global Stage1
    Stage1 = Stage_level_1()
    game_world.add_object(Stage1, 0)
def exit():
    game_world.clear()

def pause():
    pass
def resume():
    pass
def handle_events():
    global Stage1
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Stage1.pausego.play()
            game_framework.push_state(pause_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Stage1.pausego.play()
            game_framework.push_state(pause_state)
        else :
            Stage1.handle_event(event)
    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()