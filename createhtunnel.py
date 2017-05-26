import variables as var

def createhtunnel(x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2)):
        var.dungeon[x][y].blocked = False
        var.dungeon[x][y].char = " "