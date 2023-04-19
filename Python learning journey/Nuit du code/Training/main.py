import pyxel as px
import time
from vaisseau import Vaisseau
from enemi import Enemi
from explosion import Explosion
from collide import collide

class App:
    def __init__(self,fps=60):
        self.f = open("bestscore.dat","r")
        self.bestscore = int(self.f.readline())
        print(self.bestscore)
        self.vaisseau = Vaisseau(vies=3)
        self.enemis = []
        self.explosions = []
        self.score = 0
        self.s = fps

        px.init(128, 128, title="My Fist App",fps=fps)
        px.run(self.update, self.draw)

    def update(self):
        self.vaisseau.update()

        for explosion in self.explosions:
            if explosion.update():
                self.explosions.remove(explosion)

        {3:0.25,9:0.5,27:1}
        for frame_num,speed in {3:0.25,9:0.5}.items():
            if px.frame_count % self.s*frame_num == 0:
                self.enemis.append(Enemi(speed))

        for enemi in self.enemis:
            if collide(enemi, self.vaisseau) or enemi.y>128:
                self.vaisseau.vies-=1
                self.enemis.remove(enemi)
                self.explosions.append(Explosion(enemi.x+enemi.w,enemi.y+enemi.h,6,3))
                self.explosions.append(Explosion(self.vaisseau.x+self.vaisseau.w,self.vaisseau.y+self.vaisseau.h,6,3))
            for tir in self.vaisseau.tirs:      
                if collide(tir, enemi):
                    self.enemis.remove(enemi)
                    self.vaisseau.tirs.remove(tir)
                    self.score +=1
                    self.explosions.append(Explosion(enemi.x+enemi.w,enemi.y+enemi.h,12,6))
            enemi.update()
        

    def draw(self):
        px.cls(0)
        if self.vaisseau.vies>=0:

            for explosion in self.explosions:
                explosion.draw()
            self.vaisseau.draw()
            for enemi in self.enemis:
                enemi.draw()
            px.text(5,5, 'VIES:'+ str(self.vaisseau.vies), 7)
            px.text(5,15, 'SCORE:'+ str(self.score), 7)
        else:
            px.text(5,5, f'GAME OVER\nSCORE: {self.score}', 7)
            if self.bestscore < self.score:
                self.f = open("bestscore.dat","w")
                self.f.write(str(self.score))
                self.f.close
                px.text(5,25,"NEW BESTSCORE !!",px.COLOR_LIME)
        

App()                        