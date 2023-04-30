import pyxel as px

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8

        self.wallet = {"gallions":0,"noises":0,"mornilles":0}

        self.skins = {"0": {"left":px.blt(self.x,self.y,0,0,0,8,8,px.COLOR_BLACK),  "right":px.blt(self.x,self.y,0,8,0,8,8,px.COLOR_BLACK)},
                      "10":{"left":px.blt(self.x,self.y,0,0,8,8,8,px.COLOR_BLACK),  "right":px.blt(self.x,self.y,0,8,8,8,8,px.COLOR_BLACK)},
                      "20":{"left":px.blt(self.x,self.y,0,0,16,8,8,px.COLOR_BLACK), "right":px.blt(self.x,self.y,0,8,16,8,8,px.COLOR_BLACK)}}
        self.eyeSide = "right"

        self.xp = 0
        self.__lastxp = 250
        self.level = 0

        self.flags = {"levelup":0}
        
    def update(self,*,allowRight,allowLeft,allowUp,allowDown):
        if px.btn(px.KEY_LEFT):
            self.eyeSide = "left"
            if allowLeft:self.x -= 2
        if px.btn(px.KEY_RIGHT):
            self.eyeSide = "right"
            if allowRight: self.x += 2
        if px.btn(px.KEY_UP) and allowUp:
            self.y -= 2
        if px.btn(px.KEY_DOWN) and allowDown:
            self.y += 2

        if self.xp >= self.__lastxp*2:
            self.__lastxp = self.__lastxp *2
            self.level += 1
            self.on("levelup")
            self.xp = self.xp - self.__lastxp

    def draw(self):
        for levelrequired in self.skins.keys():
            if self.level >= int(levelrequired):
                todraw = self.skins[levelrequired]

        todraw[self.eyeSide]()

    def on(self, flag:str, val:int=1):
        self.flags[flag] = val
    
    def off(self, flag:str, val:int=None):
        if val is None: self.flags[flag] = 0
        else: self.flags[flag]-=val

    def transaction(self, gallions:int=0, noises:int=0, mornilles:int=0):
        if self.wallet["gallions"] > gallions and self.wallet["noises"] > noises and self.wallet["mornilles"] > mornilles:
            self.wallet["gallions"] -= gallions
            self.wallet["noises"] -= noises
            self.wallet["mornilles"] -= mornilles
            return True
        else:
            return False