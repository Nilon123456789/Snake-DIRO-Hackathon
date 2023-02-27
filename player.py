from constant import IDs, Direction
from component import Component
from sprites import Player as SpritePlayer



class Player(Component):

    def __init__(self, x, y, userId):
        Component.__init__(self, id=IDs["PLAYER_HEAD"], x=x, y=y, img=SpritePlayer.top_head())
        self.__body = []
        self.__direction = Direction["UP"]
        self.__pointage = 0
        self.__highscore = 0
        self.userId = userId
    
    @property
    def body(self):
        return self.__body
    
    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, direction):

        if self.__direction == Direction["UP"]:
            self.img = SpritePlayer.top_head()
        elif self.__direction == Direction["DOWN"]:
            self.img = SpritePlayer.bottom_head()
        elif self.__direction == Direction["LEFT"]:
            self.img = SpritePlayer.left_head()
        elif self.__direction == Direction["RIGHT"]:
            self.img = SpritePlayer.right_head()

        self.__direction = direction
    
    def add_body(self, body):
        self.__body.insert(0, body)

    @property
    def pointage(self):
        return self.__pointage
    
    @pointage.setter
    def pointage(self, pointage):
        self.__pointage = pointage

    def add_pointage(self, pt):
        self.__pointage += pt
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id == id

    @property
    def highscore(self):
        return self.__highscore
    
    @highscore.setter
    def highscore(self, highscore):
        self.__highscore = highscore
    
    
    