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
        self.game_matrix = GameMatrix(self.get_tick, self.set_update_interval)

        self.game_mode = None

        self.game_modes = {}  # game state
        self.game_modes['ai_hard'] = [self.load_ai_3, 0]
        self.game_modes['ai_normal'] = [self.load_ai_2, 0]
        self.game_modes['ai_easy'] = [self.load_ai_1, 0]
        self.game_modes['normal'] = [self.load_normal, 0]
        self.game_modes['Start'] = [self.load_online_menu, 1]


        # Grid
        # self.game_matrix = None
        self.update_interval = 5

        # game state
        self.me = None  # is 0 when non-networked, and 0 or 1 when networked, None if not playing | PLAYER ID
        

        self.menuImageCnt = 0
        self.listOfPlayers = []
        self.isHosting = False
        self.isSlave = False
        self.isReady = False
        self.inMenu = False


        self.networked   = False  # are we playing over the network?
        self.random_seed = 0      # to get same random order on both nodes, set later
        self.msg_type    = None   # type of the messages sent between the nodes, set later
        self.ping_timer  = 0      # used to check that the mate is still with us
        self.pong_timer  = 0
        self.last_update = 0
        self.tick_counter = 0

        apps.register('SNAKE', lambda: self.snake(0), False)
        apps.register('SNAKEDUO', lambda: self.snake(1), True)
        apps.register('SNK Host', lambda: self.snake(2), True) 
        apps.register('SNK Join', lambda: self.snake(3), True) 

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

    def init_game(self): # 4
        self.me = None
        self.isReady = True

        dev.clear_screen(self.bg)

        x = dev.screen_width//2
        ui.center(x, dev.font_height*4, 'SNAKE', '#FFF', self.bg)
        ui.center(x, dev.font_height*5, 'TEAM 22!', '#FFF', self.bg)
        ui.center(x, dev.font_height*7, 'Get', '#FFF', self.bg)
        ui.center(x, dev.font_height*8, 'Ready!', '#FFF', self.bg)

    def get_tick(self):
        return self.tick_counter
    
    def set_update_interval(self, step):
        self.update_interval -= step
        if self.update_interval < 1:
            self.update_interval = 0.5

    def button_handler(self, event, resume):
        if self.me is None: return  # not yet playing or no longer playing
        if event == 'cancel':
            self.quit()
        elif event == 'tick':
            self.tick_counter += 1
            if self.tick_counter >= self.last_update + self.update_interval:
                self.isDead = self.game_matrix.isDead
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
            if self.game_matrix.isDead:
                self.game_over(event)
            else:
                self.game_matrix.update_direction(event)
            
            # self.game_over(event)
            # ui.center(dev.screen_width//2, dev.font_height*5, msg, '#FFF', self.bg)
            resume()

    def game_over(self, event):
            # self.game_matrix = GameMatrix(self.get_tick, self.set_update_interval)
            # self.game_matrix.reset_game(self.get_tick, self.set_update_interval)
            self.isReady = False
            if (event == 'left_down'):
                self.menu()

    def start_game_soon(self, player): # 4

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
    
    def load_online(self): # called by api from host
        self.start_game(1)

    def load_online_menu(self): # called by host to start the game
        for player in self.listOfPlayers:
            net.send(player, ["custom", "start"])
        self.load_online()
    
    def menu(self):  # pick an app with a menu and call its handler # 5
        if self.inMenu: return
        dev.clear_screen("#632")
        fg = '#fff'

        def items():
            result = []
            for gamemode in self.game_modes:
                if self.networked:
                    if self.game_modes[gamemode][1] == 1:
                        result.append(gamemode) # add only online game modes
                else:
                    if self.game_modes[gamemode][1] == 0:
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
                    dev.draw_image(20, 60, snakeImgs.spritemenu2())

                elif self.menuImageCnt == 1:
                    self.menuImageCnt = 2
                    dev.draw_image(10, 10, snakeImgs.title2())
                    dev.draw_image(20, 60, snakeImgs.spritemenu3())

                elif self.menuImageCnt == 2:
                    self.menuImageCnt = 3
                    dev.draw_image(10, 10, snakeImgs.title1())
                    dev.draw_image(20, 60, snakeImgs.spritemenu2())

                elif self.menuImageCnt == 3:
                    self.menuImageCnt = 0
                    dev.draw_image(10, 10, snakeImgs.title2())
                    dev.draw_image(20, 60, snakeImgs.spritemenu3())

                
            else:  # an item was selected by the menu
                self.game_mode = item
                self.game_modes[item][0]()

                


        # dev.draw_image(20, 60, readFile("snake1.png"))        
        ui.menu(4, 150, 8, 8, 2, [fg, "#632"], items, "normal", menu_handler)
        self.inMenu = True



    def start_game(self, player):
        self.me = player
        self.inMenu = False
        self.reset_mate_timeout()
        ui.track_button_presses(self.button_handler)  # start tracking button presses
        dev.clear_screen(self.bg)

        
        self.game_matrix.reset_game(self.get_tick, self.set_update_interval)
        

   

    # The following functions are used when playing the game over the network

    def master(self):  # the master is the node with the smallest id
        if len(self.listOfPlayers) == 1:
            return net.id < mate.id;
        if self.isHosting:
            return True;
        else:
            return False;

    def message_handler(self, peer, msg):
        # global pong_timer
        print('received', msg)
       
        if peer is None:
            if msg == 'found_mate':
                if mate.id not in self.listOfPlayers:
                    self.listOfPlayers.append(mate.id)
                if not self.isHosting:
                    self.found_mate()
            else:
                print('system message', msg)  # ignore other messages from system

        elif type(msg) is list and msg[0] == None and msg[1] == self.msg_type: # BYPASS ADD MULTIPLE PLAYERS
             if peer not in self.listOfPlayers:
                self.listOfPlayers.append(peer)
        elif type(msg) is list and msg[0] == self.msg_type:
            if msg[1] == 'quit':
                self.leave()
            elif msg[1] == 'ping':
                self.reset_mate_timeout()
            elif self.me == None:
                if not self.isHosting:
                    random.seed(self.random_seed ^ msg[1])  # set same RNG on both nodes
            else:
                print('received', peer, msg)
        elif type(msg) is list and msg[0] == 'custom':
            if msg[1] == 'ready':
                if not self.isHosting and self.master() and not self.isSlave:
                    self.start_game_soon(peer)
            if msg[1] == 'start':
                self.load_online()
        if self.isHosting and not self.isReady: # BYPASS ADD MULTIPLE PLAYERS
            if (len(self.listOfPlayers) >= 2):
                self.found_mates()
            else:
                mate.find(self.msg_type, self.message_handler)
                dev.fill_rect(0, 60, 135, 180, "#000")
                dev.draw_text(0, 60, "Waiting", "#fff", "#000")
                dev.draw_text(0, 80, "for", "#fff", "#000")
                dev.draw_text(0, 100, "another", "#fff", "#000")
                dev.draw_text(0, 120, "player", "#fff", "#000")
    def found_mate(self):
        self.init_game()
        net.send(mate.id, [self.msg_type, self.random_seed])
        net.send(mate.id, ["custom", "ready"])

    def found_mates(self):
        print("EVERYONE IS HERE")
        self.init_game()
        self.start_game_soon(0)
        for player in self.listOfPlayers:
            net.send(player, [self.msg_type, self.random_seed])
            net.send(player, ["custom", "ready"])
        



    ###### INIT the game ######
    def snake_non_networked(self): # 3
        self.init_game()  # 4
        self.start_game_soon(0) # 4

    def snake_networked(self): #2
        if self.isHosting:
            self.random_seed = random.randrange(0x1000000)
            random.seed(self.random_seed)
        self.msg_type = 'SNAKENET'
        mate.find(self.msg_type, self.message_handler)
        if self.isHosting:
            dev.fill_rect(0, 30, 135, 180, "#000")
            dev.draw_text(0, 30, "Waiting", "#fff", "#000")
            dev.draw_text(0, 50, "for", "#fff", "#000")
            dev.draw_text(0, 70, "two", "#fff", "#000")
            dev.draw_text(0, 90, "player", "#fff", "#000")


    def snake(self, n): #n = networked? bool
        if n == 0:
            self.networked = False
            self.snake_non_networked()
        elif n == 1:
            self.networked = True
            self.snake_networked()
        elif n == 2:
            self.networked = True
            self.isHosting = True
            self.snake_networked()
        elif n == 3:
            self.networked = True
            self.isSlave = True
            self.snake_networked()
        