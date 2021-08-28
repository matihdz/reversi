import cocos2d
class Tablero:
    def __init__(self):
        self.sprite=cocos2d.sprite.Sprite("resources/reversi.png")
        self.sprite.position=270,270
        self.mapa= [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
        ]
