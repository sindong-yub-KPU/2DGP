import game_framework
from pico2d import*


name = "Tutorial"
tutorial = None

class Tutorial:
    def __init__(self):
        self.Tutorial_Map = load_image('Tutorial/Tutorial_map.png')
        self.board = load_image('Tutorial/board.png')

        pass
    def handle_events(self):
        global game_menu
        events = get_events()


    def draw(self):
        clear_canvas()
        self.Tutorial_Map.draw(700,300)
        self.board.draw(280,550)

        update_canvas()

def update():
    pass


def enter():
    global tutorial
    tutorial = Tutorial()
    pass
def draw():
    global tutorial
    tutorial.draw()

    pass
def exit():
    pass
def handle_events():

    pass
def update():
    pass

