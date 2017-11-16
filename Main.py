import pygame as pg
import random
from Settings import *
import Sprites as Player
import Coin
import sys


class Game():
    def __init__(self):
        #Inicia la ventana y demas
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock= pg.time.Clock()
        self.running= True
        self.now = 0
        self.coins= 0


    def new(self):
        #Inicia el juego

        self.creationTimer = 0

        self.player = Player.PacMan(0, 0)

        self.all_sprites= pg.sprite.Group()

        self.evil_sprites = pg.sprite.Group()

        #My shit
        self.coin_sprites = pg.sprite.Group()
        #End of my shit

        self.pill_sprites = pg.sprite.Group()

        self.all_sprites.add(self.player)


        self.run()


    def run(self):
        #Loop del juego
        self.playing= True

        while self.playing:
            #Mantains the speed
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            for i in self.evil_sprites:
                if self.player.updateX()== i.updateX() and self.player.updateY()== i.updateY():
                    print ("Choque")
                    pg.quit()
            for i in self.coin_sprites:
                if self.player.updateX()== i.updateX() and self.player.updateY()== i.updateY():
                    print ("Coin up")
                    i.kill()
                    self.coins+=1
                    q = Coin.Coin(random.randrange(0,30),random.randrange(0,30),self, YELLOW)
                    self.coin_sprites.add(q)
                    self.all_sprites.add(q)
                    print("COINER")
                    print(self.coins)
            if self.coins == 20:
                i= Coin.Coin(random.randrange(0,30),random.randrange(0,30),self, PURPLE)
                self.pill_sprites.add(i)
                self.all_sprites.add(i)
                self.coins=0

            for i in self.pill_sprites:
                if self.player.updateX()== i.updateX() and self.player.updateY()== i.updateY():
                    print ("Pill up")
                    i.kill()

        pg.quit()

    def events(self):
        for event in pg.event.get():

        # check for closing window
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        time = pg.time.get_ticks()

        if time - self.now > WAIT:
            keys= pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.player.left()
                self.now = time

            if keys[pg.K_RIGHT]:
                self.player.right()
                self.now = time

            if keys[pg.K_UP]:
                self.player.up()
                self.now = time

            if keys[pg.K_DOWN]:
                self.player.down()
                self.now = time

    def update(self):
        time = pg.time.get_ticks()

        if time - self.creationTimer > 1000:
            pass

            if len(self.evil_sprites) < 10:
                i = Player.PacManEvil(random.randrange(0,30),random.randrange(0,30),self, random.choice(COLORS))

                self.evil_sprites.add(i)
                self.all_sprites.add(i)
                print("Creado")

                self.creationTimer = time
        if time - self.creationTimer > 10:
            if len(self.coin_sprites) < 10:
                i = Coin.Coin(random.randrange(0,30),random.randrange(0,30),self,YELLOW)
                self.coin_sprites.add(i)
                self.all_sprites.add(i)
                print("COINER")
                self.creationTimer = time

        for i in self.evil_sprites:
            i.mov()
            i.update()
        self.player.update()


    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

g= Game()


while g.running:
    g.new()

pg.quit()
