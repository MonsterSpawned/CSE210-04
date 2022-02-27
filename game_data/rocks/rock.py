# Guage
from game_data.rocks.rock_base import RockBase
import random


class Rock(RockBase):
    # Pulls from rock base
    def __init__(self):
        super().__init__()
        self.score_subtraction = 1
        self.rock_speed = random.randint(5, 20)