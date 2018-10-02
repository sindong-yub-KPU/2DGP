from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
point = [(random.randint(100,KPU_WIDTH - 100), random.randint(100,KPU_HEIGHT - 100))for i in range(10) ]

print(point)





open_canvas(KPU_WIDTH , KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
character_x , character_y  = point[0]
frame = 0

def start_move_characeter(i , p1, p2 ,p3):
    t = i / 100
    x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
    y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
    return x, y
def NO_START_END_move_charceter(i , p1 , p2 , p3 , p4):
    t = i / 100
    x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (-3 * t ** 3 + 4 * t ** 2 + t) *
         p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
    y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (-3 * t ** 3 + 4 * t ** 2 + t) *
         p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
    return x, y
def end_move_characeter(i , p1 , p2 ,p3):
    t = i / 100
    x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
    y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
    print(where)
    return x, y


def Re_Init(where):
    global move , p_count
    if(where == 0):
        if(move == 50):
            move = 0
            p_count = p_count + 1
    elif(where == 1):
        if (move == 100):
            move = 0
            p_count = p_count + 1
    elif(where == 2):
        if(move == 50):
            move = 0
            p_count = p_count + 1
move = 0
p_count = 0
direction = 0
where = 0
doit = 0
while(True):

    clear_canvas();
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * direction, 100, 100, character_x, character_y)
    Re_Init(where)
    px = point[((p_count + 1) % 10)]
    if((p_count % 10) == 0):
        character_x, character_y = start_move_characeter(move, point[(p_count % 10)], point[(p_count+1) % 10] ,point[(p_count+2) % 10])
        where = 0
    elif((p_count % 10)  > 0 and (p_count % 10) < 9):
        character_x, character_y = NO_START_END_move_charceter(move, point[(p_count -1) % 10], point[(p_count ) % 10], point[(p_count + 1) % 10] , point[(p_count + 2) % 10])
        where = 1
    elif ((p_count % 10) == 9):
        character_x, character_y = start_move_characeter(move+50, point[(p_count -1) % 10], point[(p_count) % 10], point[(p_count+1) % 10])
        where = 2


    print(p_count)
    print(move)
    if(px[0] - character_x > 0):
        direction = 1
    if (px[0] - character_x < 0):
        direction = 0
    move = move + 2
    events = get_events()
    update_canvas()
    frame = (frame + 1) % 8



    delay(0.02)




close_canvas()


turtle.done()