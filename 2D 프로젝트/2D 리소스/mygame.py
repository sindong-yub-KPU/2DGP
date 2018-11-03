from pico2d import *
import game_framework
import start_state
import Tutorial_state

GAME_WIDTH = 1400
GAME_HEIGHT = 600
pico2d.open_canvas(GAME_WIDTH, GAME_HEIGHT)
game_framework.run(Tutorial_state)
pico2d.close_canvas()

