# hero_controller.py : control hero move with left and right key

import random
from pico2d import *

running = None
hero = None
speed = 5
frame = 3


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Hero:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3
    UP_RUN, DOWN_RUN, UP_LEFT_RUN, UP_RIGHT_RUN, DOWN_LEFT_RUN, DOWN_RIGHT_RUN = 4, 5, 6, 7, 8, 9


    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.state = self.RIGHT_STAND
        if Hero.image == None:
            Hero.image = load_image('animation_sheet.png')

    def handle_event(self, event):
        global frame
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            # 서있다가 왼쪽 키가 눌렸을 때
            if self.state in (self.LEFT_STAND, self.RIGHT_STAND):
                self.state = self.LEFT_RUN
                frame = self.LEFT_RUN
            # 오른쪽으로 달리다 왼쪽 키가 눌렸을 때
            elif self.state in (self.RIGHT_RUN, ):
                self.state = self.LEFT_RUN
                frame = self.LEFT_RUN
            # 위쪽으로 달리다 왼쪽 키가 눌렸을 때
            elif self.state in (self.UP_RUN, ):
                self.state = self.UP_LEFT_RUN
                frame = self.LEFT_RUN
            # 아래쪽으로 달리다 왼쪽 키가 눌렸을 때
            elif self.state in (self.DOWN_RUN, ):
                self.state = self.DOWN_LEFT_RUN
                frame = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            # 서있다가 오른쪽 키가 눌렸을 때
            if self.state in (self.LEFT_STAND, self.RIGHT_STAND):
                self.state = self.RIGHT_RUN
                frame = self.RIGHT_RUN
            # 왼쪽으로 달리다 오른쪽 키가 눌렸을 때
            elif self.state in (self.LEFT_RUN, ):
                self.state = self.RIGHT_RUN
                frame = self.RIGHT_RUN
            # 위쪽으로 달리다 오른쪽 키가 눌렸을 때
            elif self.state in (self.UP_RUN, ):
                self.state = self.UP_RIGHT_RUN
                frame = self.RIGHT_RUN
            # 아래쪽으로 달리다 오른쪽 키가 눌렸을 때
            elif self.state in (self.DOWN_RUN, ):
                self.state = self.DOWN_RIGHT_RUN
                frame = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            # 왼쪽 보고 서있다가 위쪽 키가 눌렸을 때
            if self.state in (self.LEFT_STAND, ):
                self.state = self.UP_RUN
                frame = self.LEFT_RUN
            # 오른쪽 보고 서있다가 위쪽 키가 눌렸을 때
            elif self.state in (self.RIGHT_STAND, ):
                self.state = self.UP_RUN
                frame = self.RIGHT_RUN
            # 왼쪽으로 달리다 위쪽 키가 눌렸을 때
            elif self.state in (self.LEFT_RUN, ):
                self.state = self.UP_LEFT_RUN
                frame = self.LEFT_RUN
            # 오른쪽으로 달리다 위쪽 키가 눌렸을 때
            elif self.state in (self.RIGHT_RUN, ):
                self.state = self.UP_RIGHT_RUN
                frame = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            # 왼쪽 보고 서있다가 아래쪽 키가 눌렸을 때
            if self.state in (self.LEFT_STAND, ):
                self.state = self.DOWN_RUN
                frame = self.LEFT_RUN
            # 오른쪽 보고 서있다가 아래쪽 키가 눌렸을 때
            elif self.state in (self.RIGHT_STAND, ):
                self.state = self.DOWN_RUN
                frame = self.RIGHT_RUN
            # 왼쪽으로 달리다 아래쪽 키가 눌렸을 때
            elif self.state in (self.LEFT_RUN, ):
                self.state = self.DOWN_LEFT_RUN
                frame = self.LEFT_RUN
            # 오른쪽으로 달리다 아래쪽 키가 눌렸을 때
            elif self.state in (self.RIGHT_RUN, ):
                self.state = self.DOWN_RIGHT_RUN
                frame = self.RIGHT_RUN

        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
                frame = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
                frame = self.RIGHT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP_RUN,):
                self.state = self.LEFT_STAND
                frame = self.LEFT_STAND
            elif self.state in (self.UP_LEFT_RUN,):
                self.state = self.LEFT_STAND
                frame = self.LEFT_STAND
            elif self.state in (self.UP_RIGHT_RUN, ):
                self.state = self.RIGHT_STAND
                frame = self.RIGHT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.DOWN_RUN,):
                self.state = self.LEFT_STAND
                frame = self.LEFT_STAND
            elif self.state in (self.DOWN_LEFT_RUN,):
                self.state = self.LEFT_STAND
                frame = self.LEFT_STAND
            elif self.state in (self.DOWN_RIGHT_RUN, ):
                self.state = self.RIGHT_STAND
                frame = self.RIGHT_STAND
        pass


    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.state == self.LEFT_RUN:
            self.x = max(0, self.x - speed)
        elif self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + speed)
        elif self.state == self.UP_RUN:
            self.y = min(600, self.y + speed)
        elif self.state == self.DOWN_RUN:
            self.y = max(0, self.y - speed)
        elif self.state == self.UP_LEFT_RUN:
            self.x = max(0, self.x - speed)
            self.y = min(600, self.y + speed)
        elif self.state == self.UP_RIGHT_RUN:
            self.x = min(800, self.x + speed)
            self.y = min(600, self.y + speed)
        elif self.state == self.DOWN_LEFT_RUN:
            self.x = max(0, self.x - speed)
            self.y = min(600, self.y - speed)
        elif self.state == self.DOWN_RIGHT_RUN:
            self.x = min(800, self.x + speed)
            self.y = min(600, self.y - speed)
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, frame * 100, 100, 100, self.x, self.y)


def handle_events():
    global running
    global hero
    global speed
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            speed = 10
        elif event.type == SDL_KEYUP and event.key == SDLK_SPACE:
            speed = 5
        else:
            hero.handle_event(event)
            pass


def main():

    open_canvas()

    global hero
    global running

    hero = Hero()
    grass = Grass()

    running = True
    while running:
        handle_events()

        hero.update()

        clear_canvas()
        grass.draw()
        hero.draw()
        update_canvas()

        delay(0.04)

    close_canvas()


if __name__ == '__main__':
    main()