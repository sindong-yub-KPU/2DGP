from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
point = [(random.randint(100,KPU_WIDTH - 100), random.randint(100,KPU_HEIGHT - 100))for i in range(20) ]

character_x , character_y  = point[0]



open_canvas(KPU_WIDTH , KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
frame = 0

def move_characeter(i , p1, p2):

    t = i / 100
    x = (1 - t) * p1[0] + t*p2[0]
    y = (1 - t) * p1[1] + t*p2[1]
    return x , y
def Re_Init():
    global move , p_count
    if(move == 100):
        move = 0

move =0
p_count = 0
while(True):

    clear_canvas();
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, character_x, character_y)
    px = point[((p_count + 1) % 10)]
    character_x, character_y = move_characeter(move, point[p_count % 10], point[((p_count + 1) % 10)])

    move = move + 2
    events = get_events()
    update_canvas()
    frame = (frame + 1) % 8

    Re_Init()

    delay(0.02)




close_canvas()


turtle.done()