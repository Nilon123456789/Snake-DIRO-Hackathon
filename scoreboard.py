from player import Player
import ttgo as dev
import net


class Scoreboard:
    def __init__(self):
        self.__scoreboard = {}
        self.array = []
        self.__player_highscore = 0
        self.screen_width  = 135  # screen size
        self.screen_height = 240

    def show_score(self, player, userId):
       # check if list is empty
        if not self.__score:
            self.__score.append(player.pointage)
            self.__userId.append(player.userId)

         # Add new score and username at the end of list if lower score
        if (player.pointage < self.__score[0]):
            self.__score.append(player.pointage)
            self.__userId.append(player.userId)

        # insert at start of list if higher score than the current first score
        else:
            self.__score.insert(0, player.pointage)
            self.__userId.insert(0, player.userId)
    
    def configure_player(self, player):
        self.__scoreboard[player.userId] = player.pointage



    def new_highscore(self, player):
            if (player.pointage > self.__player_highscore):
                self.__player_highscore = player.pointage

            
            self.__scoreboard[player.userId] = player.pointage
            self.array.append(self.__player_highscore)
    


        


    def show_screen(self):
        pass

    def bottom_score(self, netId):
        dev.draw_text(0, self.screen_height, "Highscore   ")

    def get_scoreboard(self, player):
        return self.array[0]




