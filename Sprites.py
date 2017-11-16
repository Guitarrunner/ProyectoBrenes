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
<<<<<<< HEAD:Player.py

class Pill(pg.sprite.Sprite):
    def __init__(self, x, y, game, color):
        pg.sprite.Sprite.__init__(self)
        self.alive = True
        self.x = x
        self.y = y
        self.prev_x = self.x
        self.prev_y = self.y
        self.now=0

        MATRIX[y][x] = 3

        self.image = pg.Surface((WIDTH/len(MATRIX[0]), HEIGHT/len(MATRIX)))
        self.image.fill(color)
        self.rect = self.image.get_rect()


        self.update()

    def updateX(self):
        posX = (WIDTH/len(MATRIX[0])-1)*self.x
        return posX

    def updateY(self):
        posY = (HEIGHT/len(MATRIX)-1)*self.y
        return posY

class Chaser(pg.sprite.Sprite):
    def __init__(self, x, y, game, color):
        pg.sprite.Sprite.__init__(self)
        self.alive = True
        self.x = x
        self.y = y
        self.prev_x = self.x
        self.prev_y = self.y
        self.now=0

        self.game = game

        self.player = self.game.player

        MATRIX[y][x] = 9

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

    def leftdown(self):
        self.prev_x = self.x
        self.prev_y = self.y

        self.x -= 1
        self.y += 1

        self.update()

    def rightdown(self):
        self.prev_x = self.x
        self.prev_y = self.y

        self.x += 1
        self.y += 1

        self.update()

    def leftup(self):
        self.prev_y = self.y
        self.prev_x = self.x

        self.y -= 1
        self.x -= 1

        self.update()

    def rightup(self):
        self.prev_y = self.y
        self.prev_x = self.x

        self.x += 1
        self.y -= 1

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
        self.mov()
    def updateX(self):
        posX = (WIDTH/len(MATRIX[0])-1)*self.x
        return posX

    def updateY(self):
        posY = (HEIGHT/len(MATRIX)-1)*self.y
        return posY

    def mov(self):
        lista = [self.left, self.right, self.up, self.down, self.leftup, self.leftdown, self.rightup, self.rightdown]
        time= pg.time.get_ticks()



        if time-self.now > 250:
            self.now = time


            mov1 = calcDis(self.player.x,self.player.y,self.x,self.y+1)
            mov2 = calcDis(self.player.x,self.player.y,self.x,self.y-1)
            mov3 = calcDis(self.player.x,self.player.y,self.x+1,self.y)
            mov4 = calcDis(self.player.x,self.player.y,self.x-1,self.y)

            mov5 = calcDis(self.player.x,self.player.y,self.x+1,self.y+1)
            mov6 = calcDis(self.player.x,self.player.y,self.x-1,self.y-1)
            mov7 = calcDis(self.player.x,self.player.y,self.x+1,self.y-1)
            mov8 = calcDis(self.player.x,self.player.y,self.x-1,self.y+1)

            movs= {mov1,mov2,mov3,mov4,mov5,mov6,mov7,mov8}

            sig = min(movs)

            if sig == mov1:
                self.down()
            elif sig == mov2:
                self.up()
            elif sig == mov3:
                self.right()
            elif sig == mov4:
                self.left()
            elif sig == mov5:
                self.rightdown()
            elif sig == mov6:
                self.leftup()
            elif sig == mov7:
                self.rightup()
            elif sig == mov8:
                self.leftdown()
            print(sig)


        else:
            pass

        MATRIX[self.prev_y][self.prev_x] = 0
        MATRIX[self.y][self.x] = 9
=======
>>>>>>> cd0b330b6d2344c94715aee143b30989d8e0e597:Sprites.py
