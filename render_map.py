"""render the map"""
from bearlibterminal import terminal
import variables as var


def render_map():
    """render the map"""
    for x in range(var.map_offset_x, var.map_width):
        for y in range(var.map_offset_y, var.map_height):
            if (x - var.map_offset_x < var.game_width and
                    y - var.map_offset_y < var.game_height):
                if var.map_array[x][y] == 0:
                    if y % 2 == 0:
                        terminal.layer(1)
                        terminal.color(terminal.color_from_name('lighter green'))
                        terminal.printf((x - var.map_offset_x)*2, y - var.map_offset_y, ' ')
                        terminal.layer(2)
                        terminal.color(terminal.color_from_name('green'))
                        terminal.put_ext((x - var.map_offset_x)*2, y - var.map_offset_y, -2, -3, ' ')
                    else:
                        terminal.layer(1)
                        terminal.color(terminal.color_from_name('dark green'))
                        terminal.printf((x - var.map_offset_x)*2, y - var.map_offset_y, ' ')


