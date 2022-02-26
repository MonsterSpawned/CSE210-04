# Josh
# REFERENCE CODE: https://www.geeksforgeeks.org/create-a-snake-game-using-turtle-in-python/
# More REFERENCE CODE: https://github.com/smahesh29/Space-Invader-Game/blob/master/space.py

from os import sep
import os
import random
import turtle
from time import sleep
from random import randint

from game_data.game_utils import GameUtils
from game_data.gems.gem_simple import GemSimple
from game_data.gems.gem_special import GemSpecial
from game_data.gems.gem_ultra_rare import GemUltraRare
from game_data.player import Player
from game_data.rocks.rock import Rock
from game_data.rocks.rock_boulder import Boulder

class Game():
    def __init__(self):
        turtle.addshape(f"{os.getcwd()+sep}data{sep}textures{sep}gem.gif")
        turtle.addshape(f"{os.getcwd()+sep}data{sep}textures{sep}gem_special.gif")
        turtle.addshape(f"{os.getcwd()+sep}data{sep}textures{sep}boulder.gif")
        turtle.addshape(f"{os.getcwd()+sep}data{sep}textures{sep}rock.gif")
        turtle.addshape(f"{os.getcwd()+sep}data{sep}textures{sep}turtle.gif")
        self.should_quit = False
        self.gameutils = GameUtils()
        self.player = Player()
        self.entity_manager = self.gameutils.get_entity_manager()
        self.window = turtle.Screen()
        self.window.title(f"{self.gameutils.get_game_name()}:")
        self.window.bgcolor("white")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)
        self.window.listen()
        self.window.onkeypress(self.quit_game, "Escape")
        self.window.onkeypress(self.player.move_left, "a")
        self.window.onkeypress(self.player.move_right, "d")
        self.window.onkeypress(self.player.move_left, "Left")
        self.window.onkeypress(self.player.move_right, "Right")
        self.gem_list = []
        self.rock_list = []
        self.boulder_chance = 51
        self.rock_chance = 53
        self.gem_chance = 55
        self.special_gem_chance = 51

        turtle.write(
            f"{self.gameutils.get_game_name()}",
            align="center",
            font=("Verdana", 30, "normal"),
        )
        sleep(3)
        turtle.clear() #attempt to delete game name from screen

    def get_game_utils(self):
        return self.gameutils

    def quit_game(self):
        self.should_quit = True
        sleep(1)
        exit(0)

    def start_game(self):

        self.window.bgcolor("white")

        while True:
            gem_list = []
            rock_list  = []
            
            if len(gem_list) == 0:
                gem_type = random.randint(1,3)
                if gem_type == 1:
                    gem = GemSimple()
                    gem_list.append(gem)
                if gem_type == 2:
                    gem = GemSpecial()
                    gem_list.append(gem)
                if gem_type == 3:
                    gem = GemUltraRare()
                    gem_list.append(gem)

            if len(rock_list) == 0:
                rock_type = random.randint(1, 2)
                if rock_type == 1:
                    rock = Rock()
                    rock_list.append(rock)
                elif rock_type == 2:
                    rock = Boulder()
                    rock_list.append(rock)
                    
            self.window.update()
            self.gameutils.draw_text_to_screen(f"Score: {self.gameutils.currentScore}", 0, 200 )
            if self.should_quit:
                print(f"Thanks for playing {self.gameutils.get_game_name()}!")
                break
            # for obj in gem_list:
            #     obj.forward(obj.get_speed)

        self.window.mainloop()

    def make_objects(self):
        if randint(0,self.gem_chance) > 50:
            self.gem_list.append(GemSimple())
        if randint(0,self.special_gem_chance) > 50:
            self.gem_list.append(GemSpecial())
        if randint(0,self.rock_chance) > 50:
            self.rock_list.append(Rock())
        if randint(0,self.boulder_chance) > 50:
            self.rock_list.append(Boulder())

if __name__ == "__main__":
    game = Game()
    game.start_game()
