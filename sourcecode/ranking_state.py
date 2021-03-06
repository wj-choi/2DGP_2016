import framework
from pico2d import *

import pause_state

name = "RankingState"
image = None
font = None

def enter():
    global image, font
    image = load_image("scoreboard.png")
    font = load_font("PWChalk.TTF", 60)


def exit():
    global image, font
    del(image)
    del(font)

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global select_status
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                    framework.push_state(pause_state)



def update(frame_time):
    pass


def draw(frame_time):
    global image
    global back
    global font

    clear_canvas()

    image.draw(500, 300)

    font.draw(275, 540, "HALL OF FAME", (0, 0, 0))

    font.draw
    update_canvas()



