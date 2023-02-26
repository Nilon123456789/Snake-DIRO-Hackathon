from component import Component
from constant import IDs
from sprites import Wall as wall_sprite
 
class Wall(Component):
        def __init__(self, x, y):
            Component.__init__(self, id=IDs["WALL"], x=x, y=y, img=wall_sprite.wall())