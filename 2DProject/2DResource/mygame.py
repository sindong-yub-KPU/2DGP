from pico2d import *
import game_framework
import start_state
import Tutorial_state
import Stage1_state
import StageLevelTwo_state
GAME_WIDTH = 1400
GAME_HEIGHT = 600
pico2d.open_canvas(GAME_WIDTH, GAME_HEIGHT)
game_framework.run(Stage1_state)
pico2d.close_canvas()
