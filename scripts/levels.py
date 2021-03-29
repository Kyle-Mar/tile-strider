import levelclass
import settings

screen_size = [settings.resolution_x, settings.resolution_y]
screen_offset = [(screen_size[0] - 500) / 2, (screen_size[1] - 500) / 2]

level50 = levelclass.Level(8, [2, 2, 2, 2, 2, 2, 2, 9,
                               2, 8, 1, 1, 1, 1, 2, 9,
                               2, 1, 1, 1, 1, 1, 2, 9,
                               2, 1, 2, 1, 0, 0, 2, 9,
                               2, 1, 1, 1, 1, 1, 2, 9,
                               2, 1, 1, 1, 1, 1, 2, 9,
                               2, 2, 2, 2, 2, 2, 2, 9,
                               9, 9, 9, 9, 9, 9, 9, 9], [[2, 2, 0], [3, 5, 1]], screen_offset)

level51 = levelclass.Level(5, [8, 1, 1, 1, 1,
                               1, 1, 1, 1, 1,
                               1, 1, 4, 1, 1,
                               1, 1, 1, 1, 1,
                               1, 1, 1, 1, 7], [[1, 1, 0], [3, 3, 1]], screen_offset)

level52 = levelclass.Level(20, [9, 2, 2, 2, 9, 9, 9, 9, 9, 9, 2, 2, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 2, 1, 1, 1, 0, 7, 1, 1, 1, 1, 1, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 2, 1, 1, 1, 2, 9, 9, 2, 1, 1, 1, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 2, 0, 1, 0, 2, 9, 9, 2, 0, 1, 0, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 2, 2, 2, 1, 1, 8, 1, 1, 1, 2, 2, 2, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 2, 2, 9, 9, 9, 9, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                           [[7, 9, 0], [4, 4, 1], [11, 4, 1]], screen_offset)

menu1 = levelclass.Level(6, [9, 9, 9, 9, 9, 9,
                             9, 7, 9, 9, 7, 9,
                             1, 1, 1, 1, 1, 1,
                             1, 1, 1, 1, 1, 1,
                             9, 8, 1, 1, 1, 9,
                             9, 9, 9, 9, 9, 9], [[2, 5, 0], [3, 5, 1]], screen_offset)

menu2 = levelclass.Level(6, [9, 9, 9, 9, 9, 9,
                             1, 9, 1, 9, 1, 9,
                             1, 1, 1, 1, 1, 1,
                             8, 1, 1, 1, 1, 1,
                             9, 1, 9, 1, 9, 1,
                             9, 9, 9, 9, 9, 9, ], [[1, 4, 0]], screen_offset)

menu3 = levelclass.Level(6, [9, 9, 9, 9, 9, 9,
                             1, 9, 1, 9, 1, 9,
                             1, 1, 1, 1, 1, 7,
                             8, 1, 1, 1, 1, 1,
                             9, 1, 9, 1, 9, 1,
                             9, 9, 9, 9, 9, 9, ], [[1, 4, 0]], screen_offset)

menu4 = levelclass.Level(6, [9, 9, 9, 9, 9, 9,
                             1, 9, 1, 9, 1, 9,
                             1, 1, 1, 1, 1, 1,
                             8, 1, 1, 1, 1, 1,
                             9, 1, 9, 1, 9, 1,
                             9, 9, 9, 9, 9, 9, ], [[1, 4, 0]], screen_offset)