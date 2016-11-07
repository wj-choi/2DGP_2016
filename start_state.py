import game_framework
from pico2d import *

import title_state

name = "StartState"
image = None
status = 0

logo_time = 0.0

def enter():
    global kpu, game
    open_canvas(1000, 600)
    kpu = load_image('kpu_credit.png')
    game = load_image('game_credit.png')

def exit():
    global image
    del(image)

def update(frame_time):
    global name, status
    global logo_time

    if (logo_time > 1.0):
        status = 1

    if (logo_time > 2.0):
        logo_time = 0
        game_framework.push_state(title_state)

    logo_time += frame_time

def draw(frame_time):
    global image
    global status

    clear_canvas()

    if status == 0:
        kpu.draw(500, 300)
    else:
        game.draw(500, 300)

    update_canvas()

def handle_events(frame_time):
    events = get_events()

def pause(): pass
def resume(): pass




