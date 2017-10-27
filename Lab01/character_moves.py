from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
running = True

while running:
    while x < 775:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        x = x + 10
        update_canvas()
        delay(0.01)
    while y < 565:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        y = y + 10
        update_canvas()
        delay(0.01)
    while x > 0:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        x = x - 10
        update_canvas()
        delay(0.01)
    while y > 90:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x, y)
        y = y - 10
        update_canvas()
        delay(0.01)
    running = False
close_canvas()
