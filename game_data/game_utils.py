# Aitana
from multiprocessing.dummy import current_process
import turtle
from game_data.player import Player
from game_data.gems.gem_base import GemBase

class GameUtils:
    def __init__(self):
        self.currentScore = 0
        # font = pygame.font.Font('freesansbold.ttf', 20)
        self.game_name = "Gem and Rock Game"

    def draw_text_to_screen(self, text_var, x_var, y_var):
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
    
    def set_score(self, score_var):
        self.currentScore = score_var

    def get_game_name(self):
        return self.game_name
