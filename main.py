import libtcodpy as lib
import variables as var
from handlekeys import handlekeys

lib.console_set_custom_font('arial10x10.png', lib.FONT_TYPE_GRAYSCALE | lib.FONT_LAYOUT_TCOD)
lib.console_init_root(var.screen_width, var.screen_height, 'Bears', False)
lib.sys_set_fps(var.limit_fps)

while not lib.console_is_window_closed():
    lib.console_set_default_foreground(0, lib.white)
    lib.console_put_char(0, var.playerx, var.playery, '@', lib.BKGND_NONE)
    lib.console_flush()
    lib.console_put_char(0, var.playerx, var.playery, ' ', lib.BKGND_NONE)

    # handle keys and exit if needed
    exit_game = handlekeys()
    if exit_game:
        break
