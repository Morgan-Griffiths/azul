
from helpers import COLOR_DICT_STOI


class PatternLines:
    def __init__(self):
        self.reset()

    def reset(self):
        self.pattern_lines = []
        for i in range(1,6):
            patterns = [0 for _ in range(i)]
            self.pattern_lines.append(patterns)

    def add_tokens(self,row,tokens):
        if len(tokens) > len(self.pattern_lines[row]):
            excess_tokens = tokens[:len(tokens) - len(self.pattern_lines[row])]
            remaining_tokens = tokens[len(tokens) - len(self.pattern_lines[row]):]
            self.pattern_lines[row] = remaining_tokens
        else:
            for i,token in enumerate(tokens):
                self.pattern_lines[row][i] = token
            excess_tokens = []
        return excess_tokens
    
    def get_state(self):
        state = []
        for row in self.pattern_lines:
            state.extend([tile for tile in row])
        return state
    
    def get_row(self,row):
        temp,self.pattern_lines[row] = self.pattern_lines[row], [0 for _ in range(len(self.pattern_lines[row]))]
        return temp
    
    def can_place_tiles(self):
        return any([row[0] for row in self.pattern_lines])

    def get_open_lines(self,color):
        """ Returns a list of open lines for a given color. depends whether the board is open and if there is room on the pattern line. """
        open_lines = [0] * 5
        for i,row in enumerate(self.pattern_lines):
            if len(row) > 0 and row[0] == color:
                open_lines.append(i)
        return open_lines
    
    def display(self):
        for i,row in enumerate(self.pattern_lines):
            print(f'pattern line {i} {row}')