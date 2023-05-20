
from helpers import COLOR_DICT_STOI


class Factory:
    def __init__(self,n_players,tile_bag):
        self.n_players = n_players
        self.factories = [tile_bag.draw(4) for _ in range(1 + (n_players * 2))]
        self.center = []
        self.one = True

    def reset(self,tile_bag):
        self.__init__(self.n_players,tile_bag)

    def draw_tile_from_factory(self,factory_choice,color):
        print(f'drawing color {color} from factory {factory_choice}',self.factories)
        taken = [tile for tile in self.factories[factory_choice] if tile == color]
        print('taken',taken)
        if len(taken):
            self.center.extend([tile for tile in self.factories[factory_choice] if tile != color])
            self.factories[factory_choice] = [0]
        # remaining go into center
        print('center',self.center)
        print('factories',self.factories)
        return taken
    
    def draw_from_center(self,color):
        one_taken = self.one
        taken = [tile for tile in self.center if tile == color]
        self.one = False
        return taken,one_taken
    
    def can_take_from_center(self,color:str):
        return color in self.center
    
    def can_take_from_factory(self,factory_choice,color: str):
        return self.factories[factory_choice] and color in self.factories[factory_choice]
    
    def get_state(self):
        state = []
        for factory in self.factories:
            state.extend([tile for tile in factory])
        state.extend([tile for tile in self.center])
        return state

    def is_empty(self):
        return all([not factory for factory in self.factories] + [len(self.center) == 0])
    
    def display(self):
        for i in range(5):
            print("Factory {}: {}".format(i,self.factories[i]))
        print(f'Center: {self.center}')