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
# the dungeon offset is used to center and move the dungeon when it's larger than the screen
dungeon_offset_x = (dungeon_con_width - dungeon_width) / 2
dungeon_offset_y = (dungeon_con_height - dungeon_height) / 2

dungeon = [[Tile(True)
            for x in range(dungeon_width)]
           for y in range(dungeon_height)]

player = Entity(2, 2, '@', lib.white)

# room definitions
room_max_size = 1
room_min_size = 1
max_rooms = 26

# objects
objects = []

