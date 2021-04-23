class LevelManager(object):
    def __init__(self):
        """
        :return LevelManager Object
        """
        self.level_list = []
        self.current_level = 0
        self.moves = 0
        self.moving_state = 0
        # create a way to quickly change the current level with integers

    def level(self):

        return self.current_level
