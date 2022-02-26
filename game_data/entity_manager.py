from game_data.gems.gem_simple import GemSimple
from game_data.gems.gem_special import GemSpecial
from game_data.rocks.rock import Rock
from game_data.rocks.rock_boulder import RockBoulder

from game_data.player import Player

class EntityManager():
    
    def __init__(self):
        self.player = Player()