from pico2d import *
running = True
direction = 0;
right_or_left = 0
gox = True
goy = True
open_canvas()
character = load_image('animation_sheet.png')
x = 535
y = 470
frame = 0
# 0 이면 + + 1 이면 - - 2 이면 - + 3 이면 + -
count = 0
def one_point ():

    global direction , count , direction , gox , goy , x ,y

    if count == 0:
        direction = 1
        if x <= 132 :
            gox = False
        if y <= 243 :
            goy = False
        if(gox == False and goy == False ):
            count = 1
            gox = True
            goy = True
    pass
def two_point ():
    global direction, count, direction, gox, goy, x, y
    if count == 1 :
        direction = 0
        if x >= 535 :
            gox = False
        if y >= 470 :
            goy = False
        if (gox == False and goy == False):
            count = 2
            gox = True
            goy = True
    pass
def three_point():
    global direction, count, direction, gox, goy, x, y
    if count == 2 :
        direction = 1
        if x <= 477 :
            gox = False
        if y <= 203 :
            goy = False
        if (gox == False and goy == False):
            count = 3
            gox = True
            goy = True
    pass
def four_point():
    global direction, count, direction, gox, goy, x, y
    pass
def five_point():
    global direction, count, direction, gox, goy, x, y
    pass
def six_point():
    global direction, count, direction, gox, goy, x, y
    pass
def seven_point():
    global direction, count, direction, gox, goy, x, y
    pass
def eight_point():
    global direction, count, direction, gox, goy, x, y
    pass
def nine_point():
    global direction, count, direction, gox, goy, x, y
    pass
def return_point():
    global direction, count, direction, gox, goy, x, y
    pass

def direction_point():
    global direction
    pass
def goto_x_y():
    global direction , count , direction , gox , goy ,x ,y
    if direction == 0:
        if gox == True:
            x += 2
        if goy == True:
            y += 2
    elif direction == 1:
        if gox == True:
            x -= 2
        if goy == True:
            y -= 2
    elif direction == 2:
        if gox == True:
            x -= 2
        if goy == True:
            y += 2
    elif direction == 3:
        if gox == True:
            x += 2
        if goy == True:
            y -= 2
pass
while running:
    clear_canvas()
    #one_point()
    #two_point()
    three_point()
    goto_x_y()

    character.clip_draw(frame * 100, 100 * right_or_left, 100, 100, x, y)
    delay(0.02)
    update_canvas()
    frame = (frame + 1) % 8

close_canvas()