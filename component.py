from constant import IDs

class Component:

    def __init__(self, id, x, y, img):
        self.__id = id
        self.__x = x
        self.__y = y
        self.__img = img

    @property
    def id(self):
        return self.__id
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y
    
    @property
    def img(self):
        return self.__img
    
    def newPos(self, x, y):
        self.__x = x
        self.__y = y
