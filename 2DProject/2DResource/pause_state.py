import game_framework
import title_state
import game_world
import Tutorial_state

from pico2d import *
import start_state
name = "Pause_state"
Main_object_esc = None
pausesound = None
frame = 0
def enter():
    global Main_object_esc , pause
    Main_object_esc = load_image('Mainresource/areyousure.png')

    pass


def exit():
    global Main_object_esc
    del(Main_object_esc)
    pass
def handle_events():
    events = get_events()
    for event in events:
        if (event.type == SDL_MOUSEBUTTONDOWN):
            if (event.x < 674 and event.x > 490 and 600 - event.y - 1 < (
                    600 // 4 + 20) + 40 and 600 - event.y - 1 > (
                    600 // 4 + 20) - 40 ):
                    game_framework.quit()



                    game_framework.change_state(title_state)
            elif (event.x < 895 and event.x > 711 and 600 - event.y - 1 < (
                    600 // 4 + 20) + 40 and 600 - event.y - 1 > (
                          600 // 4 + 20) - 40):

                game_framework.pop_state()
def update():

    pass




def pause():
    pass


def resume():
    pass

def draw():
    clear_canvas()


    for game_object in game_world.all_objects():
        game_object.draw()
    Main_object_esc.draw(1400 // 2, 600 // 2, 510, 380)

    update_canvas()