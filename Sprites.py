from Settings import *
import pygame as pg
import random

vec = pg.math.Vector2

class PacMan(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.alive = True
        self.x = x
        self.y = y
        self.prev_x = self.x
        self.prev_y = self.y

        MATRIX[y][x] = 1

        self.image = pg.Surface((WIDTH/len(MATRIX[0]), HEIGHT/len(MATRIX)))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.update()

    def left(self):
        self.prev_x = self.x
        self.prev_y = self.y

        self.x -= 1

        self.update()

    def right(self):
        self.prev_x = self.x
        self.prev_y = self.y

        self.x += 1

        self.update()

    def up(self):
        self.prev_y = self.y
        self.prev_x = self.x

        self.y -= 1

        self.update()

    def down(self):
        self.prev_y = self.y
        self.prev_x = self.x

        self.y += 1

        self.update()

    def update(self):

        x = self.updateX()
        y = self.updateY()

        if self.x > len(MATRIX[0])+1:           #Cambios
            self.x = 0
        elif self.x < 0:
            self.x = len(MATRIX[0])+1

        if self.y > len(MATRIX):
            self.y = 0
        elif self.y < 0:
            self.y = len(MATRIX)

        self.rect.topleft = (x,y)

    def updateX(self):
        posX = (WIDTH/len(MATRIX[0])-1)*self.x
        return posX


    def updateY(self):
        posY = (HEIGHT/len(MATRIX)-1)*self.y
        return posY

class PacManEvil(pg.sprite.Sprite):
    def __init__(self, x, y, game, color):
        pg.sprite.Sprite.__init__(self)
        self.alive = True
        self.x = x
        self.y = y
        self.prev_x = self.x
        self.prev_y = self.y
        self.now=0

        MATRIX[y][x] = 2

        self.image = pg.Surface((WIDTH/len(MATRIX[0]), HEIGHT/len(MATRIX)))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.now = 0

        self.update()



    def left(self):
        self.prev_x = self.x
        self.prev_y = self.y

        self.x -= 1

        self.update()

    def right(self):
        self.prev_x = self.x
        self.prev_y = self.y

        self.x += 1

        self.update()

    def up(self):
        self.prev_y = self.y
        self.prev_x = self.x

        self.y -= 1

        self.update()

    def down(self):
        self.prev_y = self.y
        self.prev_x = self.x

        self.y += 1

        self.update()

    def update(self):

        x = self.updateX()
        y = self.updateY()

        if self.x > len(MATRIX[0])-1:
            self.x = 0
        elif self.x < 0:
            self.x = len(MATRIX[0])-1

        if self.y > len(MATRIX)-1:
            self.y = 0
        elif self.y < 0:
            self.y = len(MATRIX)-1

        self.rect.topleft = (x,y)

    def updateX(self):
        posX = (WIDTH/len(MATRIX[0])-1)*self.x
        return posX

    def updateY(self):
        posY = (HEIGHT/len(MATRIX)-1)*self.y
        return posY

    def mov(self):
        lista = [self.left, self.right, self.up, self.down]
        time= pg.time.get_ticks()

        if time-self.now > 250:
            self.now = time

            mov = random.choice(lista)
            mov()
        else:
            pass

        MATRIX[self.prev_y][self.prev_x] = 0
        MATRIX[self.y][self.x] = 2
