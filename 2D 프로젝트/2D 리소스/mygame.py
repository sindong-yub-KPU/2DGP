import game_framework
import start_state
import pico2d
GAME_WIDTH = 1400
GAME_HEIGHT = 600
pico2d.open_canvas(GAME_WIDTH, GAME_HEIGHT)
print(10)
game_framework.run(start_state)
pico2d.close_canvas()