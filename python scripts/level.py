import pygame
import tileclass
import objectclass

def detection(object_list,object_index,direction,x_change,y_change,tile_list,tile_size,grid_size):
    #handles movement of player in the desired direction if possible, as well as making sure crates are pushed correctly by the player and other crates and act solid if pushed against a wall
    for item in object_list:
        if direction == "up":
            condition = item.y > 50 and tile_list[((round((item.y - 50) / tile_size) - 1) * grid_size) + round((item.x - 50) / tile_size)].is_floor()
        elif direction == "down":
            condition = item.y < (550 - tile_size) and tile_list[((round((item.y - 50) / tile_size) + 1) * grid_size) + round((item.x - 50) / tile_size)].is_floor()
        elif direction == "left":
            condition = item.x > 50 and tile_list[(round((item.y - 50) / tile_size) * grid_size) + (round((item.x - 50) / tile_size) - 1)].is_floor()
        elif direction == "right":
            condition = item.x < (550 - tile_size) and tile_list[(round((item.y - 50) / tile_size) * grid_size) + (round((item.x - 50) / tile_size) + 1)].is_floor()
        if object_list.index(item) == object_index and condition:
            for item2 in object_list:
                if item2.name == "crate" and item.x + x_change == item2.x and item.y + y_change == item2.y:
                    if detection(object_list,object_list.index(item2),direction,x_change,y_change,tile_list,tile_size,grid_size):
                        item.new_coords(item.x + x_change,item.y + y_change)
                        if item.name == "crate":
                            return True
                        else:
                            return
                    else:
                        return
            item.new_coords(item.x + x_change,item.y + y_change)
            return True
    if object_list[object_index].name == "crate":
        return False

def create_level(size,level_tiles,level_objects):
    #creates a level with customizable grid size and tiles (see bottom for an example)
    #NOTE: THIS FUNCTION DOES NOT WORK THE WAY IT WILL WORK IN THE FINAL GAME. THE PYGAME INITIALIZATION AND EXIT WILL BE ELSEWHERE ONCE A MAIN MENU/LEVEL SELECT IS CREATED
    
    pygame.init()
    screen = pygame.display.set_mode([600,600])
    background = pygame.Surface((600,600))
    background.fill((0,0,0))
    background.convert()
    clock = pygame.time.Clock()
    FPS = 30

    #creates the grid and the lists containing the tiles and objects
    grid_size = size
    tile_size = 500 / size
    tiles = []
    objects = []
    for y in range(grid_size):
        for x in range(grid_size):
            tiles.append(tileclass.Tile(round(x * tile_size) + 50,round(y * tile_size) + 50,level_tiles[(y * grid_size) + x]))
    for item in level_objects:
        objects.append(objectclass.Object(round((item[0] - 1) * tile_size) + 50,round((item[1] - 1) * tile_size) + 50,item[2]))

    #runs the level, allows the map to be visualised, and detects movement inputs and sends them to the collision detection function
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    detection(objects,0,"up",0,0 - tile_size,tiles,tile_size,grid_size)
                if event.key == pygame.K_DOWN:
                    detection(objects,0,"down",0,tile_size,tiles,tile_size,grid_size)
                if event.key == pygame.K_LEFT:
                    detection(objects,0,"left",0 - tile_size,0,tiles,tile_size,grid_size)
                if event.key == pygame.K_RIGHT:
                    detection(objects,0,"right",tile_size,0,tiles,tile_size,grid_size)         
        screen.blit(background,(0,0))
        for i in range(len(tiles)):
            screen.blit(pygame.transform.scale(tiles[i].variant,(round(tile_size),round(tile_size))),(tiles[i].x,tiles[i].y))
        for i in range(len(objects)):
            screen.blit(pygame.transform.scale(objects[i].variant,(round(tile_size),round(tile_size))),(objects[i].x,objects[i].y))
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()

create_level(5,[1,1,1,1,1,1,1,1,1,1,1,2,1,0,0,1,1,1,1,1,1,1,1,1,1],[[1,3,0],[3,4,1],[3,3,1]])
