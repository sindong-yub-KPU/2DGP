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




move = 0
p_count = 0
direction = 0
where = 0
doit = 0
while(True):

    clear_canvas();
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * direction, 100, 100, character_x, character_y)






    move = move + 1
    events = get_events()
    update_canvas()
    frame = (frame + 1) % 8



    delay(0.02)




close_canvas()


turtle.done()