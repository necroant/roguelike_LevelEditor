from random import randint
import constants


class Tile:
    def __init__(self, symbol='.', color=7, passable=True, breakable=False, inventory=None):
        self._symbol = symbol
        self._color = color
        self._passable = passable
        self._breakable = breakable
        self._inventory = inventory

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, symbol_: str):
        self._symbol = symbol_

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color_: int):
        if color_ not in range(8):
            self._color = 7
        else:
            self._color = color_

    @property
    def passable(self):
        return self._passable

    @passable.setter
    def passable(self, passable_: bool):
        self._passable = passable_

    @property
    def breakable(self):
        return self._breakable

    @breakable.setter
    def breakable(self, breakable_: bool):
        self._breakable = breakable_

    # TODO: inventory


def create(settings: 'dict', dungeon_type=constants.CAVERN):
    dungeon_width = settings["Width"]
    dungeon_height = settings["Height"]

    dungeon_layout = [[Tile() for _ in range(dungeon_height)] for _ in range(dungeon_width)]

    if dungeon_type == constants.CAVERN:
        for i in range(dungeon_width):
            for j in range(dungeon_height):
                if i == 0 or j == 0 or i == dungeon_width-1 or j == dungeon_height-1:
                    tile = Tile(symbol='#', passable=False)     # Impassible walls
                    dungeon_layout[i][j] = tile
                else:
                    chance = randint(0, 9)
                    if chance == 0:                             # Randomly placed boulders
                        tile = Tile(symbol='#', passable=False, breakable=True)
                        dungeon_layout[i][j] = tile
    else:
        ...

    return dungeon_layout
