# Josh
# REFERENCE CODE: https://www.geeksforgeeks.org/create-a-snake-game-using-turtle-in-python/
# More REFERENCE CODE: https://github.com/smahesh29/Space-Invader-Game/blob/master/space.py

import turtle
from time import sleep
from random import randint

from game_data.gems.gem_simple import GemSimple
from game_data.gems.gem_special import GemSpecial
from game_data.rocks.rock import Rock
from game_data.rocks.rock_boulder import RockBoulder

from game_data.player import Player
from game_data.game_utils import GameUtils

class Game:
    def __init__(self):
        self.should_quit = False
        self.gameutils = GameUtils()
        self.player = Player()
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
        sleep(5)
        turtle.clear #attempt to delete game name from screen
        sleep(3)

    def quit_game(self):
        self.should_quit = True
        sleep(1)
        exit(0)

    def start_game(self):

        self.window.bgcolor("black")
        self.gameutils.draw_text_to_screen("Score: 0", 0, 200 )

        while True:
            self.window.update()
            if self.should_quit:
                print(f"Thanks for playing {self.gameutils.get_game_name()}!")
                break

        self.window.mainloop()

    def make_objects(self):
        if randint(0,self.gem_chance) > 50:
            self.gem_list.append(GemSimple())
        if randint(0,self.special_gem_chance) > 50:
            self.gem_list.append(GemSpecial())
        if randint(0,self.rock_chance) > 50:
            self.gem_list.append(Rock())
        if randint(0,self.boulder_chance) > 50:
            self.gem_list.append(RockBoulder())


if __name__ == "__main__":
    game = Game()
    game.start_game()
