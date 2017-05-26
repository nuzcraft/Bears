import libtcodpy as lib
import variables as var
from Tile import Tile
from Rect import Rect
from createroom import createroom
from Entity import Entity

def makedungeon():
    var.dungeon = [[Tile(True)
                    for y in range(var.dungeon_con_height)]
                   for x in range(var.dungeon_width)]

    rooms = []
    num_rooms = 0

    for r in range(var.max_rooms):
        # random width and height
        w = lib.random_get_int(0, var.room_min_size, var.room_max_size)
        h = lib.random_get_int(0, var.room_min_size, var.room_max_size)
        # random position without going outside the boundaries of the map, leaving the walls
        x = lib.random_get_int(0, 1, var.dungeon_width - w - 2)
        y = lib.random_get_int(0, 1, var.dungeon_height - h - 2)

        # rect class makes rectangles easier to work with
        new_room = Rect(x + var.dungeon_offset_x, y + var.dungeon_offset_y, w, h)

        # run through the other rooms and see if they intersect with this one
        failed = False
        for other_room in rooms:
            if new_room.intersect(other_room):
                failed = True
                break

        if not failed:
            # this room is valid
            # "paint" it to the maps tiles
            createroom(new_room)
            # center coordinates will be useful
            (new_x, new_y) = new_room.center()
            (new_x, new_y) = (new_x + var.dungeon_offset_x, new_y + var.dungeon_offset_y)
            room_no = Entity(new_x, new_y, chr(65 + num_rooms), lib.white)
            var.objects.insert(0, room_no)
            if num_rooms == 0:
                # this is the first room, where the player starts at
                var.player.x = new_x
                var.player.y = new_y
        # finally, append new room to the list
        rooms.append(new_room)
        num_rooms += 1
