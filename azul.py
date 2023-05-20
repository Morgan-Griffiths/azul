from enum import Enum, auto
from actions import ACTION_DICT, READABLE_ACTIONS_STOI, ActionType,READABLE_ACTIONS
from factory import Factory
from helpers import COLOR_DICT_STOI, COLORS,COLOR_DICT_ITOS
from board import Board
import numpy as np
from collections import deque
import random

from player import Player
from tiles import TileBag
""" 
Azul has 5 colors. 
azul, yellow, red, black, white

the board
A,Y,R,B,W
W,A,Y,R,B
B,W,A,Y,R
R,B,W,A,Y
Y,R,B,W,A

This is a reinforcement learning project.

action space: 35
state space: 82

game states:
game while score < 100:
    Round:
        picking tiles from factory -> same player
        placing picked tiles on pattern line -> same player
        switch players
    End of round:
        while tiles:
            place tiles on wall
        switch player
    score player

"""


class Azul:
    def __init__(self,n_players):
        self.n_players = n_players
        
    def reset(self):
        self.current_player = 0
        self.players = [Player() for _ in range(self.n_players)]
        self.tile_bag = TileBag()
        self.factory = Factory(self.n_players,self.tile_bag)
        self.discard_pile = []
        self.game_over = False
        self.picking_factory = True
        self.picking_pattern_line = False
        self.placing_tiles = False
        return self.return_player_state(),self.return_valid_actions(),self.game_over

    def increment_player_state(self):
        """ we only increment player when we're done picking a factory. """
        if self.picking_factory == True:
            self.picking_factory = False
            self.picking_pattern_line = True
        elif self.picking_pattern_line == True:
            self.picking_pattern_line = False
            self.picking_factory = True
            self.current_player = (self.current_player + 1) % self.n_players
        elif self.placing_tiles == True:
            if not any(player.can_place_tiles_from_pattern_lines() for player in self.players):
                # repopulate the factory.
                self.factory.reset(self.tile_bag)
                self.placing_tiles = False
                self.picking_factory = True
                self.current_player = (self.current_player + 1) % self.n_players
            else:
                if not self.players[self.current_player].can_place_tiles_from_pattern_lines():
                    self.current_player = (self.current_player + 1) % self.n_players


    def return_player_state(self):
        """ 
        the state of Azul. 
        there are 25 tiles on the board.
        there are 5 factories with 4 tiles each.
        there are a maximum of 19 tiles in the center.
        boolean for if the center has been taken from.
        boolean for if we're choosing a color.
        boolean for if we're choosing a factory.
        boolean for if we're choosing a floor line.
        15 len vector for the choosen tiles.
        that would be a 25 + 20 + 19 + 3 + 15 = 82 dimensional state.        
        """
        state = []
        state.extend(self.players[self.current_player].get_state())
        state.extend(self.factory.get_state())
        state.extend([self.picking_factory,self.picking_pattern_line,self.placing_tiles])
        state = [COLOR_DICT_STOI[t] if isinstance(t,str) else t for t in state ]
        return np.array(state,dtype=np.int8)
    
    def get_color_from_action(self,action:int):
        return COLORS[action % 5]
    
    def get_pattern_line_from_action(self,action:int):
        return action % 5
    
    def return_action_vector(self):
        return np.zeros(len(ACTION_DICT),dtype=np.int8)
    
    def get_color_playable(self,color):
        open_rows = self.players[self.current_player].board.open_rows_for_color(color)
        open_lines = self.players[self.current_player].pattern_lines.get_open_lines(color)
        union = set(open_rows).union(set(open_lines))
        return union

    
    def return_valid_actions(self):
        action_vector = self.return_action_vector()
        # prevent the picking of a color if the board is full or no pattern line is open.
        if self.picking_factory == True:
            for i in range(5):
                vector_idx = i*5
                for j,color in enumerate(COLORS):
                    if self.factory.can_take_from_factory(i,color) and any(self.get_color_playable(color)):
                        action_vector[vector_idx+j] = 1
            vector_idx = 25
            for i,color in enumerate(COLORS):
                if self.factory.can_take_from_center(color):
                    action_vector[vector_idx+i] = 1
        else:
            # check if pattern lines are open, and if so, if the color is valid. And if the color matches the current color of the pattern line.
            chosen_color = self.players[self.current_player].chosen_tokens[0]
            union = self.get_color_playable(chosen_color)
            print('union')
            for row in union:
                action_vector[READABLE_ACTIONS_STOI['place_on_pattern_line_1'] + row] = 1
        return action_vector
    
    def is_placing_tile_state(self):
        """ Clear any pattern lines that are filled -> move to board. All tiles on factory and center must be gone for round to be over """
        if self.factory.is_empty():
            self.placing_tiles = True
        

    def is_game_over(self):
        """ if any player has reached 100 points, the game is over. """
        return any([player[self.current_player].score >= 100 for player in self.players])
        

    def done(self):
        """ Game is over when a player completes a row. """
        return any([player[self.current_player].board.is_row_complete() for player in self.players])
    

    def step(self,action:int):
        color = self.get_color_from_action(action)
        print('color',color)
        print('action',action)
        pattern_line_row = action % 5
        if ACTION_DICT[action] in [ActionType.take_factory_0,ActionType.take_factory_1,ActionType.take_factory_2,ActionType.take_factory_3,ActionType.take_factory_4]:
            # tile type
            tiles = self.factory.draw_tile_from_factory(pattern_line_row,color)
            self.players[self.current_player].chosen_tokens = tiles
        elif ACTION_DICT[action] == ActionType.take_center:
            tiles = self.factory.draw_from_center(color)
            self.players[self.current_player].chosen_tokens = tiles
        elif ACTION_DICT[action] == ActionType.pick_pattern_line:
            self.players[self.current_player].place_on_pattern_line(pattern_line_row)
            # if factory is empty, round is over.
            if self.factory.is_empty():
                self.placing_tiles = True
        elif ACTION_DICT[action] == ActionType.place_tile_on_wall:
            extra_tokens = self.players[self.current_player].place_on_board(pattern_line_row)
            self.tile_bag.extend(extra_tokens)
        else:
            raise ValueError("Invalid action")
        state = self.return_player_state()
        valid_actions = self.return_valid_actions()
        self.increment_player_state()
        return state,valid_actions,self.game_over


    def display(self):
        print("Player: {}".format(self.current_player))
        self.players[self.current_player].display()
        self.factory.display()
        print("Picking Factory: {}".format(self.picking_factory))
        print("Picking Pattern Line: {}".format(self.picking_pattern_line))
        print("Placing Tiles: {}".format(self.placing_tiles))
        actions = self.return_valid_actions()
        mask = np.where(actions == 1)[0]
        readable_actions = [READABLE_ACTIONS[a] for a in mask]
        print(actions)
        print(mask)
        print("Valid Actions: {}".format(readable_actions))


