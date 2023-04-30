import pyxel as px

class App:
    def __init__(self,fps=60,window_size:dict={"x":128 ,"y":128}):
        px.init(window_size["x"],window_size["y"],fps=fps,title="Little Tycoon")
        px.load("PYXEL_RESSOURCE_FILE.pyxres")
        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        px.cls(px.COLOR_BLACK)