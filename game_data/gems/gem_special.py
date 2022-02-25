# Bryan
import os
from os import sep
from game_data.gems.gem_base import GemBase


class GemSpecial(GemBase):
    def __init__(self):
        super().__init__()
        self.gem_name = "Special Gem"
        self.collect_sound = f"{os.getcwd()+sep}data{sep}sounds{sep}gem_collect1.wav"
        self.gem.shape(f"{os.getcwd()+sep}data{sep}textures{sep}gem_special.gif")
