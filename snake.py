import ttgo as dev
import net
import mate
import apps
import ui
import random

import snakeImgs
from game_matrix import GameMatrix

class SnakeGame:

    def __init__(self):
        self.bg = '#000'  # general background color

        # game Mode
        self.game_mode = {}  # game state
        self.game_mode['ai_3'] = [self.load_ai_3, 0]
        self.game_mode['ai_2'] = [self.load_ai_2, 0]
        self.game_mode['ai_1'] = [self.load_ai_1, 0]
        self.game_mode['normal'] = [self.load_normal, 0]
        self.game_mode['online_ffa'] = [self.load_online_ffa, 1]
        self.game_mode['online_normal'] = [self.load_online_normal, 1]

        # Gride
        self.game_matrix = None

        # game state
        self.me = None  # is 0 when non-networked, and 0 or 1 when networked


        self.menuImageCnt = 0
        # the following global variables are useful for the networked version

        self.networked   = False  # are we playing over the network?
        self.random_seed = 0      # to get same random order on both nodes, set later
        self.msg_type    = None   # type of the messages sent between the nodes, set later
        self.ping_timer  = 0      # used to check that the mate is still with us
        self.pong_timer  = 0
        self.last_update = 0
        self.tick_counter = 0

        apps.register('SNAKE', lambda: self.snake(False), False)
        apps.register('SNAKENET', lambda: self.snake(True), True)

    def reset_mate_timeout(self):
        self.pong_timer = int(5 / ui.time_delta)  # reset peer timeout to 5 seconds

    def quit(self):  # called to quit the game
        if self.networked:
            net.send(mate.id, [self.msg_type, 'quit'])
        self.leave()

    def leave(self):
        self.me = None  # no longer playing
        if self.networked:
            net.pop_handler()  # remove message_handler
        apps.menu()  # go back to app menu

    def init_game(self):
        self.me = None

        dev.clear_screen(self.bg)

        x = dev.screen_width//2
        ui.center(x, dev.font_height*4, 'SNAKE', '#FFF', self.bg)
        ui.center(x, dev.font_height*5, 'TEAM 22!', '#FFF', self.bg)

        

    # tick_counter = 0

    def button_handler(self, event, resume):
        if self.me is None: return  # not yet playing or no longer playing
        if event == 'cancel':
            self.quit()
        elif event == 'tick':
            self.tick_counter += 1
            if self.tick_counter >= self.last_update + 5:
                self.last_update = self.tick_counter
                self.game_matrix.update()
            if self.networked:
                self.pong_timer -= 1
                if self.pong_timer < 0:
                    self.leave()
                    return
                self.ping_timer -= 1
                if self.ping_timer < 0:
                    self.ping_timer = int(2 / ui.time_delta)  # send ping every 2 secs
                    net.send(mate.id, [self.msg_type, 'ping'])
            dev.after(ui.time_delta, resume) # need to wait...
        else:
            self.game_matrix.update_direction(event)
            # ui.center(dev.screen_width//2, dev.font_height*5, msg, '#FFF', self.bg)
            resume()

    def start_game_soon(self, player):
        # dev.after(3, lambda: start_game(player))
        dev.after(3, lambda: self.menu())




    # TODO add game modes
    def load_normal(self):
        self.start_game(0)

    def load_ai_1(self):
        self.start_game(0)

    def load_ai_2(self):
        self.start_game(0)
    
    def load_ai_3(self):
        self.start_game(0)
    
    def load_online_normal(self):
        self.start_game(1)

    def load_online_ffa(self):
        self.start_game(1)

    # def nextImage(self):
    #     dev.clear_screen("#000");
    #     self.menuImageCnt += 1;
    #     if self.menuImageCnt == 5:
    #         self.menuImageCnt = 0
    #     if self.menuImageCnt == 0:
    #         dev.draw_image(20, 30, readFile("snake.png"))
    #     elif self.menuImageCnt == 1:
    #         dev.draw_image(20, 30, readFile("snake2.png"))
    #     elif self.menuImageCnt == 2:
    #         dev.draw_image(20, 30, readFile("snake3.png"))
    #     elif self.menuImageCnt == 3:
    #         dev.draw_image(20, 30, readFile("snake4.png"))
    #     elif self.menuImageCnt == 4:
    #         dev.draw_image(20, 30, readFile("snake5.png"))
    




    
    def menu(self):  # pick an app with a menu and call its handler
        dev.clear_screen("#632")
        fg = '#fff'

        def items():
            result = []
            for gamemode in self.game_mode:
                if self.networked:
                    if self.game_mode[gamemode][1] == 1:
                        result.append(gamemode) # add only online game modes
                else:
                    if self.game_mode[gamemode][1] == 0:
                        result.append(gamemode) # add only offline game modes
            return result

        def menu_handler(item, cont):
            # # global last_app
            # self.nextImage()

            if item is None or item is False:  # menu is asking to wait?
                dev.after(ui.time_delta, cont)
                if self.menuImageCnt == 0:
                    self.menuImageCnt = 1
                    # dev.draw_image(10, 10, readFile("snake-title.png"))
                    dev.draw_image(10, 10, snakeImgs.title1())

                elif self.menuImageCnt == 1:
                    self.menuImageCnt = 0
                    dev.draw_image(10, 10, snakeImgs.title2())
                
            else:  # an item was selected by the menu
                self.game_mode = item
                self.start_game(0)

        # ui.center(dev.screen_width//2, 40, '\x1F\x1FGame\x1F\x1F', fg, self.bg)
        # ui.center(dev.screen_width//2, 40+20, '\x1F\x1FMode\x1F\x1F', fg, self.bg)
        # self.menu(
        # ui.center(dev.screen_width//2, 40, '\x1F\x1FGame\x1F\x1F', fg, self.bg)

        dev.draw_image(20, 60, readFile("snake1.png"))        
        ui.menu(4, 150, 8, 8, 2, [fg, "#632"], items, "normal", menu_handler)


    def start_game(self, player):
        self.me = player
        self.reset_mate_timeout()
        ui.track_button_presses(self.button_handler)  # start tracking button presses
        dev.clear_screen(self.bg)

        self.game_matrix = GameMatrix()
        
        # x = dev.screen_width//2
        # ui.center(x, dev.font_height*10, 'QUIT =', '#FFF', self.bg)
        # ui.center(x, dev.font_height*11, 'PUSH', '#FFF', self.bg)
        # ui.center(x, dev.font_height*12, 'BOTH', '#FFF', self.bg)
        # ui.center(x, dev.font_height*13, 'BUTTONS', '#FFF', self.bg)

    def snake_non_networked(self):
        self.init_game()
        self.start_game_soon(0)

    # The following functions are used when playing the game over the network

    def master(self):  # the master is the node with the smallest id
        return net.id < mate.id

    def message_handler(self, peer, msg):
        if peer is None:
            if msg == 'found_mate':
                self.found_mate()
            else:
                print('system message', msg)  # ignore other messages from system
        elif type(msg) is list and msg[0] == self.msg_type:
            if self.me == None:
                random.seed(self.random_seed ^ msg[1])  # set same RNG on both nodes
                # determine if we are player 0 or 1
                self.start_game_soon(self.master() ^ random.randrange(2))
            elif msg[1] == 'quit':
                self.leave()
            elif msg[1] == 'ping':
                self.reset_mate_timeout()
            else:
                print('received', peer, msg)

    def found_mate(self):

        self.init_game()

        # exchange random seeds so both nodes have the same RNG
        self.random_seed = random.randrange(0x1000000)
        net.send(mate.id, [self.msg_type, self.random_seed])

    def snake_networked(self):
        self.msg_type = 'SNAKENET'
        mate.find(self.msg_type, self.message_handler)

    def snake(self, n):
        self.networked = n
        if self.networked:
            self.snake_networked()
        else:
            self.snake_non_networked()

    