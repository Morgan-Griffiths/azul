
from enum import Enum, auto


class ActionType(Enum):
    take_factory_0 = auto()
    take_factory_1 = auto()
    take_factory_2 = auto()
    take_factory_3 = auto()
    take_factory_4 = auto()
    take_center = auto()
    pick_pattern_line = auto()
    place_tile_on_wall = auto()

class Actions(Enum):
    """ 
    can either take a tile from a factory or place a tile on the floor.
    there are 5 factories, 1 center, 5 floor lines, and 5 colors.
    pick color in a factory or center = 6 * 5 = 30 actions
    pick a floor line = 5 actions

    that would be 30 + 5 = 35 actions.
    """
    take_factory_0_azul = auto()
    take_factory_0_yellow = auto()
    take_factory_0_red = auto()
    take_factory_0_black = auto()
    take_factory_0_white = auto()
    take_factory_1_azul = auto()
    take_factory_1_yellow = auto()
    take_factory_1_red = auto()
    take_factory_1_black = auto()
    take_factory_1_white = auto()
    take_factory_2_azul = auto()
    take_factory_2_yellow = auto()
    take_factory_2_red = auto()
    take_factory_2_black = auto()
    take_factory_2_white = auto()
    take_factory_3_azul = auto()
    take_factory_3_yellow = auto()
    take_factory_3_red = auto()
    take_factory_3_black = auto()
    take_factory_3_white = auto()
    take_factory_4_azul = auto()
    take_factory_4_yellow = auto()
    take_factory_4_red = auto()
    take_factory_4_black = auto()
    take_factory_4_white = auto()
    take_center_azul = auto()
    take_center_yellow = auto()
    take_center_red = auto()
    take_center_black = auto()
    take_center_white = auto()
    place_on_pattern_line_1 = auto()
    place_on_pattern_line_2 = auto()
    place_on_pattern_line_3 = auto()
    place_on_pattern_line_4 = auto()
    place_on_pattern_line_5 = auto()
    place_on_wall_1 = auto()
    place_on_wall_2 = auto()
    place_on_wall_3 = auto()
    place_on_wall_4 = auto()
    place_on_wall_5 = auto()

READABLE_ACTIONS = {
    Actions.take_factory_0_azul.value - 1: 'take_factory_0_azul',
    Actions.take_factory_0_yellow.value - 1: 'take_factory_0_yellow',
    Actions.take_factory_0_red.value - 1: 'take_factory_0_red',
    Actions.take_factory_0_black.value - 1: 'take_factory_0_black',
    Actions.take_factory_0_white.value - 1: 'take_factory_0_white',
    Actions.take_factory_1_azul.value - 1: 'take_factory_1_azul',
    Actions.take_factory_1_yellow.value - 1: 'take_factory_1_yellow',
    Actions.take_factory_1_red.value - 1: 'take_factory_1_red',
    Actions.take_factory_1_black.value - 1: 'take_factory_1_black',
    Actions.take_factory_1_white.value - 1: 'take_factory_1_white',
    Actions.take_factory_2_azul.value - 1: 'take_factory_2_azul',
    Actions.take_factory_2_yellow.value - 1: 'take_factory_2_yellow',
    Actions.take_factory_2_red.value - 1: 'take_factory_2_red',
    Actions.take_factory_2_black.value - 1: 'take_factory_2_black',
    Actions.take_factory_2_white.value - 1: 'take_factory_2_white',
    Actions.take_factory_3_azul.value - 1: 'take_factory_3_azul',
    Actions.take_factory_3_yellow.value - 1: 'take_factory_3_yellow',
    Actions.take_factory_3_red.value - 1: 'take_factory_3_red',
    Actions.take_factory_3_black.value - 1: 'take_factory_3_black',
    Actions.take_factory_3_white.value - 1: 'take_factory_3_white',
    Actions.take_factory_4_azul.value - 1: 'take_factory_4_azul',
    Actions.take_factory_4_yellow.value - 1: 'take_factory_4_yellow',
    Actions.take_factory_4_red.value - 1: 'take_factory_4_red',
    Actions.take_factory_4_black.value - 1: 'take_factory_4_black',
    Actions.take_factory_4_white.value - 1: 'take_factory_4_white',
    Actions.take_center_azul.value - 1: 'take_center_azul',
    Actions.take_center_yellow.value - 1: 'take_center_yellow',
    Actions.take_center_red.value - 1: 'take_center_red',
    Actions.take_center_black.value - 1: 'take_center_black',
    Actions.take_center_white.value - 1: 'take_center_white',
    Actions.place_on_pattern_line_1.value - 1: 'place_on_pattern_line_1',
    Actions.place_on_pattern_line_2.value - 1: 'place_on_pattern_line_2',
    Actions.place_on_pattern_line_3.value - 1: 'place_on_pattern_line_3',
    Actions.place_on_pattern_line_4.value - 1: 'place_on_pattern_line_4',
    Actions.place_on_pattern_line_5.value - 1: 'place_on_pattern_line_5',
    Actions.place_on_wall_1.value - 1: 'place_on_wall_1',
    Actions.place_on_wall_2.value - 1: 'place_on_wall_2',
    Actions.place_on_wall_3.value - 1: 'place_on_wall_3',
    Actions.place_on_wall_4.value - 1: 'place_on_wall_4',
    Actions.place_on_wall_5.value - 1: 'place_on_wall_5',
}

READABLE_ACTIONS_STOI = {v:k for k,v in READABLE_ACTIONS.items()}


ACTION_DICT = {
    0 : ActionType.take_factory_0,
    1 : ActionType.take_factory_0,
    2 : ActionType.take_factory_0,
    3 : ActionType.take_factory_0,
    4 : ActionType.take_factory_0,
    5 : ActionType.take_factory_1,
    6 : ActionType.take_factory_1,
    7 : ActionType.take_factory_1,
    8 : ActionType.take_factory_1,
    9 : ActionType.take_factory_1,
    10 : ActionType.take_factory_2,
    11 : ActionType.take_factory_2,
    12 : ActionType.take_factory_2,
    13 : ActionType.take_factory_2,
    14 : ActionType.take_factory_2,
    15 : ActionType.take_factory_3,
    16 : ActionType.take_factory_3,
    17 : ActionType.take_factory_3,
    18 : ActionType.take_factory_3,
    19 : ActionType.take_factory_3,
    20 : ActionType.take_factory_4,
    21 : ActionType.take_factory_4,
    22 : ActionType.take_factory_4,
    23 : ActionType.take_factory_4,
    24 : ActionType.take_factory_4,
    25 : ActionType.take_center,
    26 : ActionType.take_center,
    27 : ActionType.take_center,
    28 : ActionType.take_center,
    29 : ActionType.take_center,
    30 : ActionType.pick_pattern_line,
    31 : ActionType.pick_pattern_line,
    32 : ActionType.pick_pattern_line,
    33 : ActionType.pick_pattern_line,
    34 : ActionType.pick_pattern_line,
    35 : ActionType.place_tile_on_wall,
    36 : ActionType.place_tile_on_wall,
    37 : ActionType.place_tile_on_wall,
    38 : ActionType.place_tile_on_wall,
    39 : ActionType.place_tile_on_wall,
}


class Action:
    def __init__(self,tile_type,action_type,factory_n=None):
        self.tile_type = tile_type
        self.action_type = action_type
        self.factory_n = factory_n