import ttgo as dev
import ui
from component import Component
from player import Player
from food import Food
from constant import Direction, IDs, Foods
import bg
from tail import Tail
from wall import Wall
import random

class GameMatrix:



    def __init__(self):
        self.block = 10
        self.width = dev.screen_width // self.block # 135 pixels
        self.height = (dev.screen_height - 20) // self.block # 230 pixels

        self.game_matrix = []
        for i in range(self.height):
            self.game_matrix.append([])
            for j in range(self.width):
                self.game_matrix[i].append(Component(0, 0, 0, 0))


        self.players = []
        self.x_offset = (dev.screen_width-self.width*self.block)//2
        

        self.players.append(Player(self.width//2, self.height//2))
        self.game_matrix[self.height//2][self.width//2] = self.players[0]

        # Create a random apple
        self.create_apple(Foods["POMME"])
        self.create_apple(Foods["POMME"])

        self.draw_matrix()
                
    def draw_pointage(self):
        dev.draw_text(0, 0, "Player 1: " + str(self.players[0].pointage), "#fff", "#000")
        dev.draw_text(0, dev.screen_width//2, "Player 2: " + str(self.players[1].pointage), "#fff", "#000")
        pass
    
    def draw_matrix(self):

        for i in range(self.height):
            for j in range(self.width):
                self.draw(j, i)
                
    def draw(self, x, y):
        if (self.game_matrix[y][x].id == IDs["AIR"]):
            dev.draw_image(self.x_offset+x*self.block, y*self.block, bg.bg())
            return
        dev.fill_rect(self.x_offset+x*self.block+1, y*self.block+1, self.block-2, self.block-2, self.game_matrix[y][x].img)

    def update_direction(self, event):
        current_direction = self.players[0].direction

        if event == 'left_down':
            current_direction -= 1
           
        elif event == 'right_down':
            current_direction += 1
        
        if current_direction > 3:
            current_direction = 0

        elif current_direction < 0:
            current_direction = 3

        self.players[0].direction = current_direction

    def update_player_head(self, player):
        posX = player.x
        posY = player.y
        lastX = posX
        lastY = posY
        
        
        if (player.direction == Direction["UP"]):
            posY -= 1   
        elif (player.direction == Direction["DOWN"]):
            posY += 1
        elif (player.direction == Direction["LEFT"]):
            posX -= 1
        elif (player.direction == Direction["RIGHT"]):
            posX += 1

        print("Player pos: ", posX, posY, "Direction: ", player.direction, "Last pos: ", lastX, lastY)
        
        if (posX < 0 or posX >= self.width or posY < 0 or posY >= self.height):
            # TODO implement game over
            print("Game Over")
            return
        
        obj = self.game_matrix[posY][posX]

        if (obj.id != IDs["AIR"]):
            if(obj.id == IDs["FOOD"]):

                player.add_pointage(obj.points)
                
                player.newPos(posX, posY)
                self.game_matrix[posY][posX] = player
                self.draw(posX, posY)
                
                if (obj.food_id == Foods["POMME_BLOC"]):
                    self.update_player_tail(player, lastX, lastY, add_block=True)
                elif (obj.food_id == Foods["POISON"]):
                    # TODO implement poison
                    pass
                elif (obj.food_id == Foods["CHRONO_POMME"]):
                    # TODO implement chrono pomme
                    pass
                elif (obj.food_id == Foods["RETRECIR"]):
                    bodys = player.body
                    if (len(bodys) == 0):
                        # TODO implement game over
                        return
                    
                    last = bodys.pop()
                    self.game_matrix[last.y][last.x] = Component(id=IDs["AIR"], x=last.x, y=last.y, img=0)
                    self.draw(last.x, last.y)

                    if (len(bodys) > 0):
                        bodys[len(bodys)].set_as_end()
                        self.draw(bodys[len(bodys)].x, bodys[len(bodys)].y)
                        self.draw(last.x, last.y)
                        self.update_player_tail(player, lastX, lastY)
                    pass
                elif (obj.food_id == Foods["VITESSE"]):
                    # TODO implement vitesse
                    pass    
                else:
                    body = Tail(player, lastX, lastY)
                    self.game_matrix[lastY][lastX] = body

                self.create_apple(apple_id=Foods["RETRECIR"])
            
            bodys = player.body
            if (len(bodys) == 1):
                bodys[0].set_as_end()
            self.draw(lastX, lastY)
            return
        else :
            player.newPos(posX, posY)
            self.game_matrix[posY][posX] = player
            self.draw(posX, posY)
            self.update_player_tail(player, lastX, lastY)


    
    def update_player_tail(self, player, lastX, lastY, add_block=False):
        bodys = player.body
        
        if (len(bodys) == 0):
            if (not add_block):
                self.game_matrix[lastY][lastX] = Component(id=IDs["AIR"], x=lastX, y=lastY, img=0)
            else:
                self.game_matrix[lastY][lastX] = Wall(lastX, lastY)
            self.draw(lastX, lastY)
            return

        for i in range(len(bodys)):

            newPosX = lastX
            newPosY = lastY
            lastX = bodys[i].x
            lastY = bodys[i].y

            bodys[i].newPos(newPosX, newPosY)
            self.game_matrix[newPosY][newPosX] = bodys[i]
            self.draw(bodys[i].x, bodys[i].y)

            if (not add_block):
                self.game_matrix[lastY][lastX] = Component(id=IDs["AIR"], x=lastX, y=lastY, img=0)
            else:
                self.game_matrix[lastY][lastX] = Wall(lastX, lastY)
            self.draw(lastX, lastY)


    def create_apple(self, apple_id=None):

        if (apple_id == None):
            apple_id = random.randint(0, len(Foods)-1)
        
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)

        while (self.game_matrix[y][x].id != IDs["AIR"]):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
        
        self.game_matrix[y][x] = Food(food_id=apple_id, x=x, y=y)
        self.draw(x, y)

    def update(self):
        for player in self.players:
            self.update_player_head(player)
    

    def get_matrix(self):
        return self.game_matrix
    
    def game_over(self):
        pass