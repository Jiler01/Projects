import pyxel as px
from random import randint

class Enemi:
    def __init__(self,speed):
        self.x = randint(0, px.width - 8)
        self.y = 0
        self.w,self.h = 8,8
        self.speed = speed
        self.alive = True

    def draw(self):
        px.rect(self.x,self.y,self.w,self.h,px.COLOR_PEACH)

    def update(self):
        self.y += self.speed