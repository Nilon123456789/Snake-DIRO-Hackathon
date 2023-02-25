from constant import IDs, Direction
from component import Component



class Player(Component):

    def __init__(self, x, y):
        Component.__init__(self, id=IDs["PLAYER_HEAD"], x=x, y=y, img='#F00')
        self.__body = []
        self.__direction = Direction["UP"]
        self.__pointage = 0
    
    @property
    def body(self):
        return self.__body
    
    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, direction):
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
    
    
    