"""This file will handle input from the player"""
from bearlibterminal import terminal
import variables as var


def handle_keys():
    """handle input from the player"""
    if terminal.has_input():
        key = terminal.read()
        # this section is inputs that take a turn
        if key == terminal.TK_RIGHT:
            # move the player right
            # check whether the map can move
            if not var.map_width - var.map_offset_x <= var.game_width:
                # check if they are within the 'border' if so, move the map
                if (var.player.x - var.map_offset_x
                        >= var.game_width - var.game_border):
                    var.map_offset_x += 1
            # check if the player is going to move outside the map
            if var.player.x - var.map_offset_x < var.game_width - 1:
                return var.player.move(1, 0)
            else:
                return 'idle'
        elif key == terminal.TK_LEFT:
            # move the player left
            # check whether the map can move
            if var.map_offset_x > 0:
                # check if they are within the 'border' if so, move the map
                if var.player.x - var.map_offset_x < var.game_border:
                    var.map_offset_x -= 1
            # check if the player is going to move outside the map
            if var.player.x - var.map_offset_x > 0:
                return var.player.move(-1, 0)
            else:
                return 'idle'
        elif key == terminal.TK_DOWN:
            # move the player down
            # check whether the map can move
            if not var.map_height - var.map_offset_y <= var.game_height:
                # check if they are within the 'border' if so, move the map
                if (var.player.y - var.map_offset_y
                        >= var.game_height - var.game_border):
                    var.map_offset_y += 1
            # check if the player is going to move outside the map
            if var.player.y - var.map_offset_y < var.game_height - 1:
                return var.player.move(0, 1)
            else:
                return 'idle'
        elif key == terminal.TK_UP:
            # move the player up
            # check whether the map can move
            if var.map_offset_y > 0:
                # check if they are within the 'border' if so, move the map
                if var.player.y - var.map_offset_y < var.game_border:
                    var.map_offset_y -= 1
            # check if the player is going to move outside the map
            if var.player.y - var.map_offset_y > 0:
                return var.player.move(0, -1)
            else:
                return 'idle'
        # this section is inputs that should not
        if key == terminal.TK_ESCAPE:
            return 'exit'
    else:
        return 'idle'
