# Guage
from rock_base import RockBase


class Rock(RockBase):
    # Pulls from rock base
    def __init__(self):
        super().__init__()
        self.score_subtraction = 1
