from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
framex = 0
framey = 1

while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(framex * 100, framey * 100, 100, 100, x, 90)
    update_canvas()
    framex = (framex + 1) % 8
    x = x + 5
    delay(0.05)
    get_events()

framey = 0

while x > 0:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(framex * 100, framey * 100, 100, 100, x, 90)
    update_canvas()
    framex = (framex + 1) % 8
    x = x - 5
    delay(0.05)
    get_events()

close_canvas()