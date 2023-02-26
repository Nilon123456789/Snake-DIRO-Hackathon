from component import Component
from constant import IDs, Foods
from sprites import Apple as apple_sprite

class Food(Component):
    def __init__(self, food_id, x, y):
        apple_img = apple_sprite.apple()
        if (food_id == Foods["POMME_10"]):
            apple_img = apple_sprite.golden()
        elif (food_id == Foods["RETRECIR"]):
            apple_img = apple_sprite.shrink()
        elif (food_id == Foods["POISON"]):
            apple_img = apple_sprite.poison()
        elif (food_id == Foods["VITESSE"]):
            apple_img = apple_sprite.speed()
        elif (food_id == Foods["POMME_BLOC"]):
            apple_img = apple_sprite.block()
        elif (food_id == Foods["CHRONO_POMME"]):
            apple_img = apple_sprite.chrono()
        
        
        Component.__init__(self, id=IDs["FOOD"], x=x, y=y, img=apple_img)
        self.__food_id = food_id
    
    @property
    def food_id(self):
        return self.__food_id
    
    @property
    def points(self):
        points = 1
        if (self.__food_id == Foods["POMME_10"]):
            points = 10
        return points