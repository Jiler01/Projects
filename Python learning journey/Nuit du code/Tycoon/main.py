import pyxel as px

class App:
    def __init__(self,fps=60,window_size:dict={"x":120 ,"y":120}):
        px.init(window_size["x"],window_size["y"],fps=fps,title="Little Tycoon")
        px.load("PYXEL_RESSOURCE_FILE.pyxres")
        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        px.bltm(0,0,0,0,0,256,256,px.COLOR_BLACK)

App()