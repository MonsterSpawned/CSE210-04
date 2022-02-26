# Guage
from os import sep
import os
from turtle import *
import winsound
from pathlib import Path
import random

class RockBase():
    def __init__(self):
        self.rock_speed = 0
        self.rock_name = "Rock"
        self.rock_chance = 0
        self.score_subtraction = 0
        self.rock_size = 1
        self.rock_color = "blue"
        self.collect_sound = f"data{sep}sounds{sep}rock_hit.wav"
        self.cur_x = random.randint(-300, 300)
        self.cur_y = 300
        self.cur_heading = 90
        self.rock = Turtle()
        self.rock.color(self.rock_color)
        self.rock.shape(f"{os.getcwd()+sep}data{sep}textures{sep}rock.gif")
        self.rock.penup()
        self.rock.speed(self.rock_speed)
        self.rock.right(90)
        self.rock.turtlesize(self.rock_size)


    def get_collect_sound(self):
        return self.collect_sound

    def play_collect_sound(self):
        self.game_utils.play_sound(self.get_collect_sound())

    def move_rock(self):
        pass

    def animate_rock(self):
        pass

    def get_rock_color(self):
        return self.rock_color
