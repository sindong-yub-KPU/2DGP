from pico2d import *
import random
import time
font = None

class plants:

    PIXEL_PER_METER = (10.0 / 0.3)# 10 pixel 30 cm
    RUN_SPEED_KMPTH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPTH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self ,mouse_x,mouse_y):
        self.x , self.y = int(mouse_x) , int(mouse_y)
        self.frame = random.randint()
        self.basic_plants_image  ('Baisc_plants.png')
        self.total_frame, self.frame = 0.0 , 0.0


