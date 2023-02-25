import ttgo as dev
import splash
import apps

# apps
from snake import SnakeGame
import zzz

snakeGame = SnakeGame()


def start():
    if (True): # Bypass Menu
        snakeGame.menu()
    else:
        splash.show()            # show splash screen
        dev.after(2, apps.menu)  # after 2 seconds show app menu

start()
