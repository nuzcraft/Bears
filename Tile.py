import libtcodpy as lib

class Tile:
    def __init__(self, blocked, char="#", color=lib.grey):
        self.blocked = blocked
        self.char = char
        self.color = color
