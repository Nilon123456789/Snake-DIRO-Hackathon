import ttgo as dev
import ui
from component import Component
from player import Player
from food import Food
from constant import Direction, IDs, Foods
import bg
from tail import Tail
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
        

        self.players.append(Player(self.height//2, self.width//2))
        self.game_matrix[self.height//2][self.width//2] = self.players[0]
        print("Player pos: ", self.players[0].x, self.players[0].y)
        self.current_direction = self.players[0].direction

        # Create a random apple
        self.create_apple(Foods["POMME"])

        self.draw_matrix()
                
    def draw_pointage(self):
        # dev.draw_text(0, 0, "Player 1: " + str(self.players[0].pointage), "#fff", "#000")
        # dev.draw_text(0, dev.screen_width//2, "Player 2: " + str(self.players[1].pointage), "#fff", "#000")
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
        if event == 'left_down':
            self.current_direction -= 1
           
        elif event == 'right_down':
            self.current_direction += 1
        
        if self.current_direction > 3:
            self.current_direction = 0

        elif self.current_direction < 0:
            self.current_direction = 3

        self.players[0].direction = self.current_direction

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
                body = Tail(player, lastX, lastY)
                self.game_matrix[lastY][lastX] = body

                player.newPos(posX, posY)
                self.game_matrix[posY][posX] = player

                self.draw(lastX, lastY)
                self.draw(posX, posY)

                player.add_pointage(obj.points)

                self.create_apple(Foods["POMME"])
            return
        else :
            player.newPos(posX, posY)
            self.game_matrix[posY][posX] = player
            self.draw(posX, posY)
            self.update_player_tail(player, lastX, lastY)


    
    def update_player_tail(self, player, lastX, lastY):
        bodys = player.body
        if (len(bodys) == 0):
            self.game_matrix[lastY][lastX] = Component(id=IDs["AIR"], x=lastX, y=lastY, img=0)
            self.draw(lastX, lastY)
            return
        
        for i in range(len(bodys) - 1):
            if (i == len(bodys) - 1):
                self.game_matrix[lastY][lastX] = Component(id=IDs["AIR"], x=lastX, y=lastY, img=0)
                self.draw(lastX, lastY)
                break
            bodys[i].newPos(lastX, lastY)
            self.game_matrix[lastY][lastX] = bodys[i]
            self.draw(bodys[i].x, bodys[i].y)

            lastX = bodys[i].x
            lastY = bodys[i].y


    def create_apple(self, apple_id):
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)

        while (self.game_matrix[y][x].id != IDs["AIR"]):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
        
        self.game_matrix[y][x] = Food(x, y, apple_id)
        self.draw(x, y)

    def update(self):
        for player in self.players:
            self.update_player_head(player)
    

    def get_matrix(self):
        return self.game_matrix




        

        