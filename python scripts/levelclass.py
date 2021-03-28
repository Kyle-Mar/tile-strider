import objectclass
import tileclass


class Level(object):
    def __init__(self, size, tiles, objects, offsets):
        """
        :param int Level Size, ArrayList Level Tiles, ArrayList, Objects
        """
        self.size = size
        self.tiles = []
        self.objects = []
        self.tile_size = 500 / size
        self.offsets = offsets

        # creates the grid and the lists containing the tiles and objects

        for y in range(size):
            for x in range(size):
                self.tiles.append(tileclass.Tile((x * self.tile_size) + offsets[0],
                                                 (y * self.tile_size) + offsets[1], tiles[(y * size) + x]))
                
        for item in objects:
            self.objects.append(objectclass.Object(((item[0] - 1) * self.tile_size) + offsets[0],
                                                   ((item[1] - 1) * self.tile_size) + offsets[1], item[2]))

    def detection(self, direction, x_change, y_change, screen_size):
        #triggers the player movement
        self.objects[0].movement(self.objects, 0, direction, x_change, y_change, self.tiles, self.tile_size, self.size, self.offsets, screen_size)
