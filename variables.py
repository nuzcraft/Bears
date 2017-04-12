"""This file will hold all constant and global variables"""

# game settings
game_height = 40
game_width = 40
game_border = 5

# map settings
map_height = 50
map_width = 50
map_array = [[0 for x in range(map_width)] for y in range(map_height)]
# the offset will be used to move the map behind the terminal
map_offset_x = 0
map_offset_y = 0

# player settings
# x and y represent location on the map
player_x = 10
player_y = 10
player_char = '@'
player_action = 'idle'

