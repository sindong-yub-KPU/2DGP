from pico2d import *


def handle_events():
    global running
    global dir
    global stand
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                stand =0
            elif event.key == SDLK_LEFT:
                dir += 1
                stand = 1
    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0
stand = 0
right_or_left = 1
while running:
    if(dir == 1):
        right_or_left = 1
    if(dir == -1):
        right_or_left = 0
    if dir == 0 and stand == 1:
        right_or_left = 2
    if dir == 0 and stand == 0:
        right_or_left = 3
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * right_or_left, 100, 100, x, 90)
    update_canvas()
    x += dir * 5
    handle_events()
    frame = (frame + 1) % 8

    delay(0.05)

close_canvas()

