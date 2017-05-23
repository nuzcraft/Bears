import libtcodpy as lib
from Entity import Entity
from Tile import Tile

first_run = 1

screen_width = 12
screen_height = 22
limit_fps = 20

# create the dungeon console
dungeon_con_y = -7
dungeon_con_width = 12
dungeon_con_height = 12
dungeon_con = lib.console_new(dungeon_con_width, dungeon_con_height)

dungeon_width = 10
dungeon_height = 10
dungeon_offset_x = 0
dungeon_offset_y = 0

dungeon = [[Tile(True)
            for x in range(dungeon_width)]
           for y in range(dungeon_height)]

player = Entity(dungeon_con_width / 2, dungeon_con_height / 2, '@', lib.white)

