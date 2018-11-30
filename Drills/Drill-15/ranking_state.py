import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state

name = "Rankstate"
rank = []
font = None
Ranking = []
def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

boy = None

def enter():
    global font
    hide_cursor()
    hide_lattice()
    load_rank()
    font = load_font('ENCR10B.TTF', 20)

def exit():
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)



def update():
    pass


def draw():
    global rank
    global font
    clear_canvas()
    count = 0
    for data in rank:
        count += 20
        font.draw(150 , 800 -count ,'player %d Time: %3.2f' % (data[0], data[1]), (0, 0, 0))


    update_canvas()
def load_rank():
    global rank
    global Ranking

    with open('rank_data.json', 'r') as f:
        rank = json.load(f)

    rank.sort(key=lambda element: element[1])