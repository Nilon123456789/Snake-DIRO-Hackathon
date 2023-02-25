from component import Component
from player import Player

class Tail(Component):

    def __init__(self, head, x, y):
        Component.__init__(self,id=2, x=x, y=y, img="#0F0")
        self.__head = head
        head.add_body(self)
    
    def set_as_end(self):
        self.__end = True
        self.__img = "#0FF"