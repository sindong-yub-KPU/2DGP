from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')
character2 = load_image('animation_sheet.png')
count =0
x = 0
frame = 0
while (1):
    if(count == 0):

        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)  # left , bottom , width , height  , x , y
        update_canvas()
        frame = (frame + 1) % 8  # 애니메이션을 빠르게 하려면 frame을 높이면 된다
        x += 10  # 캐릭터를 빠르게 하려면 x값을 더 올려줘야한다.
        delay(0.05)
        get_events()
        if (x > 790):
            count = 1
    if(count ==1):
        clear_canvas()
        grass.draw(400, 30)
        character2.clip_draw(frame * 100, 0, 100, 100, x, 90)  # left , bottom , width , height  , x , y
        update_canvas()
        frame = (frame + 1) % 8  # 애니메이션을 빠르게 하려면 frame을 높이면 된다
        x -= 10  # 캐릭터를 빠르게 하려면 x값을 더 올려줘야한다.
        delay(0.05)
        get_events()
        if (x < 10):
            count = 0



close_canvas()

