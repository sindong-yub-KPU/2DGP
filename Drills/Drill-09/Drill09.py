from pico2d import*
running = True
import random
open_canvas()
class ball:
    pass

class Boy:
    def __init__(self):
        self.x , self.y = random.randint(50 , 700) , 90
        self.image = load_image('run_animation.png')
        self.grass_image = load_image('grass.png')
        self.frame = random.randint(0 , 7)
    def draw(self):

        self.image.clip_draw(self.frame * 100  , 0  ,100 , 100 , self.x , self.y )


    def update(self):
        self.frame = (self.frame + 1 ) % 8
        self.x += 5



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

i = 0
running_Boy = Boy()
team = [Boy() for i in range(11)]
balls = [ball() for i in range(20)]
print(type(team))
while(running):
    handle_events()
    clear_canvas()
    Boy().grass_image.draw(400, 40)
    for boy in team:
        boy.draw()
        boy.update()


    delay(0.02)
    update_canvas()







