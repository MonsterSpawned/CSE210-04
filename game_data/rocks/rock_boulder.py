# Guage
from game_data.rocks.rock_base import RockBase
import random

class Boulder(RockBase):
    # Pulls from rock base
    def __init__(self):
        super().__init__()
        self.rock_name = "Boulder"
        self.score_subtraction = 5
        self.rock_speed = random.randint(5, 15)
        self.rock_size = 2