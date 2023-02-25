from component import Component
from constant import IDs

class Wall(Component):
    
        def __init__(self, x, y):
            Component.__init__(self, id=IDs["WALL"], x=x, y=y, img="#000")