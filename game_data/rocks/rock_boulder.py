# Guage
from rock_base import RockBase

class RockBoulder(RockBase):
    # Pulls from rock base
    def __init__(self):
        super().__init__()
        self.rock_name = "Boulder"
        self.score_subtraction = 5
