from pico2d import *

def handle_events():
    global running
    global x, y
    global a
    global click
    global i
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 600 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            i += 1
            click = True
            a.append(x)
            a.append(y)
            a.append(frame)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            i = 0
            a.clear()


open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
x, y = 100, 100
a = []
i = 0
frame = 0
click = False
hide_cursor()
while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)

    if click == True:
        for j in range(i):
            character.clip_draw(a[(j*3) + 2] * 100, 0, 100, 100, a[(j*3) + 0], a[(j*3) + 1])

    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()
