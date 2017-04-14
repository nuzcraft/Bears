"""Class File for a gameobject"""
from bearlibterminal import terminal
import variables as var


class GameObject:
    def __init__(self, name, layers, x, y):
        self.name = name
        self.layers = layers
        self.x = x
        self.y = y

    def draw(self):
        layer_num = 1
        for layer in self.layers:
            x_offset = layer[0]
            y_offset = layer[1]
            char = layer[2]
            color = layer[3]
            terminal.layer(layer_num)
            layer_num += 1
            terminal.color(terminal.color_from_name(color))
            terminal.put_ext(self.x - var.map_offset_x, self.y - var.map_offset_y, x_offset, y_offset, char)

