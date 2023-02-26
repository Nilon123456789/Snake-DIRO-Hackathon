from component import Component
from sprites import Tail as tailSprite
from constant import IDs

class Tail(Component):

    def __init__(self, head, x, y, img):
        Component.__init__(self,id=IDs["PLAYER_BODY"], x=x, y=y, img=img)
        self.__head = head
        self.__end = False
        head.add_body(self)
    
    def set_as_end(self, beforeX, beforeY):
        if (beforeX < self.__x):
            self.__img = tailSprite.right_tail()
        elif (beforeX > self.__x):
            self.__img = tailSprite.left_tail()
        elif (beforeY < self.__y):
            self.__img = tailSprite.bottom_tail()
        elif (beforeY > self.__y):
            self.__img = tailSprite.top_tail()
        self.__end = True
    
    @property
    def end(self):
        return self.__end