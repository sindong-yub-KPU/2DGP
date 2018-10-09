from pico2d import *
import random
running = True
open_canvas()
class Boy:
    def __init__(self):
        #self.x, self.y = 0 , 90
        self.x , self.y = random.randint(0 , 800) , 90
        self.frame = random.randint(0 , 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x  += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100 , 0 , 100 , 100 , self.x ,self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400 ,30)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
team = [Boy() for i in range(11)] # team은 소년을 생성 11 번
grass = Grass()
boy = Boy()
while(running):
    handle_events()

    clear_canvas()
    for boy in team:
        boy.draw()
        boy.update()
    grass.draw()
    update_canvas()
    delay(0.02)



