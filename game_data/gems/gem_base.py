# Bryan
import os
from turtle import *
import turtle
import math
import random
import winsound
from os.path import sep
from game_data.game_utils import GameUtils

class GemBase():
    def __init__(self):
        self.game_utils = GameUtils()
        self.gem_name = "Base Gem"
        self.gem_speed = 0
        self.gem_chance = 0
        self.score_addition = 0
        self.score_multiplier = 0
        self.is_special = False
        self.gem_color = "white"
        self.collect_sound = f"{os.getcwd()+sep}data{sep}sounds{sep}gem_collect.wav"
        self.cur_x = random.randint(-300,300)
        self.cur_y = 300
        self.cur_heading = 90
        self.gem = turtle.Turtle()
        self.gem.color(self.gem_color)
        self.gem.shape(f"{os.getcwd()+sep}data{sep}textures{sep}gem.gif")
        self.gem.penup()
        self.gem.right(self.cur_heading)
        self.gem.speed(self.gem_speed)

    def get_collect_sound(self):
        return self.collect_sound

    def play_collect_sound(self):
        self.game_utils.play_sound(self.get_collect_sound())

    def move_gem(self):
        pass

    def animate_gem(self):
        pass

    def get_gem_color(self):
        return self.gem_color
