import pygame as pg
from random import randint

class Circle:
    def __init__(self, x, y, rad, col=(0, 0, 0)):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.y -= 1
        if keys[pg.K_DOWN]:
            self.y += 1
        if keys[pg.K_LEFT]:
            self.x -= 1
        if keys[pg.K_RIGHT]:
            self.x += 1

    def draw(self, win):
        pg.draw.circle(win, self.col, (self.x, self.y), self.rad)

    def horizontal_movement(self):
        self.x += 1
        if self.x > W:
            self.x = 0

W = 500
H = 500
FPS = 60

list_circles = []
for i in range(100):
    circle = Circle(i * 10, i * 5, 50, (randint(0, 255), randint(0, 255), randint(0, 255)))
    list_circles.append(circle)

pg.init()
win = pg.display.set_mode((W, H))
clock = pg.time.Clock()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    for i in range(100):
        list_circles[i].horizontal_movement()

    win.fill((255, 255, 255))
    for i in range(100):
        list_circles[i].draw(win)
    pg.display.update()
    clock.tick(FPS)
