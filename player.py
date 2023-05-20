

from board import Board
from floor_line import FloorLine
from pattern_lines import PatternLines


class Player:
    def __init__(self):
        self.score = 0
        self.board = Board()
        self.pattern_lines = PatternLines()
        self.floor_line = FloorLine()
        self.chosen_tokens = []

    def reset(self):
        self.__init__(self)

    def take_factory_tile(self,factory,color):
        tokens = factory.draw_tile_from_factory(color)
        self.chosen_tokens.extend(tokens)
        return tokens
    
    def take_center_tile(self,factory,color):
        taken,one = factory.draw_from_center(color)
        if one:
            self.floor_line.add_to_floor(one)
        return taken

    def get_score(self):
        return self.score + self.board.get_score() + self.floor_line.get_score()
    
    def place_on_pattern_line(self,row,tokens):
        self.chosen_tokens = []
        self.pattern_lines.add_tokens(row,tokens)

    def place_on_floor_line(self):
        self.floor_line.add_to_floor(self.chosen_tokens)
        self.chosen_tokens = []

    def place_on_board(self,pattern_line_row):
        self.board.place_tile(self.pattern_lines.get_row(pattern_line_row))
        extra_tokens = self.pattern_lines.clear_row(pattern_line_row)
        return extra_tokens
    
    def can_place_tiles_from_pattern_lines(self):
        return self.pattern_lines.can_place_tiles()

    def get_state(self):
        state = []
        state.extend(self.board.get_state())
        state.extend(self.pattern_lines.get_state())
        state.extend(self.floor_line.get_state())
        state.extend(self.chosen_tokens + [0] * (15 - len(self.chosen_tokens)))
        return state

    def display(self):
        print(f"Score: {self.get_score()}")
        print(f"Board: ")
        self.board.display()
        print(f"Pattern Lines: ")
        self.pattern_lines.display()
        print(f"Floor Line: {self.floor_line.display()}")
        print("Chosen Tokens: ",self.chosen_tokens)