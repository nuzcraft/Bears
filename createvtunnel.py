import variables as var

def createhtunnel(y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2)):
        var.dungeon[x][y].blocked = False
        var.dungeon[x][y].char = " "