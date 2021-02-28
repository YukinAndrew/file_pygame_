import pygame as pg

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
        pg.display.update()

W = 500
H = 500

pg.init()
win = pg.display.set_mode((W, H))
circle = Circle(W // 2, H // 2, 50)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg,quit()
            exit()

    circle.movement()

    win.fill((255, 255, 255))
    circle.draw(win)
    pg.display.update()