import ttgo as dev
from component import Component
from constant import IDs, Maps
from game_matrix import GameMatrix
from bg import bg_grass, bg_map1
from sprites import Wall 
import random


class Map():

    def __init__(self):
        self.block = 10
        self.width = dev.screen_width // self.block # 135 pixels
        self.height = (dev.screen_height - 20) // self.block # 230 pixels
        self.__map_list = Maps
        self.map_matrix = []

        self.init_matrix()



    def init_matrix(self):
        for i in range(self.height):
            self.map_matrix.append([])

            for j in range(self.width):
                self.map_matrix[i].append(Component(0, 0, 0, bg_grass))

    def add_block_wall(self, x, y):
        self.map_matrix[10][10] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[10][11] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[10][12] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[10][13] = Component(6, 0, 0, Wall.tree_wall())

        self.map_matrix[11][10] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[11][11] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[11][12] = Component(6, 0, 0, Wall.tree_wall())

        self.map_matrix[12][13] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[12][14] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[12][15] = Component(6, 0, 0, Wall.tree_wall())

        self.map_matrix[10][10] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[10][11] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[10][12] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[10][13] = Component(6, 0, 0, Wall.tree_wall())

        self.map_matrix[11][10] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[11][11] = Component(6, 0, 0, Wall.tree_wall())
        self.map_matrix[11][12] = Component(6, 0, 0, Wall.tree_wall())
        
        return self.map_matrix()

            



                            


        
                




        
        





