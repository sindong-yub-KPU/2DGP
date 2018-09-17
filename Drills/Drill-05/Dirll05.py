from pico2d import *
running = True
direction = 0;
right_or_left = 0
gox = True
goy = True
open_canvas()
character = load_image('animation_sheet.png')
x = 682
y = 336
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
    direction = 3
    if x >= 715:
        gox = False
    if y <= 136:
        goy = False
    if (gox == False and goy == False):
        count = 4
        gox = True
        goy = True
    pass
def five_point():
    global direction, count, direction, gox, goy, x, y
    direction = 2
    if x <= 316:
        gox = False
    if y >= 225:
        goy = False
    if (gox == False and goy == False):
        count = 5
        gox = True
        goy = True

    pass
def six_point():
    global direction, count, direction, gox, goy, x, y
    if count == 5 :
        direction = 3
        if x >= 510 :
            gox = False
        if y <= 92 :
            goy = False
        if (gox == False and goy == False):
            count = 6
            gox = True
            goy = True
    pass
def seven_point():
    global direction, count, direction, gox, goy, x, y
    if count == 6 :
        direction = 0
        if x >= 692 :
            gox = False
        if y >= 518 :
            goy = False
        if (gox == False and goy == False):
            count = 7
            gox = True
            goy = True
    pass
def eight_point():
    global direction, count, direction, gox, goy, x, y
    if count == 7 :
        direction = 1
        if x <= 682 :
            gox = False
        if y <= 336 :
            goy = False

        if (gox == False and goy == False):
            count = 8
            gox = True
            goy = True
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
    #three_point()
    #four_point()
    #five_point()
    #six_point()
    seven_point()
    goto_x_y()

    character.clip_draw(frame * 100, 100 * right_or_left, 100, 100, x, y)
    delay(0.02)
    update_canvas()
    frame = (frame + 1) % 8

close_canvas()