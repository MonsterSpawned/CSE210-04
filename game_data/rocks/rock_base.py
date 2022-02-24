# Guage
from turtle import *
import winsound
from pathlib import Path


class RockBase:
    def __init__(self):
        self.rock_speed = 0
        self.rock_chance = 0
        self.rock_color = "blue"
        self.collect_sound = Path("./data/sounds/collect_sound.wav")
        self.cur_x = 0
        self.cur_y = -250
        self.cur_heading = 90
        self.rock = Turtle()
        self.rock.color(self.rock_color)
        self.rock.shape(Path("./data/textures/rock.gif"))
        self.rock.penup()
        self.rock.speed(0)
        self.rock.setposition(self.cur_x, self.cur_y)
        self.rock.setheading(self.cur_heading)

    def get_collect_sound(self):
        return self.collect_sound

    def play_collect_sound(self):
        winsound.PlaySound(str(self.get_collect_sound()), winsound.SND_ASYNC)

    def move_rock(self):
        pass

    def animate_rock(self):
        pass

    def get_rock_color(self):
        return self.rock_color
