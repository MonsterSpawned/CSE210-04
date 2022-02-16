# Bryan
from game_data.gems.gem_base import GemBase

class GemSpecial(GemBase):
    
    def __init__(self):
        super(GemBase, self).__init__()
        self.gem_name = "Special Gem"