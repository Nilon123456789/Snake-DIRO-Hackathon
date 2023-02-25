import ttgo as dev
from component import Component
from constant import IDs, Maps
from game_matrix import GameMatrix


class Map():

    def __init__(self):
        self.__map_list = Maps
        self.map_matrix = []
        self.block = 10
        self.width = dev.screen_width // self.block # 135 pixels
        self.height = (dev.screen_height - 20) // self.block # 230 pixels


    def init_matrix(self):
        for i in range(self.width):
            for j in range(self.height):
                
    
    # Carte 
    def island_map(self):
        pass

    def ice_map(self):
        pass

    def forest_map(self):
        pass


