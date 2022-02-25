# Aitana
from multiprocessing.dummy import current_process
import turtle
from game_data.player import Player
from game_data.gems.gem_base import GemBase
# import Pygame


class GameUtils:
    def __init__(self):
        self.currentScore = 0
        # font = pygame.font.Font('freesansbold.ttf', 20)
        self.game_name = "Gem and Rock Game"

<<<<<<< HEAD
    def draw_text_to_screen(self, text_var: str, x_var: int, y_var: int):
=======

    
    def draw_text_to_screen(self, text_var, x_var, y_var):
>>>>>>> 1ce511bb2f709fac70967e09f832585a0a2f9f98
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(x_var, y_var)
        pen.write(text_var, align="center", font=("candara", 24, "bold"))

    def get_score(self):
        player = Player
        gems = GemBase
        if gems.move_gem().equals(player.move_left()):
            self.currentScore += 10
        return self.currentScore
<<<<<<< HEAD

    def set_score(self, score_var: int):
=======
    

    def set_score(self, score_var):
        
>>>>>>> 1ce511bb2f709fac70967e09f832585a0a2f9f98
        self.currentScore = score_var

    def get_game_name(self):
        return self.game_name
