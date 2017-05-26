import variables as var

def isblocked(x, y):
    if var.dungeon[x - var.dungeon_offset_x][y - var.dungeon_offset_y].blocked:
        return True