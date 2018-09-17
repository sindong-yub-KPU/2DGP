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

def four_point():
    global direction, count, direction, gox, goy, x, y
    if count == 3 :
        direction = 3
        if x >= 715 :
            gox = False
        if y <= 136 :
            goy = False
        if (gox == False and goy == False):
            count = 4
            gox = True
            goy = True

def five_point():
    global direction, count, direction, gox, goy, x, y
    if count == 4 :
        direction = 2
        if x <= 316 :
            gox = False
        if y >= 225 :
            goy = False
        if (gox == False and goy == False):
            count = 5
            gox = True
            goy = True


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

def nine_point():
    global direction, count, direction, gox, goy, x, y
    if count == 8 :
        direction = 0
        if x >= 712 :
            gox = False
        if y >= 349 :
            goy = False
        if (gox == False and goy == False):
            count = 9
            gox = True
            goy = True

def return_point():
    global direction, count, direction, gox, goy, x, y
    if count == 9 :
        if x <= 203:
            gox = False
        if y >= 535:
            goy = False

        direction = 2
        if (gox == False and goy == False):
            count = 0
            gox = True
            goy = True



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
def right_left_direction():
    global direction, right_or_left
    if direction == 0 or direction == 3:
        right_or_left = 1
    if direction == 1 or direction == 2:
        right_or_left = 0

while running:

    clear_canvas()
    one_point()
    two_point()
    three_point()
    four_point()
    five_point()
    six_point()
    seven_point()
    eight_point()
    nine_point()
    return_point()
    goto_x_y()
    right_left_direction()
    character.clip_draw(frame * 100, 100 * right_or_left, 100, 100, x, y)
    delay(0.02)
    update_canvas()
    frame = (frame + 1) % 8

close_canvas()