from player import Player
import ttgo as dev
import net


class Scoreboard:
    def __init__(self):
        self.__score = []
        self.screen_width  = 135  # screen size
        self.screen_height = 240

    def show_score(self, player, username):
       # check if list is empty
        if not self.__score:
            self.__score.append(player.pointage)

         # Add new score and username at the end of list if lower score
        if (player.pointage < self.__score[0]):
            self.__score.append(player.pointage)

        # insert at start of list if higher score than the current first score
        else:
            self.__score.insert(0, player.pointage)

    def show_screen(self):
        pass

    def bottom_score(self, player):


        dev.draw_text(0, self.screen_height, "SCORE    " + player.pointage, )




