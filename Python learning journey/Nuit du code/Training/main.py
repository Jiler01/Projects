import pyxel as px
from vaisseau import Vaisseau
from enemi import Enemi
from collide import collide

class App:
    def __init__(self):
        self.vaisseau = Vaisseau()
        self.enemis = []
        self.score = 0

        px.init(128, 128, title="My Fist App")
        px.run(self.update, self.draw)

    def update(self):
        self.vaisseau.update()
        if px.frame_count % 300 == 0:
            self.enemis.append(Enemi(0.5))
        if px.frame_count % 1000 == 0:
            self.enemis.append(Enemi(1))

        for enemi in self.enemis:
            if collide(enemi, self.vaisseau):
                px.quit()
                print(self.score)
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

App()