"""Class File for an entity"""
from bearlibterminal import terminal
import variables as var


class Entity:
    def __init__(self, name, layers, x, y, blocks):
        """initialize an entity"""
        self.name = name
        self.layers = layers
        self.x = x
        self.y = y
        self.blocks = blocks

    def draw(self):
        """loop through the layers of an entity (starting at layer 1) and put them on a screen"""
        for layer in self.layers:
            x_offset = layer[0]
            y_offset = layer[1]
            char = layer[2]
            color = layer[3]
            layer_num = self.layers.index(layer) + 1
            terminal.layer(layer_num)
            terminal.color(terminal.color_from_name(color))
            terminal.put_ext((self.x - var.map_offset_x) * 2, self.y - var.map_offset_y, x_offset, y_offset, char)

    def clear(self):
        """clear the layers of an entity"""
        for layer_num in range(len(self.layers)):
            terminal.layer(layer_num)
            terminal.clear_area(self.x * 2, self.y, 1, 1)

    def move(self, dx, dy):
        """moves the entity dx, dy, if possible"""
        for entity in var.entities:
            # TODO: Fix this if not statement
            if not (entity.x == self.x + dx and entity.y == self.y + dy
                    and entity != self and entity.blocks):
                self.x += dx
                self.y += dy
                return 'moving'
        return 'idle'




