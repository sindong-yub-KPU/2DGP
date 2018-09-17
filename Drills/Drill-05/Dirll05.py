from pico2d import *
running = True
direction = 0;
right_or_left = 0
gox = True
goy = True
open_canvas()
character = load_image('animation_sheet.png')
x = 203
y = 535
frame = 0
# 0 이면 + + 1 이면 - - 2 이면 - + 3 이면 + -
count = 0
def one_point ():

    pass
def two_point ():
    pass
def three_point():
    pass
def four_point():
    pass
def five_point():
    pass
def six_point():
    pass
def seven_point():
    pass
def eight_point():
    pass
def nine_point():
    pass
def return_point():
    pass

def direction_point():
    pass

while running:
    clear_canvas()
    one_point()

    character.clip_draw(frame * 100, 100 * right_or_left, 100, 100, x, y)
    delay(0.02)
    update_canvas()
    frame = (frame + 1) % 8

close_canvas()