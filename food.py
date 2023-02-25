from component import Component
from constant import IDs, Foods

class Food(Component):
    def __init__(self, food_id, x, y):
        Component.__init__(self, id=IDs["FOOD"], x=x, y=y, img="#FA0")
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