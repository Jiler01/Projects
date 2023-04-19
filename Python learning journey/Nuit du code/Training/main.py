import pyxel as px
from vaisseau import Vaisseau
from enemi import Enemi
from collide import collide

class App:
    def __init__(self,fps=60):
        self.vaisseau = Vaisseau()
        self.enemis = []
        self.score = 0
        self.s = fps

        px.init(128, 128, title="My Fist App",fps=fps)
        px.run(self.update, self.draw)

    def update(self):
        self.vaisseau.update()
        if px.frame_count % self.s*3 == 0:
            self.enemis.append(Enemi(0.25))
        if px.frame_count % self.s*10 == 0:
            self.enemis.append(Enemi(0.5))

        for enemi in self.enemis:
            if collide(enemi, self.vaisseau):
                print(self.score)
                px.quit()
                exit()
            for tir in self.vaisseau.tirs:      
                if collide(tir, enemi):
                    self.enemis.remove(enemi)
                    self.vaisseau.tirs.remove(tir)
                    self.score +=1
            enemi.update()
        

    def draw(self):
        px.cls(0)
        self.vaisseau.draw()
        for enemi in self.enemis:
            enemi.draw()

App(fps=30)