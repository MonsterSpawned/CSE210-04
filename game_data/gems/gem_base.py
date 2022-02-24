# Bryan
from turtle import *
import turtle
import math
import random
import winsound
from os.path import sep


class GemBase:
    def __init__(self):
        self.gem_name = "Base Gem"
        self.gem_speed = 0
        self.gem_chance = 0
        self.score_addition = 0
        self.score_multiplier = 0
        self.is_special = False
        self.gem_color = "white"
        self.collect_sound = f"data{sep}sounds{sep}collect_sound.wav"
        self.cur_x = 0
        self.cur_y = -250
        self.cur_heading = 90
        self.gem = turtle.Turtle()
        self.gem.color(self.gem_color)
        self.gem.shape(f"data{sep}textures{sep}gem.gif")
        self.gem.penup()
        self.gem.speed(0)
        self.gem.setposition(self.cur_x, self.cur_y)
        self.gem.setheading(self.cur_heading)

    def get_collect_sound(self):
        return self.collect_sound

    def play_collect_sound(self):
        winsound.PlaySound(self.get_collect_sound(), winsound.SND_ASYNC)

    def move_gem(self):
        pass

    def animate_gem(self):
        pass

    def get_gem_color(self):
        return self.gem_color
