import variables as var


def createroom(room):
    for x in range(room.x1, room.x2):
        for y in range(room.y1, room.y2):
            var.dungeon[x][y].blocked = False
            var.dungeon[x][y].char = " "
