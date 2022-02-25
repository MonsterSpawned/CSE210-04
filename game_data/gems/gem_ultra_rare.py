# Bryan
import os
from os import sep
from game_data.gems.gem_base import GemBase


class GemUltraRare(GemBase):
    def __init__(self):
        super().__init__()
        self.gem_name = "Le Turtle Gem"
        self.collect_sound = f"{os.getcwd()+sep}data{sep}sounds{sep}gem_collect1.wav"
        self.gem.shape(f"{os.getcwd()+sep}data{sep}textures{sep}turtle.gif")
        self.gem.shape = "turtle"
        self.gem_speed = 25