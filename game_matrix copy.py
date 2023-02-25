import ttgo as dev
import ui
from component import Component
from player import Player
from constant import Direction, ID

class GameMatrix:
    block = 10
    width = dev.screen_width // block # 135 pixels
    height = (dev.screen_height - 20) // block # 230 pixels
    game_matrix = []
    players = []
    current_direction = Direction(0)


    def __init__(self):
        global game_matrix, width, height, block

        for i in range (width):
            for j in range (height):
                game_matrix[i][j] = Component(0)
                
    def draw_pointage():
        dev.draw_text(0, 0, "Player 1: " + str(players[0].pointage), "#fff", "#000")
        dev.draw_text(0, dev.screen_width//2, "Player 2: " + str(players[1].pointage), "#fff", "#000")

    def draw_matrix():
        x_offset = (dev.screen_width-width*block)//2
        for i in range(height):
            for j in range(width):
                dev.fill_rect(x_offset+i*block, j*block, block, block, "#000000")
                dev.fill_rect(x_offset+i*block+1, j*block+1, block-2, block-2, "#0f0")
                # dev.draw_image(x_offset+i*block, j*block, block, block, "bg.png")
                dev.fill_rect(x_offset+i*block+1, j*block+1, block-2, block-2, game_matrix[i][j].img())

    def update_direction(self, event, player):
        if event == 'left_down':
            if self.current_direction == Direction["RIGHT"]: # direction = 1
                self.current_direction -= Direction["LEFT"] # direction = 0 (UP)

            elif self.current_direction == Direction["LEFT"]: # direction = 3
                self.current_direction -= Direction["RIGHT"] # direction = 2 (DOWN)
            
            else:
                self.current_direction = Direction["LEFT"] 

        elif event == 'right_down':
            if self.current_direction == Direction["RIGHT"]: # direction = 1
                self.current_direction += Direction["RIGHT"] # direction = 2 (DOWN)
            
            elif self.current_direction == Direction["LEFT"]: # direction = 3
                self.current_direction += Direction["RIGHT"] # direction = 0 (UP)

            else:
                self.current_direction = Direction["RIGHT"]
        
        if self.current_direction > 3:
            self.current_direction = 0

        elif self.current_direction < 0:
            self.current_direction = 3

        player.direction = self.current_direction

    def update_player_head(self, player):
        posX = player.x
        posY = player.y
        
        if (player.direction == Direction.UP):
            posY -= 1   
        elif (player.direction == Direction.DOWN):
            posY += 1
        elif (player.direction == Direction["LEFT"]):
            posX -= 1
        elif (player.direction == Direction["RIGHT"]):
            posX += 1
        
        if (posX < 0 or posX >= width or posY < 0 or posY >= height):
            # TODO implement game over
            print("Game Over")
            return
        
        obj = game_matrix[posX][posY]

        if (obj.id != IDs["air"]):
            # TODO implement interaction
            print("Object")
            return
        
        player.newPos(posX, posY)
        game_matrix[posX][posY] = player
        self.update_player_tail(player)


    
    def update_player_tail(self, player):
        body = player.body

        if (len(body) == 0):
            return
        
        # start from the last body part and move it forward to the position of the one before it and replace the last one by air
        for i in range(len(body)-1, 0, -1):
            if (i == len(body)-1):
                game_matrix[body[i].x][body[i].y] = Component(0, )
            body[i].newPos(body[i-1].x, body[i-1].y)
            game_matrix[body[i].x][body[i].y] = body[i]

        # move the first body part to the position of the head
        body[0].newPos(player.x, player.y)
        game_matrix[body[0].x][body[0].y] = body[0]

        

    def update(self):
        global players
        for player in players:
            self.update_player_head(player)
    

    def get_matrix(self):
        return self.game_matrix




        

        