# Aitana
from multiprocessing.dummy import current_process
from os import sep
import os
import turtle
import winsound
from game_data.gems.gem_special import GemSpecial
from game_data.player import Player
import math

from game_data.rocks.rock import Rock

class GameUtils():
    def __init__(self):
        self.currentScore = 0
        # font = pygame.font.Font('freesansbold.ttf', 20)
        self.game_name = "Gem and Rock Game"
        self.screen_x = 600
        self.screen_y = 600

    def draw_text_to_screen(self, text_var, x_var, y_var):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(x_var, y_var)
        pen.write(text_var, align="center", font=("candara", 24, "bold"))
        self.game_complete_sound = f"{os.getcwd()+sep}data{sep}sounds{sep}game_complete.wav"

    def get_game_complete_sound(self):
        return self.game_complete_sound
    
    def play_sound(self, snd_path):
        winsound.PlaySound(snd_path, winsound.SND_ASYNC)
    
    def play_game_complete_sound(self):
        self.play_sound(self.get_game_complete_sound())
        
    def get_score(self):
        player = Player()
        gems = GemSpecial()
        rocks = Rock()
        if gems.move_gem().equals(player.move_left()):
            self.currentScore += 10
        if rocks.move_rock().equals(player.move_left()):
            self.currentScore -= 10            
        return self.currentScore
    
    def set_score(self, score_var):
        self.currentScore = score_var

    def get_game_name(self):
        return self.game_name

    def check_collisions(self, obj, player):
        return abs(obj.xcor() - player.xcor()) < 10 and abs(obj.ycor() - player.ycor()) < 10
