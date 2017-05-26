import libtcodpy as lib
import variables as var
from isblocked import isblocked


class Entity:
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def draw(self):
        lib.console_set_default_foreground(var.dungeon_con, self.color)
        lib.console_put_char(var.dungeon_con, self.x, self.y, self.char, lib.BKGND_NONE)

    def clear(self):
        lib.console_put_char(var.dungeon_con, self.x, self.y, ' ', lib.BKGND_NONE)

    def move(self, dx, dy):
        if not isblocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy
