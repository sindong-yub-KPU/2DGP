from pico2d import*
import random
running = True
open_canvas()
class ball:
    def __init__(self):

        self.x , self.y = random.randint(20 , 800) , 600
        self.right = random.randint(0, 1)
        if(self.right == 0):
            self.ball_image = load_image('ball21x21.png')
        if(self.right == 1):
            self.ball_image = load_image('ball41x41.png')

        self.fall = random.randint(2 , 10)
    def draw(self):

        self.ball_image.draw(self.x , self.y)

    def update(self):
        if(self.right == 0):
            if(self.y > 70):
                self.y -= self.fall
            elif (self.y < 70):
                self.y += (70 - self.y)
        if(self.right == 1):
            if (self.y > 70 + 25 / 2 ):
                self.y -= self.fall
            elif (self.y < 70 + 25 /2 ):
                self.y += ((70 + 25/2) - self.y)

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


team = [Boy() for i in range(11)]
balls = [ball() for i in range(20)]

while(running):
    handle_events()
    clear_canvas()
    Boy().grass_image.draw(400, 40)
    for boy in team:
        boy.draw()
        boy.update()

    for ball in balls:
        ball.draw()
        ball.update()
    delay(0.02)
    update_canvas()







