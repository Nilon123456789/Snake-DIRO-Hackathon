from player import Player
import ttgo as dev


class Scoreboard:
    def __init__(self):
        self.__score = []

    def config_username(self, player, username):
       # check if list is empty
        if not self.__score:
            self.__score.append(player.pointage)
            self.__username.append(username)

         # Add new score and username at the end of list if lower score
        if (player.pointage < self.__score[0]):
            self.__score.append(player.pointage)
            self.__username.append(username)

        # insert at start of list if higher score than the current first score
        else:
            self.__score.insert(0, player.pointage)
            self.__username.insert(0, username)

    def show_screen(self):
        pass



