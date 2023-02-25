from food import Food
from constant import IDs, Foods

class Chrono_pomme(Food):
    def __init__(self, x, y):
        Food.__init__(self, food_id=IDs["Chrono_pomme"], x=x, y=y, img="#00F")
        self.__food_id = Foods[IDs["Chrono_pomme"]]
    
    