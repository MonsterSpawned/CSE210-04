# Josh
# REFERENCE CODE: https://www.geeksforgeeks.org/create-a-snake-game-using-turtle-in-python/
from time import sleep
import turtle
from game_data.game_utils import GameUtils
from game_data.player import Player

class Game():
    
    def quit_game(self):
        self.should_quit = True
        sleep(1)
        exit(0)
    
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
        turtle.write(f"{self.gameutils.get_game_name()}", align="center", font=("Verdana", 30, "normal"))
        sleep(5)

    def start_game(self):
        self.window.bgcolor("black")
        while True:
            self.window.update()
            if self.should_quit:
                print(f"Thanks for playing {self.gameutils.get_game_name()}!")
                break
        self.window.mainloop()

if __name__ == "__main__":
    game = Game()
    game.start_game()