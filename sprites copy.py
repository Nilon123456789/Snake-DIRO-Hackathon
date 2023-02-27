from constant import Direction

class Apple:
    def apple():
        return """                                        
                        #0e5            
        #f04#f04#f04#0e5#f04#f04        
    #f04#ffe#f7a#f04#f04#f04#f04#b04    
    #f04#f7a#f04#f04#f04#f04#f04#b04    
    #f04#f04#f04#f04#f04#f04#f04#b04    
    #f04#f04#f04#f04#f04#f04#f04#b04    
        #b04#f04#f04#f04#f04#b04        
            #b04#b04#b04#b04            
                                        """

    def poison():
        return """                                        
                        #0e5            
        #6b7#6b7#6b7#0e5#6b7#6b7        
    #6b7#ffe#aba#6b7#6b7#6b7#6b7#474    
    #6b7#aba#6b7#6b7#6b7#6b7#6b7#474    
    #6b7#6b7#6b7#6b7#6b7#6b7#6b7#474    
    #6b7#6b7#6b7#6b7#6b7#6b7#6b7#474#8f0
    #8f0#474#6b7#6b7#6b7#6b7#474#8f0#8f0
    #8f0#8f0#474#474#474#474#8f0#6c0#6c0
        #8f0#8f0#8f0#8f0#8f0#8f0#6c0    """

    def golden():
        return """                                        
                        #0e5            
        #fd1#fd1#fd1#0e5#fd1#fd1        
    #fd1#ffe#fe9#fd1#fd1#fd1#fd1#db1    
    #fd1#fe9#fd1#fd1#fd1#fd1#fd1#db1    
    #fd1#fd1#fd1#fd1#fd1#fd1#fd1#db1    
    #fd1#fd1#fd1#fd1#fd1#fd1#fd1#db1    
        #db1#fd1#fd1#fd1#fd1#db1        
            #db1#db1#db1#db1            
                                        """

    def speed():
        return """                                        
                        #0e5            
        #f04#f04#f04#0e5#f04#b04        
    #f04#ffe#f7a#f04#f04#f04#f04#b04        
    #f04#f7a#f04#f04#f04#f04#f04#b04    
    #f04#f04#f04#f04#f04#0ff#f04#b04    
    #f04#f04#f04#f04#f04#0ff#0ff#b04    
        #f04#0ff#0ff#0ff#0ff#0ff#0bc    
            #b04#b04#b04#0ff#0bc        
                        #0bc            """
    def shrink():
        return """                                        
                        #0e5            
        #b04#b04#b04#0e5#b04#b04        
        #fc4#f04#f04#f04#f04#fc4#fd6    
    #fd6#fd6#fc4#f04#f04#fc4#fd6#fd6    
    #fd6#fd6#fc4#f04#f04#fc4#fd6#fd6    
    #fd6#fd6#f04#f04#f04#fc4#fd6#fd6    
        #b04#f04#f04#f04#f04#fc4        
            #b04#b04#b04#b04            
                                        """
    def block():
        return """                                        
    #b04#b04#b04#b04#b04#0e5#b04#b04    
    #b04#f04#f04#f04#0e5#f04#f04#b04    
    #b04#ffe#f7a#f04#f04#f04#f04#b04    
    #b04#f7a#f04#f04#f04#f04#f04#b04    
    #b04#f04#f04#f04#f04#f04#f04#b04    
    #b04#f04#f04#f04#f04#f04#f04#b04    
    #b04#f04#f04#f04#f04#f04#f04#b04    
    #b04#b04#b04#b04#b04#b04#b04#b04    
                                        """
    def chrono():
        return """                                        
                        #0e5            
        #f04#f04#f04#0e5#f04#b04        
    #f04#ffe#f7a#f04#f04#f04#f04#b04    
    #f04#f7a#f04#f04#000#000#000#000    
    #f04#f04#f04#000#fff#fff#fff#000#000
    #f04#f04#f04#000#fff#fff#000#fff#000
        #f04#f04#000#fff#fff#000#000#000
            #b04#000#fff#fff#fff#fff#000
                    #000#000#000#000    """

class Body:
    def vertical():
        return """    #300#732#943#943#943#943#732#300    
    #300#732#943#943#943#943#732#300    
    #300#843#a64#a64#a64#a64#843#300    
    #300#843#a64#a64#a64#a64#843#300    
    #300#732#943#943#943#943#732#300    
    #300#732#943#943#943#943#732#300    
    #300#843#a64#a64#a64#a64#843#300    
    #300#843#a64#a64#a64#a64#843#300    
    #300#732#943#943#943#943#732#300    
    #300#732#943#943#943#943#732#300    """
    def horizontal():
        return """                                        
#300#300#300#300#300#300#300#300#300#300
#732#732#843#843#732#732#843#843#732#732
#943#943#a64#a64#943#943#a64#a64#943#943
#943#943#a64#a64#943#943#a64#a64#943#943
#943#943#a64#a64#943#943#a64#a64#943#943
#943#943#a64#a64#943#943#a64#a64#943#943
#732#732#843#843#732#732#843#843#732#732
#300#300#300#300#300#300#300#300#300#300
                                        """
    def top_left_corner():
        return """
                #300#300#300#300#300#300
            #300#732#732#843#843#732#732
        #300#843#943#943#a64#a64#a64#943
    #300#732#943#943#943#943#a64#a64#943
    #300#732#943#943#943#943#a64#a64#943
    #300#843#a64#943#943#943#943#a64#943
    #300#843#a64#a64#a64#943#943#a64#843
    #300#732#a64#a64#a64#a64#a64#732#300
    #300#732#943#943#943#943#843#300    """
    def top_right_corner():
        return """
    #300#300#300#300#300#300            
    #732#732#843#843#732#732#300        
    #943#a64#a64#a64#943#943#843#300    
    #943#a64#a64#943#943#943#943#732#300
    #943#a64#a64#943#943#943#943#732#300
    #943#a64#943#943#943#943#a64#843#300
    #843#a64#943#943#a64#a64#a64#843#300
    #300#732#a64#a64#a64#a64#a64#732#300
        #300#843#943#943#943#943#732#300"""
    def bottom_left_corner():
        return """    #300#732#943#943#943#943#843#300    
    #300#732#a64#a64#a64#a64#a64#732#300
    #300#843#a64#a64#a64#943#943#a64#843
    #300#843#a64#943#943#943#943#a64#943
    #300#732#943#943#943#943#a64#a64#943
    #300#732#943#943#943#943#a64#a64#943
        #300#843#943#943#a64#a64#a64#943
            #300#732#732#843#843#732#732
                #300#300#300#300#300#300"""
    def bottom_right_corner():
        return """        #300#843#943#943#943#943#732#300
    #300#732#a64#a64#a64#a64#a64#732#300
    #843#a64#943#943#a64#a64#a64#843#300
    #943#a64#943#943#943#943#a64#843#300
    #943#a64#a64#943#943#943#943#732#300
    #943#a64#a64#943#943#943#943#732#300
    #943#a64#a64#a64#943#943#843#300    
    #732#732#843#843#732#732#300        
    #300#300#300#300#300#300            """

    def get_body(direction):
        if direction == Direction["LEFT"]:
            return Body.horizontal()
        elif direction == Direction["RIGHT"]:
            return Body.right_head()
        elif direction == Direction["UP"]:
            return Body.vertical()
        elif direction == Direction["DOWN"]:
            return Body.vertical()

class Player:

    def left_head():
        return """            #300#300#300#300#300        
        #300#512#512#512#512#732#300#300
    #300#512#723#723#723#723#512#732#732
#300#512#723#d94#d94#723#723#723#512#943
#300#512#723#723#723#723#723#723#723#512
#300#512#723#723#723#723#723#723#723#512
#300#512#723#d94#d94#723#723#723#512#943
    #300#512#723#723#723#723#512#732#732
        #300#512#512#512#512#732#300#300
            #300#300#300#300#300        """
    def right_head():
        return """        #300#300#300#300#300            
#300#300#732#512#512#512#512#300        
#732#732#512#723#723#723#723#512#300    
#943#512#723#723#723#d94#d94#723#512#300
#512#723#723#723#723#723#723#723#512#300
#512#723#723#723#723#723#723#723#512#300
#943#512#723#723#723#d94#d94#723#512#300
#732#732#512#723#723#723#723#512#300    
#300#300#732#512#512#512#512#300        
        #300#300#300#300#300            """
    def top_head():
        return """            #300#300#300#300            
        #300#512#512#512#512#300        
    #300#512#723#723#723#723#512#300    
#300#512#723#d94#723#723#d94#723#512#300
#300#512#723#d94#723#723#d94#723#512#300
#300#512#723#723#723#723#723#723#512#300
#300#512#723#723#723#723#723#723#512#300
#300#732#512#723#723#723#723#512#732#300
    #300#732#512#723#723#512#732#300    
    #300#732#943#512#512#943#732#300    """
    def bottom_head():
        return """    #300#732#943#512#512#943#732#300    
    #300#732#512#723#723#512#732#300    
#300#732#512#723#723#723#723#512#732#300
#300#512#723#723#723#723#723#723#512#300
#300#512#723#723#723#723#723#723#512#300
#300#512#723#d94#723#723#d94#723#512#300
#300#512#723#d94#723#723#d94#723#512#300
    #300#512#723#723#723#723#512#300    
        #300#512#512#512#512#300        
            #300#300#300#300            """


def get_head(direction):
    if direction == Direction["LEFT"]:
        return Player.left_head()
    elif direction == Direction["RIGHT"]:
        return Player.right_head()
    elif direction == Direction["UP"]:
        return Player.top_head()
    elif direction == Direction["DOWN"]:
        return Player.bottom_head()

class Tail:

    def left_tail():
        return """
                #300#300#300#300#300#300
        #300#300#743#743#632#632#743#743
    #300#632#632#a64#a64#943#943#a64#a64
#300#743#943#943#a64#a64#943#943#a64#a64
#300#743#943#943#a64#a64#943#943#a64#a64
    #300#632#632#a64#a64#943#943#a64#a64
        #300#300#743#743#632#632#743#743
                #300#300#300#300#300#300
                                        """
    def right_tail():
        return """
#300#300#300#300#300#300                
#743#743#632#632#743#743#300#300        
#a64#a64#943#943#a64#a64#632#632#300    
#a64#a64#943#943#a64#a64#943#943#743#300
#a64#a64#943#943#a64#a64#943#943#743#300
#a64#a64#943#943#a64#a64#632#632#300    
#743#743#632#632#743#743#300#300        
#300#300#300#300#300#300                
                                        """
    def top_tail():
        return """                #300#300                
            #300#743#743#300            
        #300#632#943#943#632#300        
        #300#632#943#943#632#300        
    #300#743#a64#a64#a64#a64#743#300    
    #300#743#a64#a64#a64#a64#743#300    
    #300#632#943#943#943#943#632#300    
    #300#632#943#943#943#943#632#300    
    #300#743#a64#a64#a64#a64#743#300    
    #300#743#a64#a64#a64#a64#743#300    """
    def bottom_tail():
        return """    #300#743#a64#a64#a64#a64#743#300    
    #300#743#a64#a64#a64#a64#743#300    
    #300#632#943#943#943#943#632#300    
    #300#632#943#943#943#943#632#300    
    #300#743#a64#a64#a64#a64#743#300    
    #300#743#a64#a64#a64#a64#743#300    
        #300#632#943#943#632#300        
        #300#632#943#943#632#300        
            #300#743#743#300            
                #300#300                """

                
    def get_tail(direction):
        if direction == Direction["LEFT"]:
            return Tail.left_tail()
        elif direction == Direction["RIGHT"]:
            return Tail.right_tail()
        elif direction == Direction["UP"]:
            return Tail.top_tail()
        elif direction == Direction["DOWN"]:
            return Tail.bottom_tail()

class Wall:
    
    def get_wall(id):
        if id == 1:
            return Wall.wall1()

    def wall1():
        return """#09a#09a#09a#09a#09a#09a#09a#09a#09a#09a
#09a#0cd#0cd#0cd#0cd#0cd#0cd#0cd#0cd#09a
#09a#0cd#0cd#09a#0cd#0cd#09a#0cd#0cd#09a
#09a#0cd#09a#0cd#0cd#09a#0cd#0cd#0cd#09a
#09a#0cd#0cd#0cd#09a#0cd#0cd#09a#0cd#09a
#09a#0cd#0cd#09a#0cd#0cd#09a#0cd#0cd#09a
#09a#0cd#09a#0cd#0cd#09a#0cd#0cd#0cd#09a
#09a#0cd#0cd#0cd#09a#0cd#0cd#09a#0cd#09a
#09a#0cd#0cd#0cd#0cd#0cd#0cd#0cd#0cd#09a
#09a#09a#09a#09a#09a#09a#09a#09a#09a#09a"""

    def rock_wall():
        pass

    def tree_wall():
        pass

class Portal:
    def blue():
        return """            #1ef#1ef#1ef#1ef            
        #1ef#147#147#147#147#1ef        
    #1ef#147                #147#1ef    
#1ef#147                        #147#1ef
#1ef#147                        #147#1ef
#1ef#147                        #147#1ef
#1ef#147                        #147#1ef
    #1ef#147                #147#1ef    
        #1ef#147#147#147#147#1ef        
            #1ef#1ef#1ef#1ef            """

    def orange():
        return """            #fe0#fe0#fe0#fe0            
        #fe0#f91#f91#f91#f91#fe0        
    #fe0#f91                #f91#fe0    
#fe0#f91                        #f91#fe0
#fe0#f91                        #f91#fe0
#fe0#f91                        #f91#fe0
#fe0#f91                        #f91#fe0
    #fe0#f91                #f91#fe0    
        #fe0#f91#f91#f91#f91#fe0        
            #fe0#fe0#fe0#fe0            """

class Menu:

    def title1():
        return """                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                            #f41#fc3#fc3#fc3#fc3#fc3#fc3#fc3#fc3#f00                                                                                                                                                                                                                                                #f61#fc3#fc3#f31#f00                                                                                                                                                            
                            #f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd3#f00#f00                                                                                                                                                                                                                                            #f61#fd4#fd4#f31#f00#f00                                                                                                                                                        
                            #f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd3#f00#f00#f00                                                                                                                                                                                                                                        #f61#fd4#fd4#f31#f00#f00                                                                                                                                                        
                #f41#fc3#fc3#fd3#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fc3#fc3#fc3#f00                                                                                                                                                                                                            #f00#fc3#fc3#fc3#fc3#fc3#fd3#fd4#fd4#f31#f00#f00                                                                                                                                                        
                #f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd3#f00#f00                                                                                                                                                                                                        #f00#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                                                                                                                                                        
                #f41#fd4#fd4#fc3#fb3#fb3#fb3#fb3#fb3#fd3#fd4#fd4#fb3#fb3#fa3#f00#f00#f00                                                                                                                                                                                                    #f00#fb3#fb3#fc3#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                                                                                                                                                        
    #f20#fc3#fc3#fd3#fd4#fd4#f51#f00#f00#f00#f00#f00#fa2#fd4#fd3#f00#f00#f00#f00#f00#f00                                                                                                                                                                                                    #f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                                                                                                                                                        
    #f20#fd4#fd4#fd4#fd4#fd4#f51#f00#f00#f00#f00#f00#fa2#fd4#fd3#f00#f00#f00#f00#f00#f00                                                                                                                                                                                                        #f00#f00#f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                                                                                                                                                        
    #f20#fd4#fd4#fd4#fd4#fd4#f51#f00#f00            #f92#fb3#fb3#f00#f00#f00                                                                                                                                                                                                                        #f00#f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                                                                                                                                                        
    #f20#fd4#fd4#fd4#fd4#fd4#f51#f00#f00            #f00#f00#f00#f00#f00#f00                                                                                                                                                                                                                            #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                                                                                                                                                        
    #f20#fd4#fd4#fd4#fd4#fd4#f51#f00#f00                #f00#f00#f00#f00#f00                                                                                                                                                                                                                            #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                                                                                                                                                        
    #f20#fd4#fd4#fd4#fd4#fd4#f51#f00#f00#f00                                                                            #f00#f00#f00#f00        #f00#f00#f00#f00#f00#f00#f00                                                    #f00#f00#f00#f00#f00                                                    #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                        #f00#f00#f00#f00                                                    #f00#f00#f00#f00#f00#f00#f00                                
    #f20#fd4#fd4#fd4#fd4#fd4#fd4#fd3#fd3#f00#f00                                                                        #f00#fd3#fd3#f61#f00    #f41#fd3#fd3#fd3#fd3#fd3#f30#f00                                                #f00#fd3#fd3#fd3#f00#f00                                                #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                        #fc3#fd3#fb3#f00#f00                                                #f10#fd3#fd3#fd3#fd3#fd3#f30#f00                            
    #f20#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00                                                                    #f00#fd4#fd4#f61#f00#f00#f41#fd4#fd4#fd4#fd4#fd4#f30#f00#f00                                            #f00#fd4#fd4#fd4#f00#f00#f00                                            #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00                        #fd3#fd4#fb3#f00#f00#f00                                            #f10#fd4#fd4#fd4#fd4#fd4#f30#f00#f00                        
    #f20#fb3#fb3#fc3#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f00                                        #f00#f00#f00#f00#f00#f00#f00#fd4#fd4#f61#f00#f00#f30#f71#f71#fa2#fd4#fd4#f30#f00#f00#f00                    #f00#f00#f00#f00#f00#f00#fd4#fd4#fd4#f00#f00#f00#f00                                        #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00            #f00#f00#f00#fd3#fd4#fb3#f00#f00#f00                    #f00#f10#f10#f10#f10#f10#f20#fd4#fd4#fd4#fd4#fd4#f30#f00#f00#f00#f10#f10#f00        
    #f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd4#fd3#fd3#fd3#f00#f00                                    #f00#fc3#fd3#fd3#fd3#fd3#fd3#fd4#fd4#fd4#fd3#fd3#f51#f00#f00#f51#fd4#fd4#fd3#fd3#fd3#f00#f00                #f82#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fb3#f00#f00                                    #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00            #f92#fd3#fd3#fd4#fd4#fd4#fd3#fd3#fb3#f00                #f00#fd3#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00    
        #f00#f00#f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00                                #f00#fc3#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f61#f00#f00#f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00            #f82#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fb3#f00#f00                                    #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00            #f92#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fb3#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00
                #f10#f61#f61#f82#fd4#fd4#fd4#fd4#fd4#f61#f61#f61#f00                            #f00#f71#f82#f82#fd3#fd4#fd4#fd4#fd4#fb3#f82#f82#f30#f00#f00#f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00            #f31#f61#f61#f61#f61#f61#fd4#fd4#fd4#fd4#fd4#fb3#f00#f00                                    #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00            #f61#f82#f82#fd4#fd4#fd3#f82#f82#f61#f00#f00#f00#f10#f10#f00#fd3#fd4#fc3#f92#f92#f92#f92#f92#f92#f92#f92#fc3#fd4#fd4#fd4#fd4#fd4#f00#f00#f00
                    #f00#f00#f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd3#f00#f00                            #f00#f00#f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00#f00#f00#f00#f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00            #f00#f00#f00#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#fb3#f00#f00                                    #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00            #f00#f00#f00#fd4#fd4#fb3#f00#f00#f00#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00#f00#f00#f00#f00#f00#f00#f82#fd4#fd4#fd4#fd4#fd4#f00#f00#f00
                        #f00#f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd3#f00#f00#f00                            #f00#f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00#f00#f00#f00#f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00                #f00#f00#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#fb3#f00#f00                                    #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00            #f20#f10#f00#fd4#fd4#fb3#f00#f00#f00#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00#f00#f00#f00#f00#f00#f00#f82#fd4#fd4#fd4#fd4#fd4#f00#f00#f00
                            #f10#f51#f51#f92#fd4#fd4#fd4#fd4#fd3#f41#f41#f41#f00                            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00#f00#f00#f00#f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00                                #f00#f61#f61#f61#fd4#fd4#fc3#f41#f41#f30#f00                            #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00            #f41#f61#f51#f51#f51#f51#f00#f00#f00#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00#f00#f00#f00#f00#f00#f00#f82#fd4#fd4#f72#f61#f61#f00#f00#f00
                                #f00#f00#f61#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd3#f00#f00                        #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00                                    #f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f82#f00                            #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00            #fa3#fd4#fc3#f00#f00#f00#f00#f00#f00        #f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00                        #f82#fd4#fd4#f20#f00#f00#f00#f00#f00
                                    #f00#f61#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd3#f00#f00#f00                    #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00                                        #f00#f00#fd4#fd4#fd4#fd4#fd4#f82#f00#f00                        #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00            #fa3#fd4#fc3#f00#f00#f00#f00#f00#f00        #f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00                        #f82#fd4#fd4#f20#f00#f00#f00#f00#f00
                                        #f30#f72#f72#fc3#fd4#fd4#fd4#fd4#fd3#f31#f31#f31                    #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00            #f30#f41#f41#f41#f41#f41#f41#f41#f41#fd4#fd4#fd4#fd4#fd4#f82#f00#f00                        #f41#fd4#fd4#fd4#fd4#fd4#f61#f31#f31#f31#f31#f31#f61#f72#f72#f00#f00#f00                    #f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00#f00#f41#f41#f41#f41#f41#f30#f30#f30#f10#f00#f00            
                                        #f00#f00#f00#fa2#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00                #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00            #f92#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f82#f00#f00                        #f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f00#f00#f00                    #f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f30#f00#f00#f00#f00#f00            
                                            #f00#f00#fa2#fd3#fd3#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00            #f92#fd4#fd4#fd3#fd3#fd3#fd3#fd3#fd3#fd4#fd4#fd4#fd4#fd4#f82#f00#f00                        #f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f00#f00#f00                    #f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f30#f00#f00#f00#f00#f00            
                                                    #f00#f00#f00#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f41#fc3#fc3#fd4#fd4#fd3#f00#f00#f00#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#fd4#fc3#fc3#f20#f00                #f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00                                #f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00#f00#f00#f00#f00#f00#f00#f00#f00#f00                        
                                                        #f00#f00#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd3#f00#f00#f00#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f30#f00#f00            #f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00                                #f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00    #f00#f00#f00#f00#f00#f00#f00#f00                        
                                                            #f00#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd3#f00#f00#f00#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f30#f00#f00            #f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00                                #f00#fd4#fd4#fd4#fd4#fd4#f92#f00#f00        #f00#f00#f00#f00#f00#f00#f00                        
                #f41#fc3#fc3#f51#f00                            #fd4#fd4#fd4#fd4#fd4#fd4#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd3#f00#f00#f00        #f00#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f30#f00#f00            #f41#fd4#fd4#fd4#fd4#fd4#f41#f00#f00#f92#fd4#fd4#f71#f71#f71#f00                            #f00#fd4#fd4#fd4#fd4#fd4#fd3#fa3#fa3#f51#f00                                                    
                #f41#fd4#fd4#f51#f00#f00                        #fd4#fd4#fd4#fd4#fd4#fd4#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd3#f00#f00#f00            #f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f30#f00#f00            #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00#f82#fd4#fd4#fd4#fd4#fc3#f00#f00                        #f00#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f51#f00#f00                                                
        #f40#f40#f41#fd4#fd4#f51#f10#f10#f40#f40#f40#f40#f40#f30#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd3#f00#f10#f10#f20#f20#f20    #f00#f00#fd4#fd4#fd4#fd4#fd4#f30#f00#f00            #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00#f82#fd4#fd4#fd4#fd4#fc3#f00#f00#f00                    #f00#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f51#f00#f00                                                
    #f40#fc3#fc3#fc3#fd4#fd4#fc3#fc3#fc3#fc3#fc3#fc3#fc3#fc3#fc3#fd4#fd4#fd3#f10#f10#f10#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd4#fc3#fc3#fc3#fc3#fc3#fc3#f00    #f00#fd4#fd4#fd4#fd4#fd4#f30#f00#f00            #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00#f00#f10#f10#fb3#fd4#fc3#f00#f00#f00                    #f00#f10#f10#f10#fd3#fd4#fd4#fd4#fd4#fc3#fa3#fa3#fa3#fa3#fa3#fa3#fa3#fa3#f10                    
    #f51#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd3#f00#f00#f00#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f30#f00#f00            #f41#fd4#fd4#fd4#fd4#fd4#f31#f00#f00#f00#f00#f00#fa3#fd4#fc3#f00#f00#f00                        #f00#f00#f00#fd3#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f20#f00                
    #f20#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd3#f00#f00#f00#f00#f00            #f00#fd3#fd4#fd4#fd4#fd4#f61#f00#f00            #f51#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f41#fc3#fc3#fd4#fd4#fd4#fd4#fd4#fd4#fc3#fc3#fc3#f00#f00#f00#fd4#fd4#fd3#fc3#fc3#f20#f00#f00            #f41#fd4#fd4#fc3#fb3#fb3#f31#f00#f00    #f00#f00#fa2#fb3#fa3#f00#f00#f00#f00                        #f00#f00#fd3#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f20#f00#f00            
    #f00#f00#f00#f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f00#f00#f00#f00#f00#f00                    #f00#fd3#fd4#fb3#f10#f10#f10#f00#f00            #f51#fd4#fd4#f41#f10#f10#f00#f00#f00#f00#f00#f00#f92#fd4#fd4#fd4#fd4#fd3#f00#f00#f00#f00#f00#f00#fd4#fd4#f82#f00#f00#f00#f00#f00            #f41#fd4#fd4#f51#f00#f00#f00#f00#f00            #f00#f00#f00#fb3#fb3#fa2#f00#f00                        #f00#f10#f10#f10#fd4#fd4#fd4#fd4#fd4#f41#f10#f10#f10#f10#f10#f00#f00#f00            
        #f00#f00#f41#fd4#fd4#fd4#fd4#fd4#fd4#fd4#fd4#f00#f00#f00#f00#f00#f00#f00#f00#f00                    #f00#fd3#fd4#fa2#f00#f00#f00#f00#f00            #f51#fd4#fd4#f30#f00#f00#f00#f00#f00    #f00#f00#f92#fd4#fd4#fd4#fd4#fd3#f00#f00#f00#f00#f00#f00#fd4#fd4#f82#f00#f00#f00#f00#f00            #f41#fd4#fd4#f51#f00#f00#f00#f00#f00                #f00#f00#fd3#fd4#fb3#f00#f00#f00                        #f00#f00#f00#fd4#fd4#fd4#fd4#fd4#f31#f00#f00#f00#f00#f00#f00#f00#f00            
            #f00#f41#fc3#fc3#fc3#fc3#fc3#fc3#fc3#fc3#f00#f00#f00#f00#f00#f00#f00#f00                        #f00#fc3#fc3#fa2#f00#f00#f00#f00#f00            #f51#fc3#fc3#f30#f00#f00#f00#f00#f00        #f00#f92#fc3#fc3#fc3#fc3#fc3#f00#f00#f00        #f00#fc3#fc3#f82#f00#f00                        #f41#fc3#fc3#f51#f00#f00                                #f00#fc3#fc3#fa3#f00#f00#f00                            #f00#f00#fc3#fc3#fc3#fc3#fc3#f30#f00#f00#f00#f00#f00#f00#f00#f00            
                #f00#f00#f00#f00#f00#f00#f00#f00#f00#f00#f00#f00                                                #f00#f00#f00#f00#f00                        #f00#f00#f00#f00#f00#f00                        #f00#f00#f00#f00#f00#f00#f00#f00#f00            #f00#f00#f00#f00#f00                        #f00#f00#f00#f00#f00#f00                                    #f00#f00#f00#f00#f00#f00                                    #f00#f00#f00#f00#f00#f00#f00#f00                                    
                    #f00#f00#f00#f00#f00#f00#f00#f00#f00#f00#f00                                                    #f00#f00#f00#f00                            #f00#f00#f00#f00#f00                            #f00#f00#f00#f00#f00#f00#f00#f00                #f00#f00#f00#f00                            #f00#f00#f00#f00#f00                                        #f00#f00#f00#f00#f00                                        #f00#f00#f00#f00#f00#f00#f00                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    """

    def title2(): 
        return """                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                            #ef1#f34#f34#f34#f34#f34#f34#f34#f34#fe0                                                                                                                                                                                                                                                #cf1#f34#f34#ef1#fe0                                                                                                                                                            
                            #ef1#f44#f44#f44#f44#f44#f44#f44#f33#fe0#fe0                                                                                                                                                                                                                                            #cf1#f44#f44#ef1#fe0#fe0                                                                                                                                                        
                            #ef1#f44#f44#f44#f44#f44#f44#f44#f33#fe0#fe0#fe0                                                                                                                                                                                                                                        #cf1#f44#f44#ef1#fe0#fe0                                                                                                                                                        
                #ef1#f34#f34#f34#f44#f44#f44#f44#f44#f44#f44#f44#f34#f34#f34#fe0                                                                                                                                                                                                            #fe0#f34#f34#f34#f34#f34#f33#f44#f44#ef1#fe0#fe0                                                                                                                                                        
                #ef1#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f34#fe0#fe0                                                                                                                                                                                                        #fe0#f44#f44#f44#f44#f44#f44#f44#f44#ef1#fe0#fe0                                                                                                                                                        
                #ef1#f44#f44#f34#f35#f35#f35#f35#f35#f33#f44#f44#f35#f35#f35#fe0#fe0#fe0                                                                                                                                                                                                    #fe0#f34#f34#f34#f44#f44#f44#f44#f44#ef1#fe0#fe0                                                                                                                                                        
    #ff0#f34#f34#f34#f44#f44#df1#fe0#fe0#fe0#fe0#fe0#f25#f44#f33#fe0#fe0#fe0#fe0#fe0#fe0                                                                                                                                                                                                    #fe0#fe0#fe0#ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0                                                                                                                                                        
    #ff0#f44#f44#f44#f44#f44#df1#fe0#fe0#fe0#fe0#fe0#f25#f44#f33#fe0#fe0#fe0#fe0#fe0#fe0                                                                                                                                                                                                        #fe0#fe0#ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0                                                                                                                                                        
    #ff0#f44#f44#f44#f44#f44#df1#fe0#fe0            #f26#f34#f35#fe0#fe0#fe0                                                                                                                                                                                                                        #fe0#ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0                                                                                                                                                        
    #ff0#f44#f44#f44#f44#f44#df1#fe0#fe0            #fe0#fe0#fe0#fe0#fe0#fe0                                                                                                                                                                                                                            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0                                                                                                                                                        
    #ff0#f44#f44#f44#f44#f44#df1#fe0#fe0                #fe0#fe0#fe0#fe0#fe0                                                                                                                                                                                                                            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0                                                                                                                                                        
    #ff0#f44#f44#f44#f44#f44#df1#fe0#fe0#fe0                                                                            #fe0#fe0#fe0#fe0        #fe0#fe0#fe0#fe0#fe0#fe0#fe0                                                    #ff0#fe0#fe0#fe0#fe0                                                    #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0                        #fe0#fe0#fe0#fe0                                                    #fe0#fe0#fe0#fe0#fe0#fe0#fe0                                
    #ff0#f44#f44#f44#f44#f44#f44#f43#f43#ff0#fe0                                                                        #fe0#f43#f43#cf1#fe0    #ef1#f43#f43#f43#f43#f43#ff0#fe0                                                #ff0#f43#f43#f43#fe0#fe0                                                #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0                        #f34#f43#f34#fe0#fe0                                                #ff0#f43#f43#f43#f43#f43#ff0#fe0                            
    #ff0#f44#f44#f44#f44#f44#f44#f44#f44#ff0#fe0#fe0                                                                    #fe0#f44#f44#cf1#fe0#fe0#ef1#f44#f44#f44#f44#f44#ff0#fe0#fe0                                            #ff0#f44#f44#f44#fe0#fe0#fe0                                            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0                        #f34#f44#f34#fe0#fe0#fe0                                            #ff0#f44#f44#f44#f44#f44#ff0#fe0#fe0                        
    #ff0#f35#f35#f34#f44#f44#f44#f44#f44#ff0#fe0#fe0#fe0                                        #fe0#fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#cf1#fe0#fe0#ef0#bf1#bf1#f25#f44#f44#ff0#fe0#fe0#fe0                    #ff0#ff0#ff0#ff0#ff0#ff0#f44#f44#f44#fe0#fe0#fe0#fe0                                        #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0            #fe0#fe0#fe0#f34#f44#f34#fe0#fe0#fe0                    #fe0#ff0#ff0#ff0#ff0#ff0#ff0#f44#f44#f44#f44#f44#ff0#fe0#fe0#ff0#ff0#ff0#fe0        
    #fe0#fe0#fe0#ef1#f44#f44#f44#f44#f44#f43#f33#f33#fe0#fe0                                    #fe0#f34#f33#f33#f33#f33#f33#f44#f44#f44#f33#f33#df1#fe0#fe0#df1#f44#f44#f43#f33#f33#fe0#fe0                #af2#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f34#fe0#fe0                                    #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0            #f26#f33#f33#f44#f44#f44#f33#f33#f35#fe0                #fe0#f43#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0    
        #fe0#fe0#ef1#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0                                #fe0#f34#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#df1#fe0#fe0#df1#f44#f44#f44#f44#f44#fe0#fe0#fe0            #af2#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f34#fe0#fe0                                    #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0            #f26#f44#f44#f44#f44#f44#f44#f44#f35#fe0#fe0            #fe0#f43#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0
                #ff0#df1#df1#bf2#f44#f44#f44#f44#f44#cf1#cf1#cf1#fe0                            #fe0#bf1#bf2#bf2#f43#f44#f44#f44#f44#f34#bf2#bf2#ef0#fe0#fe0#df1#f44#f44#f44#f44#f44#fe0#fe0#fe0            #ef1#df1#df1#df1#df1#df1#f44#f44#f44#f44#f44#f34#fe0#fe0                                    #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0            #cf1#bf2#bf2#f44#f44#f33#bf2#bf2#cf1#fe0#fe0#fe0#ff0#ff0#fe0#f43#f44#f34#f26#f26#f26#f26#f26#f26#f26#f26#f34#f44#f44#f44#f44#f44#fe0#fe0#fe0
                    #fe0#fe0#ef1#f44#f44#f44#f44#f44#f44#f44#f33#fe0#fe0                            #fe0#fe0#fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0#fe0#fe0#fe0#df1#f44#f44#f44#f44#f44#fe0#fe0#fe0            #fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#f44#f44#f44#f34#fe0#fe0                                    #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0            #fe0#fe0#fe0#f44#f44#f34#fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#f44#f44#f44#f26#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#bf2#f44#f44#f44#f44#f44#fe0#fe0#fe0
                        #fe0#ef1#f44#f44#f44#f44#f44#f44#f44#f33#fe0#fe0#fe0                            #fe0#fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0#fe0#fe0#fe0#df1#f44#f44#f44#f44#f44#fe0#fe0#fe0                #fe0#fe0#fe0#fe0#fe0#f44#f44#f44#f44#f44#f34#fe0#fe0                                    #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0            #ff0#ff0#ff0#f44#f44#f34#fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#f44#f44#f44#f26#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#bf2#f44#f44#f44#f44#f44#fe0#fe0#fe0
                            #ff0#df1#df1#f25#f44#f44#f44#f44#f43#ef1#ef1#ef1#fe0                            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0#fe0#fe0#fe0#df1#f44#f44#f44#f44#f44#fe0#fe0#fe0                                #fe0#cf1#cf1#cf1#f44#f44#f34#ef1#ef1#ef0#fe0                            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0            #ef1#df1#df1#df1#df1#df1#fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#f44#f44#f44#f26#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#bf2#f44#f44#bf2#cf1#cf1#fe0#fe0#fe0
                                #fe0#fe0#cf1#f44#f44#f44#f44#f44#f44#f44#f34#fe0#fe0                        #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0                                    #fe0#fe0#fe0#f44#f44#f44#f44#f44#bf2#fe0                            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0            #f35#f44#f34#fe0#fe0#fe0#fe0#fe0#fe0        #ff0#f44#f44#f44#f44#f44#f26#fe0#fe0                        #bf2#f44#f44#ff0#fe0#fe0#fe0#fe0#fe0
                                    #fe0#cf1#f44#f44#f44#f44#f44#f44#f44#f34#fe0#fe0#fe0                    #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0                                        #ff0#fe0#f44#f44#f44#f44#f44#bf2#fe0#fe0                        #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0            #f35#f44#f34#fe0#fe0#fe0#fe0#fe0#fe0        #ff0#f44#f44#f44#f44#f44#f26#fe0#fe0                        #bf2#f44#f44#ff0#fe0#fe0#fe0#fe0#fe0
                                        #ef0#cf2#cf2#f34#f44#f44#f44#f44#f33#ef1#ef1#ef1                    #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0            #ff0#ef1#ef1#ef1#ef1#ef1#ef1#ef1#ef1#f44#f44#f44#f44#f44#bf2#fe0#fe0                        #ef1#f44#f44#f44#f44#f44#cf1#ef1#ef1#ef1#ef1#ef1#cf1#bf2#cf2#fe0#fe0#fe0                    #ff0#f44#f44#f44#f44#f44#f26#fe0#fe0#fe0#ef1#ef1#ef1#ef1#ef1#ef0#ef0#ef0#ff0#fe0#fe0            
                                        #fe0#fe0#fe0#f25#f44#f44#f44#f44#f44#f44#f44#f44#fe0                #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0            #f25#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#bf2#fe0#fe0                        #ef1#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0#fe0#fe0#fe0                    #ff0#f44#f44#f44#f44#f44#f26#fe0#fe0#fe0#f44#f44#f44#f44#f44#ff0#fe0#fe0#fe0#fe0#fe0            
                                            #fe0#fe0#f25#f33#f33#f44#f44#f44#f44#f44#f44#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0            #f25#f44#f44#f43#f43#f43#f43#f43#f43#f44#f44#f44#f44#f44#bf2#fe0#fe0                        #ef1#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0#fe0#fe0#fe0                    #ff0#f44#f44#f44#f44#f44#f26#fe0#fe0#fe0#f44#f44#f44#f44#f44#ff0#fe0#fe0#fe0#fe0#fe0            
                                                    #fe0#fe0#fe0#f44#f44#f44#f44#f44#f44#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0#ef1#f34#f34#f44#f44#f33#fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#f44#f44#f44#f44#f34#f34#ff0#fe0                #ef1#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0                                #ff0#f44#f44#f44#f44#f44#f26#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0                        
                                                        #fe0#fe0#f44#f44#f44#f44#f44#f44#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0#df1#f44#f44#f44#f44#f33#fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#f44#f44#f44#f44#f44#f44#ff0#fe0#fe0            #ef1#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0                                #ff0#f44#f44#f44#f44#f44#f26#fe0#fe0    #fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0                        
                                                            #fe0#f44#f44#f44#f44#f44#f44#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0#df1#f44#f44#f44#f44#f33#fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#f44#f44#f44#f44#f44#f44#ff0#fe0#fe0            #ef1#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0                                #ff0#f44#f44#f44#f44#f44#f26#fe0#fe0        #fe0#fe0#fe0#fe0#fe0#fe0#fe0                        
                #ef1#f34#f34#df1#fe0                            #f44#f44#f44#f44#f44#f44#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0#df1#f44#f44#f44#f44#f33#fe0#fe0#fe0        #fe0#fe0#fe0#fe0#f44#f44#f44#f44#f44#ff0#fe0#fe0            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0#f26#f44#f44#bf1#cf1#cf1#fe0                            #ff0#f44#f44#f44#f44#f44#f43#f35#f35#df1#fe0                                                    
                #ef1#f44#f44#df1#fe0#fe0                        #f44#f44#f44#f44#f44#f44#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0#df1#f44#f44#f44#f44#f33#fe0#fe0#fe0            #fe0#fe0#fe0#f44#f44#f44#f44#f44#ff0#fe0#fe0            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0#bf2#f44#f44#f44#f44#f34#fe0#fe0                        #ff0#f44#f44#f44#f44#f44#f44#f44#f44#df1#fe0#fe0                                                
        #ef0#ef0#ef1#f44#f44#df1#ff0#ff0#ef0#ef0#ef0#ef0#ef0#ef0#f44#f44#f44#f44#f44#f44#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0#df1#f44#f44#f44#f44#f33#fe0#ff0#ff0#ff0#ff0#ff0    #fe0#fe0#f44#f44#f44#f44#f44#ff0#fe0#fe0            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0#bf2#f44#f44#f44#f44#f34#fe0#fe0#fe0                    #ff0#f44#f44#f44#f44#f44#f44#f44#f44#df1#fe0#fe0                                                
    #ef0#f34#f34#f34#f44#f44#f34#f34#f34#f34#f34#f34#f34#f34#f34#f44#f44#f33#ff0#ff0#ff0#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0#df1#f44#f44#f44#f44#f44#f34#f34#f34#f34#f34#f34#fe0    #fe0#f44#f44#f44#f44#f44#ff0#fe0#fe0            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0#ff0#ff0#ff0#f35#f44#f34#fe0#fe0#fe0                    #fe0#ff0#ff0#ff0#f43#f44#f44#f44#f44#f34#f35#f35#f35#f35#f35#f35#f35#f35#ff0                    
    #df1#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f34#fe0#fe0#fe0#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0#df1#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0#f44#f44#f44#f44#f44#ff0#fe0#fe0            #ef1#f44#f44#f44#f44#f44#ef1#fe0#fe0#fe0#fe0#fe0#f35#f44#f34#fe0#fe0#fe0                        #fe0#fe0#fe0#f43#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#ff0#fe0                
    #ff0#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f34#fe0#fe0#fe0#fe0#fe0            #fe0#f34#f44#f44#f44#f44#cf1#fe0#fe0            #df1#f44#f44#f44#f44#f44#fe0#fe0#fe0#ef1#f34#f34#f44#f44#f44#f44#f44#f44#f34#f34#f34#fe0#fe0#fe0#f44#f44#f43#f34#f34#ff0#fe0#fe0            #ef1#f44#f44#f34#f34#f34#ef1#fe0#fe0    #fe0#fe0#f25#f34#f35#fe0#fe0#fe0#ff0                        #fe0#fe0#f43#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#f44#ff0#fe0#fe0            
    #fe0#fe0#fe0#ef1#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0                    #fe0#f34#f44#f35#ff0#ff0#ff0#fe0#fe0            #df1#f44#f44#ef1#ff0#ff0#fe0#fe0#fe0#fe0#fe0#fe0#f25#f44#f44#f44#f44#f33#fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#bf2#fe0#fe0#fe0#fe0#fe0            #ef1#f44#f44#df1#fe0#fe0#fe0#fe0#fe0            #fe0#fe0#fe0#f35#f35#f25#fe0#fe0                        #fe0#ff0#ff0#ff0#f44#f44#f44#f44#f44#ef1#ff0#ff0#ff0#ff0#ff0#fe0#fe0#fe0            
        #fe0#fe0#ef1#f44#f44#f44#f44#f44#f44#f44#f44#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0                    #fe0#f34#f44#f25#fe0#fe0#fe0#fe0#fe0            #df1#f44#f44#ff0#fe0#fe0#fe0#fe0#fe0    #fe0#fe0#f25#f44#f44#f44#f44#f33#fe0#fe0#fe0#fe0#fe0#fe0#f44#f44#bf2#fe0#fe0#fe0#fe0#fe0            #ef1#f44#f44#df1#fe0#fe0#fe0#fe0#fe0                #fe0#fe0#f34#f44#f34#fe0#fe0#fe0                        #fe0#fe0#fe0#f44#f44#f44#f44#f44#ff1#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0            
            #fe0#ef1#f34#f34#f34#f34#f34#f34#f34#f34#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0                        #fe0#f34#f34#f25#fe0#fe0#fe0#fe0#fe0            #df1#f34#f34#ff0#fe0#fe0#fe0#fe0#fe0        #fe0#f26#f34#f34#f34#f34#f34#fe0#fe0#fe0        #fe0#f34#f34#bf2#fe0#fe0                        #ef1#f34#f34#df1#fe0#fe0                                #fe0#f34#f34#f35#fe0#fe0#fe0                            #fe0#fe0#f34#f34#f34#f34#f34#ff0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0            
                #fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0                                                #fe0#fe0#fe0#fe0#fe0                        #fe0#fe0#fe0#fe0#fe0#fe0                        #fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0            #fe0#fe0#fe0#fe0#fe0                        #fe0#fe0#fe0#fe0#fe0#fe0                                    #fe0#fe0#fe0#fe0#fe0#fe0                                    #fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0                                    
                    #fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0                                                    #fe0#fe0#fe0#fe0                            #fe0#fe0#fe0#fe0#fe0                            #fe0#fe0#fe0#fe0#fe0#fe0#fe0#fe0                #fe0#fe0#fe0#fe0                            #fe0#fe0#fe0#fe0#fe0                                        #fe0#fe0#fe0#fe0#fe0                                        #fe0#fe0#fe0#fe0#fe0#fe0#fe0                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

    def spritemenu1():
        return """#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#853#853#853#853#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#854#854#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#854#854#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#742#742#742#742#742#742#742#742#212#212#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#742#742#742#742#742#742#742#742#212#212#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#853#853#853#853#212#212#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#853#853#853#853#212#212#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#742#742#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#742#742#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#413#413#212#212#943#943#943#943#943#943#943#943#413#413#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#413#413#212#212#943#943#943#943#943#943#943#943#413#413#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#212#212#953#953#953#953#953#953#953#953#413#413
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#212#212#953#953#953#953#953#953#953#953#413#413
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#854#854#854#854#a64#a64#a64#a64#413#413
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#854#854#854#854#a64#a64#a64#a64#413#413
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#742#742#742#742#742#742#742#742#742#742#413#413
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#742#742#742#742#742#742#742#742#742#742#413#413
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413#632#632"""

    def spritemenu2():
        return """        #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#723#723#723#723#723#723#d94#d94#d94#d94#723#723#d94#d94#d94#d94#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#723#723#723#723#723#723#d94#d94#d94#d94#723#723#d94#d94#d94#d94#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#742#742#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#742#742#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#853#853#853#853#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#853#853#853#853#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#854#854#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#854#854#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#742#742#742#742#742#742#742#742#212#212#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#742#742#742#742#742#742#742#742#212#212#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#853#853#853#853#212#212#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#853#853#853#853#212#212#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#742#742#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#742#742#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#212#212#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#212#212#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#212#212#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#212#212#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#212#212#413#413#413#413#212#212#413#413#413#413#413#413#212#212#943#943#943#943#943#943#943#943#413#413#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#212#212#413#413#413#413#212#212#413#413#413#413#413#413#212#212#943#943#943#943#943#943#943#943#413#413#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#212#212#413#413#413#413#212#212#632#632#212#212#413#413#413#413#413#413#212#212#953#953#953#953#953#953#953#953#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#212#212#413#413#413#413#212#212#632#632#212#212#413#413#413#413#413#413#212#212#953#953#953#953#953#953#953#953#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#212#212#632#632#632#632#212#212#413#413#413#413#413#413#413#413#a64#a64#a64#a64#a64#a64#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#212#212#632#632#632#632#212#212#413#413#413#413#413#413#413#413#a64#a64#a64#a64#a64#a64#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#212#212#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#413#413#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#212#212#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#413#413#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632"""

    def spritemenu3():
        return """        #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#723#723#723#723#723#723#d94#d94#d94#d94#723#723#d94#d94#d94#d94#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#723#723#723#723#723#723#d94#d94#d94#d94#723#723#d94#d94#d94#d94#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#742#742#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#742#742#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#853#853#853#853#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#853#853#853#853#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#854#854#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#854#854#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#742#742#742#742#742#742#742#742#212#212#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#742#742#742#742#742#742#742#742#212#212#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#853#853#853#853#212#212#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#853#853#853#853#212#212#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#742#742#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#742#742#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#413#413#212#212#943#943#943#943#943#943#943#943#413#413#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#413#413#212#212#943#943#943#943#943#943#943#943#413#413#632#632
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#212#212#953#953#953#953#953#953#953#953#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#212#212#953#953#953#953#953#953#953#953#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#a64#a64#a64#a64#a64#a64#a64#a64#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#a64#a64#a64#a64#a64#a64#a64#a64#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#943#943#943#943#943#943#943#943#943#943#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#943#943#943#943#943#943#943#943#943#943#413#413
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413        
            #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413        """
    def spritemenu4():
        return """#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#723#723#723#723#723#723#d94#d94#d94#d94#723#723#d94#d94#d94#d94#723#723#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#723#723#723#723#723#723#d94#d94#d94#d94#723#723#d94#d94#d94#d94#723#723#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#742#742#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#742#742#413#413#723#723#723#723#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#853#853#853#853#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#853#853#853#853#413#413#723#723#723#723#723#723#723#723#723#723#413#413#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#854#854#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#854#854#854#854#413#413#413#413#413#413#413#413#413#413#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#742#742#742#742#742#742#742#742#742#742#212#212#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#742#742#742#742#742#742#742#742#742#742#212#212#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#853#853#853#853#853#853#212#212#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#853#853#853#853#853#853#212#212#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#854#854#854#854#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#854#854#854#854#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#742#742#943#943#943#943#742#742#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#742#742#943#943#943#943#742#742#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#853#853#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#853#853#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#854#854#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#854#854#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#a64#a64#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #212#212#212#212#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #212#212#212#212#212#212#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#413#413#943#943#943#943#943#943#943#943#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#953#953#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
    #212#212#413#413#413#413#212#212#632#632#632#632#632#632#632#632#632#632#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#953#953#953#953#953#953#953#953#953#953#413#413#632#632#632#632#632#632#632#632#632#632#632#632
            #212#212#413#413#413#413#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
            #212#212#413#413#413#413#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#a64#a64#a64#a64#a64#a64#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
                    #212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#943#943#943#943#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
                    #212#212#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#413#943#943#943#943#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632
                            #212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632
                            #212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#212#413#413#413#413#413#413#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632#632"""

class GameOver:
    def img1():
        return """                                                                                                                                                                                
                                                                                                                                                    #444#444#444#444                
                                                                                                                                    #444#444#444#444#444            #444            
                                                                                                                            #444#444#444#444#444#444#444#444            #444        
                                                                                                                        #444#444        #444#444#444#444#444#444#444    #444        
                                                                                                                        #444#444#444        #444#444#444#444#444#444#444            
                                                                                                                                #444#444#444#444        #444#444#444                
                                                                                                                                        #444#444#444#444#444#444#444                
                                                                                                                            #444#444#444#444#444#444#444#444#444                    
                                                                                                                        #444#444    #444                                            
                                                                                                                        #444#444    #444#444                                        
                                                                                                                            #444        #444                                        
                                                                                                                            #444#444#444    #444                                    
                                                                                                                                        #444#444                                    
                                                                                                                                                #444                                
                                                                                                                                                                                    
                                                                                                                                                                                    
                                                                                                                                #413#413#413#413#413#413#413#413                    
                                                #413#413#413#413#413#413#413#413#413#413                            #413#413#413#212#723#723#723#723#723#423#413#413                
                                            #413#413#723#723#723#723#723#723#723#723#413#212#212            #212#212#413#723#723#723#723#723#723#723#723#723#423#413#413            
            #212                        #413#413#723#423#723#723#723#723#723#723#723#723#723#212#212#212#212#212#723#723#723#723#723#723#723#723#000#723#723#000#000#413#413        
            #212#212            #413#413#413#723#423#723#423#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#000#000#723#723#723#000#000#413        
            #212#212#212#212#413#413#423#723#423#723#423#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#000#000#723#723#723#723#423#423#212        
            #212#212#423#423#423#423#423#423#423#423#423#423#423#723#723#723#723#723#723#723#723#723#723#723#423#423#423#423#423#423#723#723#723#723#723#723#723#423#423#212        
                #212#212#423#423#423#212#212#212#212#212#212#212#423#423#423#423#423#423#423#423#423#423#423#212#212#212#212#212#212#423#423#423#723#723#723#423#423#212#212        
                    #212#212#212#212#212                        #212#212#212#212#212#212#212#212#212#212#212                    #212#212#212#212#212#423#423#423#212#212            
                                                                                                                                                #212#212#212#212#212"""

    def img2():
        return """                                                                                                                                                                                
                                                                                                                                                    #444#444#444#444                
                                                                                                                                            #444#444                #444            
                                                                                                                            #444#444#444#444#444#444#444#444            #444        
                                                                                                                            #444            #444#444#444    #444#444    #444        
                                                                                                                                #444            #444#444#444#444#444#444            
                                                                                                                                    #444                #444    #444                
                                                                                                                                        #444#444#444#444#444#444#444                
                                                                                                                                    #444#444#444#444#444#444#444                    
                                                                                                                                    #444                                            
                                                                                                                                    #444#444                                        
                                                                                                                                        #444                                        
                                                                                                                            #444            #444                                    
                                                                                                                                            #444                                    
                                                                                                                                                #444                                
                                                                                                                                                                                    
                                                                                                                                                                                    
                                                                                                                                #413#413#413#413#413#413#413#413                    
                                                #413#413#413#413#413#413#413#413#413#413                            #413#413#413#212#723#723#723#723#723#423#413#413                
                                            #413#413#723#723#723#723#723#723#723#723#413#212#212            #212#212#413#723#723#723#723#723#723#723#723#723#423#413#413            
            #212                        #413#413#723#423#723#723#723#723#723#723#723#723#723#212#212#212#212#212#723#723#723#723#723#723#723#723#000#723#723#000#000#413#413        
            #212#212            #413#413#413#723#423#723#423#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#000#000#723#723#723#000#000#413        
            #212#212#212#212#413#413#423#723#423#723#423#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#723#000#000#723#723#723#723#423#423#212        
            #212#212#423#423#423#423#423#423#423#423#423#423#423#723#723#723#723#723#723#723#723#723#723#723#423#423#423#423#423#423#723#723#723#723#723#723#723#423#423#212        
                #212#212#423#423#423#212#212#212#212#212#212#212#423#423#423#423#423#423#423#423#423#423#423#212#212#212#212#212#212#423#423#423#723#723#723#423#423#212#212        
                    #212#212#212#212#212                        #212#212#212#212#212#212#212#212#212#212#212                    #212#212#212#212#212#423#423#423#212#212            
                                                                                                                                                #212#212#212#212#212                
                                                                                                                                    """

    def title():
        pass