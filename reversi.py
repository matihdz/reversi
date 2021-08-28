import cocos
class Laberinto:
    def __init__(self):
        self.sprite=cocos.sprite.Sprite("resources/reversi.png")
        self.sprite.position=270,270
        self.mapa= [
            [0,0,0,0,0,0,0,0,0],
            [0,1,0,1,1,1,0,1,0],
            [0,0,0,0,0,0,0,0,0],
            [1,1,0,1,0,1,0,1,1],
            [0,1,0,1,1,1,0,1,0],
            [0,1,0,0,0,0,0,1,0],
            [0,0,0,1,1,1,0,0,0],
            [0,1,0,1,0,1,0,1,0],
            [0,0,0,0,0,0,0,0,0]
        ]
