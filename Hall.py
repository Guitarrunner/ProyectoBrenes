from Settings import *
import pygame as pg
import random
import string
import sys
from os import path

class Hall():
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption("Hall of Fame")
        self.clock= pg.time.Clock()
        self.counter = 0
        self.now = 0
        self.running= True
        self.AArray = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.i = 0
        self.final = []
        self.Let = self.AArray[self.i]
        self.font_name = pg.font.match_font('arial')

    def run(self):
        self.playing = True
        while self.playing:
            if len(self.final) == 3:
                self.dir = path.dirname(__file__)
                with open(path.join(self.dir,HF_FILE),'a') as f:
                    f.write(str(self.final)+"\n")
                self.final = []
            self.clock.tick(60)
            self.events()
            self.draw()
        pg.quit()
    def events(self):
        for event in pg.event.get():

        # check for closing window
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        time = pg.time.get_ticks()

        if time - self.now > 500:
            keys= pg.key.get_pressed()
            if keys[pg.K_UP]:
                self.i += 1
                if self.i > len(self.AArray)-1:
                    self.i = 0
                elif self.i < 0:
                    self.i =  len(self.AArray)-1
                self.Let = self.AArray[self.i]
                self.now = time
            if keys[pg.K_DOWN]:
                self.i -= 1
                if self.i > len(self.AArray)-1:
                    self.i = 0
                elif self.i < 0:
                    self.i = len(self.AArray)-1
                self.Let = self.AArray[self.i]
                self.now = time
            if keys[pg.K_SPACE]:
                self.final.append(self.Let)
                self.now = time
    def draw(self):
        self.screen.fill((255,0,0))
        self.draw_text(str(self.Let),22,WHITE,WIDTH/2,15)
        self.draw_text(("".join(self.final)),22,WHITE,WIDTH/2,50)
        pg.display.flip()

    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)
g = Hall()
while g.running:
    g.run()
