from food import Food
import random
from constant import Foods

class Chrono_pomme(Food):
    def __init__(self, x, y, chrono_apples_list, current_time):
        Food.__init__(self, food_id=Foods["CHRONO_POMME"], x=x, y=y)
        chrono_apples_list.append(self)
        self.__quit_time = current_time + random.randint(25, 120)

    @property
    def quit_time(self):
        return self.__quit_time
    
    