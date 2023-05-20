
from helpers import COLOR_DICT_STOI


class FloorLine:
    def __init__(self):
        self.floor_line = []
        self.scoring = [-1,-1,-2,-2,-2,-3,-3]

    def add_to_floor(self,token):
        self.floor_line.append(token)

    def get_score(self):
        score = 0
        for token,score in zip(self.floor_line,self.scoring):
            score += token + score
        return score

    def get_state(self):
        return [COLOR_DICT_STOI[tile] for tile in self.floor_line] + [0 for _ in range(7 - len(self.floor_line))]

    def display(self):
        print(f'Floor Line:{self.floor_line}')