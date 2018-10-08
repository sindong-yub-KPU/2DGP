from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
point = [(random.randint(100,KPU_WIDTH - 100), random.randint(200,KPU_HEIGHT - 200))for i in range(10) ]

print(point)





open_canvas(KPU_WIDTH , KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
character_x , character_y  = point[0]
frame = 0


def NO_START_END_move_charceter(i,p1, p2, p3, p4):



    # draw p1-p2
    t = i / 100
    x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + ( -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
    y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
    return x , y

    # draw p4-p5

def Re_Init(where):

    global move , p_count

    if (move == 100):
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


    character_x, character_y = NO_START_END_move_charceter(move, point[(p_count - 1) % 10], point[(p_count ) % 10], point[(p_count + 1) % 10] , point[(p_count + 2) % 10])




    print(p_count)
    print(move)
    if(px[0] - character_x > 0):
        direction = 1
    if (px[0] - character_x < 0):
        direction = 0
    move = move + 1
    events = get_events()
    update_canvas()
    frame = (frame + 1) % 8



    delay(0.02)




close_canvas()


turtle.done()