from Settings import *
import pygame as pg
import random

class Coin(pg.sprite.Sprite):
    def __init__(self,x,y,game,color):
        pg.sprite.Sprite.__init__(self)
        #self.coin_get()
        self.x = x
        self.y = y

        MATRIX[y][x] = 3

        self.image = pg.Surface((WIDTH/len(MATRIX[0]), HEIGHT/len(MATRIX)))
        self.image.fill(color)
        self.rect = self.image.get_rect()
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
#self.x y self.y no funcan, gurdar las posiciones en las que esta la moneda en la matrix :3 creo (?)
