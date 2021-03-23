import pygame

# class for objects that sit on top of tiles like the player and crates
player = pygame.image.load('../images/player.png')
crate = pygame.image.load('../images/crate.png')
objectset = [player, crate]
nameset = ["player", "crate"]


class Object(object):
    def __init__(self, x, y, variant):
        # creates an object (variant is what type of object it is, see the objectset list for info)
        self.x = x
        self.y = y
        self.variant = objectset[variant]
        self.name = nameset[variant]

    def x(self):
        # returns the object's x position
        return self.x

    def y(self):
        # returns the object's y position
        return self.y

    def variant(self):
        # returns the object's surface for blitting
        return self.variant

    def name(self):
        # returns the object's name
        return self.name

    def new_coords(self, new_x, new_y):
        # changes the object's coords to the new ones specified
        self.x = new_x
        self.y = new_y
