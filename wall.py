from component import Component
from constant import IDs
from sprites import Wall as wall_sprite
 
class Wall(Component):
    def __init__(self, x, y, wall_id=0):
        Component.__init__(self, id=IDs["WALL"], x=x, y=y, img=wall_sprite.get_wall(wall_id))

