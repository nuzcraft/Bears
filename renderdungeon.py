import libtcodpy as lib
import variables as var


def renderdungeon():
    # draw the dungeon
    for y in range(var.dungeon_width):
        for x in range(var.dungeon_height):
            lib.console_set_default_foreground(var.dungeon_con, var.dungeon[x][y].color)
            lib.console_put_char(var.dungeon_con, x + var.dungeon_offset_x, y + var.dungeon_offset_y, var.dungeon[x][y].char, lib.BKGND_NONE)


