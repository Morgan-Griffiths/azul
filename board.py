
from helpers import COLOR_DICT_STOI, COLORS

PLACEMENT_DICT = {
    'azul': [(0,0),(1,1),(2,2),(3,3),(4,4)],
    'yellow': [(0,1),(1,2),(2,3),(3,4),(4,0)],
    'red': [(0,2),(1,3),(2,4),(3,0),(4,1)],
    'black': [(0,3),(1,4),(2,0),(3,1),(4,2)],
    'white': [(0,4),(1,0),(2,1),(3,2),(4,3)],
}

class Square:
    def __init__(self,color):
        self.color = color
        self.filled = False

    def place(self,color):
        if color != self.color:
            raise ValueError(f'wrong color')
        self.filled = True

    def __bool__(self):
        return self.filled

    def __eq__(self,other_color):
        return self.color == other_color
    
    def __ne__(self,other_color):
        return self.color != other_color
    

class Board:
    def __init__(self):
        colors = COLORS.copy()
        self.wall = [[Square(color) for color in colors],
                     [Square(color) for color in [colors[-1]] + colors[:-1]],
                     [Square(color) for color in colors[-2:] + colors[:-2]],
                     [Square(color) for color in colors[-3:] + colors[:-3]],
                     [Square(color) for color in colors[-4:] + colors[:-4]]
                     ]
        
    def place_tile(self,color,row):
        """ places a tile on the wall """
        r,c = PLACEMENT_DICT[color][row]
        if self.wall[r][c].color:
            raise ValueError(f'wrong color')
        self.wall[r][c].place_tile(color)
        
    def get_score(self):
        """ 2 points for each row. 7 points for each column. 10 points for all 5 per color """
        score = 0
        for row in self.wall:
            if all(row):
                score += 2
        for i in range(5):
            if all([self.wall[0][i],self.wall[1][i],self.wall[2][i],self.wall[3][i],self.wall[4][i]]):
                score += 7
        return score
    
    def get_state(self):
        """ returns a list of lists of colors """
        return [l for r in [[square.color for square in row] for row in self.wall] for l in r]
    
    def is_row_complete(self):
        """ returns a list of booleans for each row """
        return [all(row) for row in self.wall]
    
    def open_rows_for_color(self,color):
        """ return which rows are open for a given color """
        color_slots = PLACEMENT_DICT[color]
        open_rows = []
        for i,slot in enumerate(color_slots):
            if not self.wall[slot[0]][slot[1]].filled:
                open_rows.append(i)
        return open_rows

    def display(self):
        """ displays the board """
        for row in self.wall:
            print([(square.color,square.filled) for square in row])