from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

go_x = 500
go_y = 500
def handle_events():
    global running
    global x , y
    global go_x , go_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x , KPU_HEIGHT -1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            go_x,go_y = event.x , KPU_HEIGHT -1 - event.y


    pass










open_canvas(KPU_WIDTH , KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse_point = load_image('hand_arrow.png')
running = True
dir = 0
stand = 0
character_x = 500
character_y = 500
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
right_or_left = 0
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH//2 , KPU_HEIGHT//2)


    mouse_point.draw(x, y)
    character.clip_draw(frame * 100, 100 * right_or_left, 100, 100, character_x, character_y)
    update_canvas()
    frame = (frame + 1) % 8
    if character_x < go_x - 12:
        character_x = character_x + 1
        right_or_left = 1
    if character_x > go_x - 12:
        character_x = character_x - 1
        right_or_left = 0
    if character_x == go_x - 12 and character_y == go_y + 20:
        right_or_left = 2
    if character_y < go_y + 20:
        character_y = character_y + 1
    if character_y > go_y + 20:
        character_y = character_y - 1
    delay(0.005)
    handle_events()

close_canvas()




