


from helpers import COLORS
import random


class Tile:
    def __init__(self,color):
        self.color = color

    def __add__(self,other):
        return other

class TileBag:
    def __init__(self):
        """ 20 tiles of each color """
        self.reset()

    def reset(self):
        self.tile_bag = []
        for color in COLORS:
            self.tile_bag.extend([color]*20)
        random.shuffle(self.tile_bag)

    def draw(self,n_tiles):
        return [self.tile_bag.pop() for _ in range(n_tiles)]
    
    def add(self,tiles):
        self.tile_bag.extend(tiles)
