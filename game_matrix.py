import ttgo as dev
import ui
import net
from component import Component
from player import Player
from food import Food
from chrono_pomme import Chrono_pomme
from veloce_pomme import Veloce_Pomme
from constant import Direction, IDs, Foods
from sprites import Tail as tailSprite
from sprites import Body as bodySprite
import bg
from tail import Tail
from wall import Wall
import random

class GameMatrix:



    def __init__(self, get_tick, set_update_interval):
        self.players = {}
        self.chrono_apples = []
        self.veloce_apples = []
        self.poison_apples = 0
        self.block = 10
        self.width = dev.screen_width // self.block # 135 pixels
        self.height = (dev.screen_height - 20) // self.block # 230 pixels

        
    def reset_game(self, get_tick, set_update_interval, map = None):
        self.isDead = False

        self.get_tick = get_tick
        self.set_update_interval = set_update_interval
        self.restart_game = False

        self.bg = bg.bg

        self.game_matrix = []
        for i in range(self.height):
            self.game_matrix.append([])
            for j in range(self.width):
                if (map != None):
                    self.bg = bg.bg_grass
                    if (map[i][j] == 1):
                        self.game_matrix[i].append(Wall(j, i))
                    else:
                        self.game_matrix[i].append(Component(0, 0, 0, 0))
                else:
                    self.game_matrix[i].append(Component(0, 0, 0, 0))


        self.next_apple_spawn = self.get_tick() + random.randint(60, 350)

        self.x_offset = (dev.screen_width-self.width*self.block)//2
        

        self.players[net.id] = Player(self.width//2, self.height//2, net.id)
        # self.players["test"] = Player(self.width//2 + 5, self.height//2 + 5, "test")
        self.game_matrix[self.height//2][self.width//2] = self.players[net.id]

        # Create a random apple
        self.create_apple(Foods["POMME"])

        self.draw_matrix()

        dev.draw_text(0, dev.screen_height - dev.font_height, "Score", "#fff", "#000")
        self.draw_pointage()
                
        

    def draw_pointage(self):
        text_offset = 7 - (self.players[net.id].pointage >= 10) - (self.players[net.id].pointage >= 100)
        dev.draw_text(dev.font_width*(text_offset), dev.screen_height - dev.font_height, str(self.players[net.id].pointage), "#fff", "#000")
    
    def draw_matrix(self):

        for i in range(self.height):
            for j in range(self.width):
                self.draw(j, i, True)
                
    def draw(self, x, y, force=False):
        if (self.game_matrix[y][x].id == IDs["AIR"] or force):
            dev.draw_image(self.x_offset+x*self.block, y*self.block, self.bg)
            if (not force):
                return
            
        if (self.game_matrix[y][x].img == 0):
            return

        elif (len(self.game_matrix[y][x].img) <= 5):
            dev.fill_rect(self.x_offset+x*self.block+1, y*self.block+1, self.block-2, self.block-2, self.game_matrix[y][x].img)
        else:
            dev.draw_image(self.x_offset+x*self.block, y*self.block, self.game_matrix[y][x].img)
    
    ''' Move and draw the component at the new position '''
    def move_draw(self, component, x, y, draw=True):
        component.newPos(x, y)
        self.game_matrix[y][x] = component
        if (draw):
            self.draw(x, y)
    
    ''' Only set the grid position of the component and draw it '''
    def new_draw(self, component, x, y, draw=True):
        self.game_matrix[y][x] = component
        if (draw):
            self.draw(x, y)

    def update_direction(self, event):
        current_direction = self.players[net.id].direction

        if event == 'left_down':
            current_direction -= 1
           
        elif event == 'right_down':
            current_direction += 1
        
        if current_direction > 3:
            current_direction = 0

        elif current_direction < 0:
            current_direction = 3

        self.players[net.id].direction = current_direction
    
    def update_direction_other(self, id, event):
        current_direction = self.players[id].direction

        if event == 'left_down':
            current_direction -= 1
           
        elif event == 'right_down':
            current_direction += 1
        
        if current_direction > 3:
            current_direction = 0

        elif current_direction < 0:
            current_direction = 3

        self.players[id].direction = current_direction

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
        
        if (posX < 0 or posX >= self.width or posY < 0 or posY >= self.height):
            self.game_over(player)
            print("Game Over")
            return
        
        obj = self.game_matrix[posY][posX]

        if (obj.id != IDs["AIR"]):
            if(obj.id == IDs["FOOD"]):
                # Update the pointage of the player
                player.add_pointage(obj.points)
                self.draw_pointage()
                
                # Set the new head positon of the player
                self.move_draw(player, posX, posY)
                
                # Action depending on the food
                if (obj.food_id == Foods["POMME_BLOC"]):
                    # Move forward the tail and add a new block at the end of the tail
                    self.update_player_tail(player, lastX, lastY, add_block=True)
                elif (obj.food_id == Foods["POISON"]):
                    self.game_over(player)
                elif (obj.food_id == Foods["RETRECIR"]):

                    bodys = player.body

                    # If the player has no tail, the game is over since he can't shrink
                    if (len(bodys) == 0):
                        self.game_over(player)
                        return
                    
                    # Remove the last block of the tail
                    last = bodys.pop()
                    self.new_draw(Component(IDs["AIR"], last.x, last.y, 0), last.x, last.y)

                    # Set the new tail
                    if (len(bodys) > 0):
                        last_body = bodys[len(bodys)-1]
                        last_body.set_as_end(bodys[len(bodys)-2].x, bodys[len(bodys)-2].y)
                        self.draw(last_body.x, last_body.y)

                    # Move forward the tail
                    self.update_player_tail(player, lastX, lastY)


                else:
                    if (obj.food_id == Foods["CHRONO_POMME"]):
                        self.chrono_apples.remove(obj)
                    elif (obj.food_id == Foods["VITESSE"]):
                        self.set_update_interval(0.5)
                    elif (obj.food_id == Foods["VELOCE"]):
                        self.veloce_apples.remove(obj)
                    # There is no special action for this food so we just add a new block at the old head position
                    self.new_draw(Tail(player, lastX, lastY, tailSprite.bottom_tail()), lastX, lastY, draw=False)

                self.create_apple()

            elif(obj.id == IDs["PLAYER_BODY"] or obj.id == IDs["WALL"]):
                self.game_over(player)
                # print("Game Over")
                return
            bodys = player.body
            if (len(bodys) == 1):
                bodys[0].set_as_end(player.x, player.y)
            self.draw(lastX, lastY)
            return
        else :
            self.move_draw(player, posX, posY)
            self.update_player_tail(player, lastX, lastY)
    
    def body_img(self, posAfter, pos, posBefore):


        dir = self.get_dir(posBefore, pos)

        if (dir == Direction["LEFT"] and posAfter[1] < pos[1]):
            return bodySprite.top_left_corner()
        elif (dir == Direction["LEFT"] and posAfter[1] > pos[1]):
            return bodySprite.bottom_left_corner()
        elif (dir == Direction["RIGHT"] and posAfter[1] < pos[1]):
            return bodySprite.top_right_corner()
        elif (dir == Direction["RIGHT"] and posAfter[1] > pos[1]):
            return bodySprite.bottom_right_corner()
        elif (dir == Direction["UP"] and posAfter[0] < pos[0]):
            return bodySprite.top_right_corner()
        elif (dir == Direction["UP"] and posAfter[0] > pos[0]):
            return bodySprite.top_left_corner()
        elif (dir == Direction["DOWN"] and posAfter[0] < pos[0]):
            return bodySprite.bottom_right_corner()
        elif (dir == Direction["DOWN"] and posAfter[0] > pos[0]):
            return bodySprite.bottom_left_corner()
        elif (dir == Direction["UP"] or dir == Direction["DOWN"]):
            return bodySprite.vertical()
        elif (dir == Direction["LEFT"] or dir == Direction["RIGHT"]):
            return bodySprite.horizontal()
    
    def get_dir(self, posBefore, pos):
        if (posBefore[0] > pos[0]):
            return Direction["RIGHT"]
        elif (posBefore[0] < pos[0]):
            return Direction["LEFT"]
        elif (posBefore[1] > pos[1]):
            return Direction["DOWN"]
        elif (posBefore[1] < pos[1]):
            return Direction["UP"]
    
    def update_player_tail(self, player, lastX, lastY, add_block=False):
        bodys = player.body
        
        if (len(bodys) == 0):
            if (not add_block):
                self.new_draw(Component(id=IDs["AIR"], x=lastX, y=lastY, img=0), lastX, lastY)
            else:
                self.new_draw(Wall(lastX, lastY), lastX, lastY)
            return

        for i in range(len(bodys)):

            newPosX = lastX
            newPosY = lastY
            lastX = bodys[i].x
            lastY = bodys[i].y

            
            if (not bodys[i].end):
                bodys[i].img = self.body_img((lastX, lastY), (newPosX, newPosY), (bodys[i-1].x, bodys[i-1].y))
            else:
                if (i == 0):
                    bodys[i].img = tailSprite.get_tail(self.get_dir((bodys[i-1].x, bodys[i-1].y), (newPosX, newPosY)))
                else:
                    x = bodys[i-1].x
                    y = bodys[i-1].y
                    if (player.direction == Direction["UP"]):
                        y += 2
                    elif (player.direction == Direction["DOWN"]):
                        y -= 2
                    elif (player.direction == Direction["LEFT"]):
                        x += 2
                    elif (player.direction == Direction["RIGHT"]):
                        x -= 2
                    bodys[i].img = tailSprite.get_tail(self.get_dir((x, y), (newPosX, newPosY)))
            
            self.move_draw(bodys[i], newPosX, newPosY)

            if (not add_block):
                self.new_draw(Component(id=IDs["AIR"], x=lastX, y=lastY, img=0), lastX, lastY)
            else:
                self.new_draw(Wall(lastX, lastY), lastX, lastY)


    def create_apple(self, apple_id=None):

        if (apple_id == None):

            # All the foods are available
            if (len(self.players[net.id].body) > 1):
                apple_id = random.randint(0, len(Foods)-1)
                
                # Stop the poison apples from spawning too much
                if (apple_id == Foods["POISON"] and self.poison_apples > 2):
                    while (apple_id == Foods["POISON"]):
                        apple_id = random.randint(0, len(Foods)-5)
        
            # Only the basic foods are available
            else:
                apple_id = random.randint(0, len(Foods)-5)


        
        pos = self.random_pos()

        while (self.game_matrix[pos[1]][pos[0]].id != IDs["AIR"]):
            pos = self.random_pos()
        if (apple_id == Foods["CHRONO_POMME"]):
            self.new_draw(Chrono_pomme(x=pos[0], y=pos[1], chrono_apples_list=self.chrono_apples, current_time=self.get_tick()), pos[0], pos[1])
        elif (apple_id == Foods["VELOCE"]):
            self.new_draw(Veloce_Pomme(x=pos[0], y=pos[1], veloce_apples_list=self.veloce_apples, current_time=self.get_tick()), pos[0], pos[1])
        else:
            if (apple_id == Foods["POISON"]):
                self.poison_apples += 1
            self.new_draw(Food(food_id=apple_id, x=pos[0], y=pos[1]), pos[0], pos[1])

    def update(self):

        if self.isDead: return
        
        current_time = self.get_tick()

        for apple in self.chrono_apples:
            if (current_time > apple.quit_time):
                self.new_draw(Component(IDs["AIR"], apple.x, apple.y, 0), apple.x, apple.y)
                self.chrono_apples.remove(apple)
        
        for apple in self.veloce_apples:
            if (current_time > apple.move_time):

                oldX = apple.x
                oldY = apple.y
                
                pos = self.random_pos()

                while (self.game_matrix[pos[1]][pos[0]].id != IDs["AIR"]):
                    pos = self.random_pos()
                
                self.move_draw(apple, pos[0], pos[1])
                self.new_draw(Component(IDs["AIR"], oldX, oldY, 0), oldX, oldY)

                apple.set_move_time(current_time)
        
        if (current_time > self.next_apple_spawn):
            self.create_apple()
            self.next_apple_spawn = current_time + random.randint(60, 350)

        for key, player in self.players.items():
            self.update_player_head(player)
        
        
    def get_matrix(self):
        return self.game_matrix
    
    def random_pos(self):
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        return (x, y)
        
    
    def game_over(self, player):
        if self.isDead : return
        if player.userId != net.id:
            return
        self.isDead = True
        dev.clear_screen("#000")
        fg = '#000'

        x = dev.screen_width//2
        
        #dev.after(ui.time_delta, cont)
        ui.center(x, dev.font_height*4, 'GAME', '#FFF', "#000")
        ui.center(x, dev.font_height*5, 'OVER', '#FFF', "#000")

        ui.center(x, dev.font_height*11, "SCORE", '#FFF', "#000")
        ui.center(x, dev.font_height*12, str(player.pointage), '#FFF', "#000")

        
        
        

        