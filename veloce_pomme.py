from food import Food
import random
from constant import Foods

class Veloce_Pomme(Food):
    def __init__(self, x, y, veloce_apples_list, current_time):
        Food.__init__(self, food_id=Foods["VELOCE"], x=x, y=y)
        veloce_apples_list.append(self)
        self.__move_time = current_time + random.randint(15, 120)

    @property
    def move_time(self):
        return self.__move_time
    
    def set_move_time(self, current_time):
        self.__move_time = current_time + random.randint(15, 120)
    
    
    