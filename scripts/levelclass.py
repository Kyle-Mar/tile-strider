import pygame
import objectclass
import tileclass
import gamedata
import levelmanager

class Level(object):
    def __init__(self, size, tiles, objects, background, text, offsets):
        """
        :param size: a grid of A x A tiles that define the level. int.
        :param tiles: the tiles that comprise the level. Array, ints.
        :param objects: the objects, including the player, that populate the level. Array, ints. (X pos, Y pos, Obj.)
        :param background: the background color associated to the level
        :param offsets: the offsets for the current screen size based on tile size
        """

        self.size = size
        self.tiles = []
        self.objects = []
        self.tile_size = 500 / size
        self.background = background
        self.offsets = offsets
        #we need to keep the moves property here in order to reset the world from other places
        self.moves = 0
        self.text_info = pygame.font.SysFont(None, 25, False)
        self.text = self.text_info.render(text, False, (255, 255, 255))
        # creates the grid and the lists containing the tiles and objects

        #turns level tile data into tiles
        for y in range(size):
            for x in range(size):
                self.tiles.append(tileclass.Tile((x * self.tile_size) + offsets[0],
                                                 (y * self.tile_size) + offsets[1], tiles[(y * size) + x][0], tiles[(y * size) + x][1]))

        #turns level object data into objects
        for item in objects:
            self.objects.append(objectclass.Object(((item[0] - 1) * self.tile_size) + offsets[0],
                                                   ((item[1] - 1) * self.tile_size) + offsets[1], item[2]))

        if gamedata.levelmanager is not None:
            gamedata.levelmanager.level_list.append(self)
        else:
            gamedata.levelmanager = levelmanager.LevelManager()
            gamedata.levelmanager.level_list.append(self)


    def undo(self):
        # triggers an undoing of the most recent move
        for item in self.tiles:
            item.back(1)
        for item in self.objects:
            item.back(1)

    def restart(self, moves):
        # triggers a full level restart
        for item in self.tiles:
            item.back(moves)
        for item in self.objects:
            item.back(moves)

    def go_back(self):
        # triggers going back to the original position if the undo button is pressed while objects are moving
        for item in self.tiles:
            item.back(0)
        for item in self.objects:
            item.back(0)

    def move_detection(self, screen_size):
        #triggers detection of if objects can move or not
        for item in self.objects:
            item.movement_detection(self.objects, self.tiles, self.tile_size, self.size, self.offsets, screen_size, self.objects.index(item))

    def move_cycle(self):
        #moves objects if they are able
        for item in self.objects:
            item.movement()

    def bg(self):
        # customizable per level background
        return self.background

    @property
    def moves(self):
        """
        :param: a Point
        :return int times slimed
        """
        return self._moves

    @moves.setter
    def moves(self, value):
        """
        :param: a Level and new value
        :return: changes moves count to new value
        """
        if isinstance(value, int):
            self._moves = value
